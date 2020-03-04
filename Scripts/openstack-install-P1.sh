sudo cat > /etc/selinux/config << EOF2
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=permissive
# SELINUXTYPE= can take one of three values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are pr$
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted
EOF2

yum update -y
yum install -y nano telnet tcpdump
hostnamectl set-hostname packstack.openstack.local
sudo cat > /etc/hosts << EOF2
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4 packstack 
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6 packstack 
192.168.37.100 packstack packstack.openstack.local 
192.168.37.101 compute compute.openstack.local
EOF2
systemctl disable firewalld
systemctl stop firewalld
systemctl disable NetworkManager
systemctl stop NetworkManager
systemctl enable network
systemctl start network 

sudo cat > /etc/sysconfig/network-scripts/ifcfg-ens33 << EOF2
NAME=ens33 
DEVICE=ens33 
TYPE=Ethernet 
BOOTPROTO=none 
DEFROUTE=yes 
ONBOOT=yes 
IPADDR=192.168.37.100 
PREFIX=24 
DNS1=8.8.8.8 
GATEWAY=192.168.37.2
EOF2
systemctl restart network

yum install -y centos-release-openstack-rocky
yum update -y
yum install -y openstack-packstack

reboot
