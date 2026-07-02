variable "admin_username" {
  default = "azureuser"
}


variable "ssh_public_key_path" {
  default = "/home/tao/.ssh/id_ed25519.pub"
}

variable "vm_basename" {
  default = "terraform-vm"
}

variable "vm_count" {
  default = 2
}

variable "vnet_name" {
  default = "terraform-vnet"
}

variable "address_space" {
  default = ["10.0.0.0/16"]
}

variable "nsg_name" {
  default = "terraform-nsg"
}

variable "ssh_port" {
  type    = list(number)
  default = [22 , 2222]
}

























# variable "vm_configs" {
#   description = "VM configurations with different sizes"
#   type = map(object({
#     vm_name = string
#     vm_size = string
#   }
#   )
#   )
#   default = {
#     "vm_0" = {
#       vm_name = "terraform-vm-0"
#       vm_size = "Standard_B2ts_v2"
#     }
#     "vm_1" = {
#       vm_name = "terraform-vm-1"
#       vm_size = "Standard_B2ts_v2"
#     }
#   }
# }


