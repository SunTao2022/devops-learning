resource "azurerm_virtual_network" "vnet" {
  name                = var.vnet_name
  address_space       = var.address_space
  resource_group_name = var.rg_name
  location            = var.rg_location

}

resource "azurerm_subnet" "subnet" {
  name                 = var.subnet_name
  resource_group_name  = var.rg_name
  virtual_network_name = var.vnet_name
  address_prefixes     = ["10.0.1.0/24"]

}

resource "azurerm_network_security_group" "nsg" {
  name                = var.nsg_name
  resource_group_name = var.rg_name
  location            = var.rg_location
  dynamic "security_rule" {
    for_each = var.ssh_ports
    content {
      priority                   = 100 + security_rule.key
      protocol                   = "Tcp"
      direction                  = "Inbound"
      name                       = "ssh_allow_${security_rule.value}"
      access                     = "Allow"
      source_port_range          = "*"
      destination_port_range     = tostring(security_rule.value)
      source_address_prefix      = "*"
      destination_address_prefix = "*"
    }

  }
}


resource "azurerm_subnet_network_security_group_association" "nsg_assoc" {
  network_security_group_id = azurerm_network_security_group.nsg.id
  subnet_id                 = azurerm_subnet.subnet.id
}