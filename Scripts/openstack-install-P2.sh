packstack --allinone --os-neutron-ovs-bridge-mappings=extnet:br-ex\
--os-neutron-ovs-bridge-interfaces=br-ex:ens33 --os-neutron-ml2-type-drivers=vxlan,flat

sudo cat > /etc/sysconfig/network-scripts/ifcfg-br-ex << EOF2
DEVICE=br-ex 
DEVICETYPE=ovs 
TYPE=OVSBridge 
BOOTPROTO=static 
IPADDR=192.168.37.100 
NETMASK=255.255.255.0 
GATEWAY=192.168.37.2 
DNS1=8.8.8.8 
ONBOOT=yes 
EOF2

cat > /etc/sysconfig/network-scripts/ifcfg-ens33 << EOF2
NAME=ens33 
DEVICE=ens33 
ONBOOT=yes 
IPV6INIT=no 
DEVICETYPE=ovs 
TYPE=OVSPort 
OVS_BRIDGE=br-ex 
EOF2
reboot