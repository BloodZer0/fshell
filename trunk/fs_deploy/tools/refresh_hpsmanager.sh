#!/bin/sh
HPS_MANAGER_PATH=/home/moresec/hps_manager
HPS_MANAGER_DASHBOARD=${HPS_MANAGER_PATH}/src/web_user/templates/dashboard.html
HPS_MAIL_STORE=${HPS_MANAGER_PATH}/src/data_sync/email_warning/email_store.py
HPS_MAIL_SYNC=${HPS_MANAGER_PATH}/src/data_sync/email_warning/email_sync.py
HPS_INSTALL_PAGE1=/home/moresec/hps_install/src/web/templates/index.html
HPS_INSTALL_PAGE2=/home/moresec/hps_install/src/web/templates/client_install.html
HPS_INSTALL_PAGE3=/home/moresec/hps_install/src/web/templates/install.html
HPS_INSTALL_PAGE4=/home/moresec/hps_install/src/web/templates/server_install.html
sed -i -e "s/幻盾//g"  ${HPS_MANAGER_DASHBOARD}
sed -i -e "s/幻盾//g"  ${HPS_MAIL_STORE}
sed -i -e "s/幻盾//g"  ${HPS_MAIL_SYNC}
sed -i -e "s/^.*moresec.cn.*$//g" ${HPS_INSTALL_PAGE1}
sed -i -e "s/^.*moresec.cn.*$//g" ${HPS_INSTALL_PAGE2}
sed -i -e "s/^.*moresec.cn.*$//g" ${HPS_INSTALL_PAGE3}
sed -i -e "s/^.*moresec.cn.*$//g" ${HPS_INSTALL_PAGE4}
mv ${HPS_MANAGER_PATH}/src/web_user/static/image/logo.png ${HPS_MANAGER_PATH}/src/web_user/static/image/logo.bak.png
cp logo.png ${HPS_MANAGER_PATH}/src/web_user/static/image/
mv /home/moresec/hps_install/src/web/static/images/logo.png /home/moresec/hps_install/src/web/static/images/log.bak.png
cp logo.png /home/moresec/hps_install/src/web/static/images/
