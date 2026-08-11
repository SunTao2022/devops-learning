variable "rg_name" {
  type = string
}

variable "rg_location" {
  type = string
}

variable "address_space" {
  type = list(string)
}

variable "vnet_name" {
  type = string
}

variable "subnet_name" {
  type = string
}

variable "nsg_name" {
  type = string
}

variable "ssh_ports" {
  type = list(number)
}


