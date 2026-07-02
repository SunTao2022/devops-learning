resource "azurerm_public_ip" "vm_ip" {
  for_each = var.vm_configs
  name                = "${each.value.vm_name}-pip"
  location            = var.rg_location
  resource_group_name = var.rg_name
  allocation_method   = "Static"
  sku                 = "Standard"
  #   domain_name_label = "${var.vm_name}-${random_string.suffix.result}"
}

resource "azurerm_network_interface" "nic" {
  for_each = var.vm_configs
  name                = "${each.value.vm_name}-nic"
  location            = var.rg_location
  resource_group_name = var.rg_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.vm_ip[each.key].id
  }
}


resource "azurerm_linux_virtual_machine" "vm" {
  for_each = var.vm_configs
  name                  = each.value.vm_name
  resource_group_name   = var.rg_name
  location              = var.rg_location
  size                  = each.value.size
  admin_username        = var.admin_username
  network_interface_ids = [azurerm_network_interface.nic[each.key].id]

  admin_ssh_key {
    username   = var.admin_username
    public_key = file(var.ssh_public_key_path)
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "ubuntu-24_04-lts"
    sku       = "server"
    version   = "latest"
  }
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
}