resource "azurerm_resource_group" "rg" {
  name     = "terraform-leaning-rg"
  location = "Canada Central"
}




module "networking" {
  source = "./modules/networking"

  vnet_name     = var.vnet_name
  address_space = var.address_space
  nsg_name      = var.nsg_name
  ssh_port      = var.ssh_port
  rg_name       = azurerm_resource_group.rg.name
  rg_location   = azurerm_resource_group.rg.location
}


module "compute" {
  source = "./modules/compute"


  vm_basename         = var.vm_basename
  vm_count            = var.vm_count
  rg_name             = azurerm_resource_group.rg.name
  rg_location         = azurerm_resource_group.rg.location
  subnet_id           = module.networking.subnet_id
  ssh_public_key_path = var.ssh_public_key_path
  admin_username      = var.admin_username
}