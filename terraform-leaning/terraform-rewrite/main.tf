resource "azurerm_resource_group" "tf_rg" {
  name = var.rg_name
  location = var.rg_location
}

module "networking" {
  source = "./modules/networking"
  ssh_ports = var.ssh_ports
  vnet_name = var.vnet_name
  rg_name = var.rg_name
  rg_location = var.rg_location
  subnet_name = var.subnet_name
  nsg_name = var.nsg_name
  address_space = var.address_space
}

module "compute" {
  source = "./modules/compute"
  rg_name = var.rg_name
  rg_location = var.rg_location
  ssh_key_path = var.ssh_public_key_path
  subnet_id = module.networking.subnet_id
  vm_base_name = var.vm_base_name
}