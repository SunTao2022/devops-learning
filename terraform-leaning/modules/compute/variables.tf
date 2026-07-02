



variable "vm_basename" {

}

variable "vm_count" {

}

variable "rg_name" {}

variable "rg_location" {}


variable "ssh_public_key_path" {

}


variable "admin_username" {

}

variable "subnet_id" {}


variable "vm_configs" {
  default = {
    "vm_0" = {
        vm_name = "terraform-vm-0"
        size = "Standard_B2ts_v2"
    }
    "vm_1" = {
        vm_name = "terraform-vm-1"
        size = "Standard_B2ts_v2"
    }
  }
}