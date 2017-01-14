#!/bin/bash




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
