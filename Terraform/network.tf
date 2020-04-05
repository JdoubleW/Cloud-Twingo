############################################
#Public network
############################################
resource "openstack_networking_network_v2" "public" {
  name                    = "${var.pool}"
  admin_state_up          = true
  shared                  = true
  external                = true
  availability_zone_hints = ["nova"]
  segments {
    physical_network = "extnet"
    network_type     = "flat"
  }
}
########################################################################################
#Public network subnet
########################################################################################
resource "openstack_networking_subnetpool_v2" "public-subnet-pool" {
  name     = "public-subnet-pool-Rancher"
  prefixes = ["192.168.37.0/24"]
}

resource "openstack_networking_subnet_v2" "public-subnet" {
  name       = "public-subnet-Rancher"
  network_id = "${openstack_networking_network_v2.public.id}"
  cidr       = "192.168.37.0/24"
  allocation_pool {
    start = "192.168.37.50"
    end   = "192.168.37.70"
  }
  ip_version      = 4
  gateway_ip      = "192.168.37.2"
  enable_dhcp     = "false"
  dns_nameservers = ["8.8.8.8"]
}
########################################################################################
#Private network
########################################################################################
resource "openstack_networking_network_v2" "private" {
  name           = "private-Rancher"
  admin_state_up = "true"
}

########################################################################################
#Private network subnet
########################################################################################
resource "openstack_networking_subnetpool_v2" "private-subnet-pool" {
  name     = "private-subnet-pool-Rancher"
  prefixes = ["10.2.0.0/24"]
}

resource "openstack_networking_subnet_v2" "private-subnet" {
  name       = "private-subnet-Rancher"
  network_id = "${openstack_networking_network_v2.private.id}"
  cidr       = "10.2.0.0/24"
  ip_version = 4
  allocation_pool {
    start = "10.2.0.10"
    end   = "10.2.0.30"
  }
  gateway_ip      = "10.2.0.1"
  enable_dhcp     = "true"
  dns_nameservers = ["8.8.8.8"]
}


########################################################################################
#Router
########################################################################################
resource "openstack_networking_router_v2" "router1" {
  name                = "Rancher-Router1"
  admin_state_up      = true
  external_network_id = "${openstack_networking_network_v2.public.id}"
}

########################################################################################
#Router interfaces
########################################################################################
resource "openstack_networking_router_interface_v2" "router-interface-1" {
  router_id = "${openstack_networking_router_v2.router1.id}"
  subnet_id = "${openstack_networking_subnet_v2.private-subnet.id}"
}

########################################################################################
#Floating IP
########################################################################################
resource "openstack_networking_floatingip_v2" "fip" {
  pool = "${openstack_networking_network_v2.public.name}"
}

