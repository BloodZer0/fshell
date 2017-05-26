generate_linux_pool(){
	for ((var=0; var< 9; var++))
	do
		virsh destroy  vm${var}
		virsh undefine vm${var}
		if [ -f "/home/vm/vm${var}.img" ];
		then
			rm -rf  /home/vm/vm${var}.img
		fi
		virt-clone -o tmpl_cent7 -n vm${var} -f /home/vm/vm${var}.img
		if [ $? != 0 ]; then
			return 1
		fi
		sed -i "s/domain-tmpl_cent7/domain-vm${var}/" /etc/libvirt/qemu/vm${var}.xml
		if [ $? != 0 ]; then
			return 1
		fi
		service libvirtd restart
	done
}

generate_linux_pool;
