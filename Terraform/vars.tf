variable "image" {
  default = "2a9dfa5c-8e00-41b3-8ee8-d3f39804a50c"
}

variable "flavor" {
  default = "m1.dwarf"
}


variable "pool" {
  default = "public-Rancher"
}

variable "sec-group" {
  default = "Rancher_secgroup"
}

variable "ssh_key_file" {
  default = "ssh-rancher"
}

variable "ssh_user_name" {
  default = "ubuntu"
}

variable "volume" {
  default = "rancher-volume"
}
