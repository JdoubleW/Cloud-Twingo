########################################################################################
#Rancher Image
########################################################################################
resource "openstack_images_image_v2" "rancheros" {
  name             = "RancherOS"
  image_source_url = "https://releases.rancher.com/os/latest/rancheros-openstack.img"
  container_format = "bare"
  disk_format      = "qcow2"
  visibility       = "public"

  properties = {
    key = "value"
  }
}


########################################################################################
#Ubuntu Image
########################################################################################
#resource "openstack_images_image_v2" "ubuntu" {
#  name             = "Ubuntu"
#  image_source_url = "https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64.img"
#  container_format = "bare"
#  disk_format      = "qcow2"
#  visibility       = "public"
#}