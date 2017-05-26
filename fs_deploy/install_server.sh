#!/bin/bash
#
##    fshell服务端自动化部署脚本
#
#  执行相关操作：
#       install_basic_suite
#       install_nginx
#       install_mysql
#
#       config_python_venv
#       start_fs_server


CUR_VERSION="1.0"
LOG_FILE=logs/deploy_`date +"%F_%H-%M-%S"`.log
ITEM_FILE=logs/deploy_`date +"%F_%H-%M-%S"`.item.log

mkdir -p /home/s0nnet/logs
chown -R s0nnet:s0nnet /home/s0nnet/logs


#begin: log util
log_to_file ()
{
    echo "$1"
    echo "$1" >> ${LOG_FILE}
}

log_to_item()
{
    echo "  $1" >> ${ITEM_FILE}
}

log_header()
{
    log_to_file "==========================================================="
    log_to_file "      begin to install fshell server, version: ${CUR_VERSION} "
    log_to_file "==========================================================="
    log_to_file ""

    log_to_item "==========================================================="
    log_to_item "      begin to install fshell server, version: ${CUR_VERSION} "
    log_to_item "==========================================================="
    log_to_item ""
}

log_module()
{
    log_to_file ""
    log_to_file "<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<"
    log_to_file "current step:  $1"
    log_to_file "proccessing..."

    log_to_item ""
    log_to_item "<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<"
    log_to_item "current step:  $1"
    log_to_item ">-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->"
    log_to_item ""
}

log_module_result()
{
    if [ $2 != 0 ];then
        log_to_file "$1 failed !!!!!!!!!!!!!!!!!!!!!!!!"
    else
        log_to_file "$1 successfully ...."
    fi
    log_to_file ">-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->"
}

failed_and_exit()
{
    log_to_file "$2"
    log_module_result "$1" 1
    exit -1
}

#may 3 args: 1,2 for failed, 3 for success but optional
check_failed(){
	if [ $? != 0 ]; then
		failed_and_exit "$1" "$2"
	else
		log_to_file "$3"
	fi
}
#end: log util



# description:
#       install basic software
# category:
#       software install
install_basic_suite(){
    cur_module="install_basic_suite"
    log_module  ${cur_module}
    log_to_file "begin to install basic suite"

    suite=(
        "gcc --version"
        "g++ --version"
        "ifconfig  --version"
		"pip --version"
		"virtualenv --version"
		"vim --version"
		"wget --version"
        "curl --version"
        "openssl version"
        "supervisord -v"
    )
    length=${#suite[@]}

    yum install -y epel-release
    yum install -y gcc gcc-c++
    yum install -y screen
    yum install -y net-tools
    yum install -y python-devel
    yum install -y mysql-devel
    yum install -y python-pip
    yum install -y python-virtualenv
    yum install -y vim wget
    yum install -y curl-devel  openssl-devel
    yum install -y supervisor

    for ((i=0; i<$length; i++))
    do
		${suite[$i]} > /dev/null
		check_failed ${cur_module} \
			"install failed:${suite[$i]}" \
			"installed:${suite[$i]}"
    done

    log_module_result ${cur_module} 0
}

# description:
#       install nginx software
# category:
#       software install
install_nginx(){
    cur_module="install_nginx"
    log_module  ${cur_module}
    log_to_file "begin to install_nginx"

	#if no spec nginx, install by yum
	systemctl status nginx.service
	if [ $? != 0 ]; then
		log_to_file "[!] no nginx installed! will install general nginx"
		yum -y install nginx
        
        log_to_file "[*] configure nginx"
        cp -f /home/s0nnet/fshell/trunk/fs_deploy/fss_conf/nginx/nginx.conf /etc/nginx/
        cp -f /home/s0nnet/fshell/trunk/fs_deploy/fss_conf/nginx/fshell.conf /etc/nginx/conf.d/
	else
		log_to_file "[!] specific nginx installed! pass"
	fi

    systemctl enable nginx.service
    systemctl start nginx.service

    log_module_result ${cur_module} 0
}

# description:
#       install mysql software
# category:
#       software install
install_mysql(){
    cur_module="deploy_mysql_db"
    log_module  ${cur_module}
    log_to_file "begin to deploy_mysql"

    log_to_file "[*] begin to install mysql"
    yum -y mysql mysql-server mysql-client

    log_to_file "[*] begin to start mysql service"
    systemctl enable mysql.service
    systemctl start mysql.service

	log_module_result ${cur_module} 0
}

# description:
#       deploy python_venv environment
# category:
#       software deploy
config_python_venv(){
    cur_module="config_python_venv"
    log_module  ${cur_module}
    log_to_file "begin to config_python_venv"
    
    log_to_file "[*] configure python virtualenv"
    cd /home/s0nnet
    rm -rf venv; virtualenv venv --no-site-packages;
    /home/s0nnet/venv/bin/pip install -r /home/s0nnet/fshell/trunk/fs_deploy/fss_conf/pip/requirements.txt > /dev/null
    cd -
    
    log_module_result ${cur_module} 0
}

# description:
#       deploy supervisor environment
# category:
#       software start service
start_fs_server(){
    cur_module="start_fs_server"
    log_module  ${cur_module}
    log_to_file "begin to start fs_server service"

    log_to_file "[*] configure supervisor"
    rm -rf /etc/supervisord.d/*
    cd /home/s0nnet/fshell/trunk/fs_deploy/fss_conf/    
    cp -f supervisor/fs_kernel.conf /etc/supervisord.d/
    cp -f supervisor/fs_srv.conf /etc/supervisord.d/
    cp -f supervisor/fs_sync.conf /etc/supervisord.d/
    cp -f supervisor/fs_web.conf /etc/supervisord.d/
    cp -f supervisor/supervisord.conf /etc/
    cd -

    log_to_file "[*] start supervisor"
    /usr/bin/supervisord -c /etc/supervisord.conf

    log_module_result ${cur_module} 0
}


deploy_server(){
	log_header
    install_basic_suite
    install_nginx
    install_mysql

    config_python_venv
    start_fs_server
}

install_server


