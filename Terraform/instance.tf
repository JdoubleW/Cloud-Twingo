########################################################################################
#Keypair
########################################################################################
resource "openstack_compute_keypair_v2" "tf-keypair" {
  name       = "rancher-keypair"
  public_key = "${file("./id_rsa.pub")}"
}

########################################################################################
#New flavor
########################################################################################
resource "openstack_compute_flavor_v2" "rancher-flavor" {
  name  = "${var.flavor}"
  ram   = "4096"
  vcpus = "1"
  disk  = "5"
}

########################################################################################
#New Instance
########################################################################################
resource "openstack_compute_instance_v2" "rancher" {
  name            = "Rancher"
  image_id        = "${openstack_images_image_v2.ubuntu.id}"
  flavor_id       = "${openstack_compute_flavor_v2.rancher-flavor.id}"
  security_groups = ["${var.sec-group}"]
  key_pair        = "${var.ssh_key_file}"

  network {
    uuid = "${openstack_networking_network_v2.private.id}"
  }
  block_device {
    uuid                  = "${var.image}"
    source_type           = "image"
    volume_size           = 20
    boot_index            = 0
    destination_type      = "volume"
    delete_on_termination = true
  }

}


########################################################################################
#Mount IP and perform commands in the instance
########################################################################################
resource "openstack_compute_floatingip_associate_v2" "terraform" {
  floating_ip = "${openstack_networking_floatingip_v2.fip.address}"
  instance_id = "${openstack_compute_instance_v2.rancher.id}"

  provisioner "remote-exec" {
    connection {
      host        = "${openstack_networking_floatingip_v2.fip.address}"
      user        = "${var.ssh_user_name}"
      private_key = "${file("./${var.ssh_key_file}.pem")}"
    }

    inline = [
      "sudo apt-get update"
        ]
  }
}