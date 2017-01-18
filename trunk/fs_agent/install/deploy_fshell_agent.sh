#!/bin/bash

# Fshell v1.0 release.
# This is an install script of linux for fshell agent.
# For more information, see <http://www.s0nnet.com>
# if have any question, mailto: s0nnet@qq.com.
#

CUR_VERSION="1.0"
LOG_FILE=fshell_agent.install.log


log_to_file()
{
    echo $1
    echo $1 >> ${LOG_FILE}
}

log_result()
{
    if [ $2 -ne 0 ];then
        log_to_file "[-] $1 failed!"
    else
        log_to_file "[+] $1 successed!"
    fi
}


backup_file()

{
    echo "backup $1 > $1.bak"
    cp $1 $1.bak
}




deploy_fshell_agent()
{
    install_basic_suite
    setup_iptables
    add_user
    install_web_suite
    install_nginx
    install_mysql
    install_python_venv
    config_web_suite
    install_service
}


install_fshell_agent()
{


}

case "$1" in
    deploy)
        deploy_fshell_agent
    ;;
    install)
        install_fshell_agent
    ;;
    service)
        restart_service
    ;;
    *)
        echo "args error: $1"
        exit -1
    ;;
esac
