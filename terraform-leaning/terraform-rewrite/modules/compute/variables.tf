variable "rg_name" {
  type = string
}

variable "rg_location" {
  type = string
}

variable "subnet_id" {
  type = string
}

variable "vm_base_name" {
    type = string
  default = "tfvm"
}

variable "vm_size" {
    type = string
  default = "Standard_B2ts_v2"
}

variable "admin_username" {
  type = string
  default = "azureuser"
}

variable "ssh_key_path" {
  type = string
}



