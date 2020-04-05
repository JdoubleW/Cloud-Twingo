########################################################################################
#Security group
########################################################################################
resource "openstack_networking_secgroup_v2" "secgroup_rancher" {
  name        = "${var.sec-group}"
  description = "Security Group for Rancher"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_3" {
  direction         = "ingress"
  ethertype         = "IPv4"
  remote_group_id   = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_4" {
  direction         = "ingress"
  ethertype         = "IPv6"
  remote_group_id   = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_5" {
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "icmp"
  remote_ip_prefix  = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_6" {
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 22
  port_range_max    = 22
  remote_ip_prefix  = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_7" {
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 80
  port_range_max    = 80
  remote_ip_prefix  = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_8" {
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 443
  port_range_max    = 443
  remote_ip_prefix  = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_9" {
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 2376
  port_range_max    = 2376
  remote_ip_prefix  = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_10" {
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 2379
  port_range_max    = 2380
  remote_ip_prefix  = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_11" {
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "udp"
  port_range_min    = 4789
  port_range_max    = 4789
  remote_ip_prefix  = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}


resource "openstack_networking_secgroup_rule_v2" "rancher_rule_12" {
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 6443
  port_range_max    = 6443
  remote_ip_prefix  = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_13" {
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "udp"
  port_range_min    = 8472
  port_range_max    = 8472
  remote_ip_prefix  = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_14" {
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 10250
  port_range_max    = 10252
  remote_ip_prefix  = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_15" {
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 10256
  port_range_max    = 10256
  remote_ip_prefix  = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_16" {
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 30000
  port_range_max    = 32767
  remote_ip_prefix  = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}

resource "openstack_networking_secgroup_rule_v2" "rancher_rule_17" {
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "udp"
  port_range_min    = 30000
  port_range_max    = 32767
  remote_ip_prefix  = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup_rancher.id}"
}