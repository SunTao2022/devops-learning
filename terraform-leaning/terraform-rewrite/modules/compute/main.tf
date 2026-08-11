resource "azurerm_public_ip" "vm_ip" {
  count = 1
  name = "${var.vm_base_name}-pip"
  resource_group_name = var.rg_name
  location = var.rg_location
  sku = "Standard"
  allocation_method = "Static"
}

resource "azurerm_network_interface" "vm_nic" {
  count = 1
  name = "${var.vm_base_name}-nic"
  resource_group_name = var.rg_name
  location = var.rg_location
  ip_configuration {
    name = "vm_nic_ip"
    private_ip_address_allocation = "Dynamic"
    subnet_id = var.subnet_id
    public_ip_address_id = azurerm_public_ip.vm_ip[0].id
  }
}

resource "azurerm_linux_virtual_machine" "tfvm" {
  count = 1
  lifecycle {
    prevent_destroy = true
  }
  name = var.vm_base_name
  resource_group_name = var.rg_name
  location = var.rg_location
  network_interface_ids = [azurerm_network_interface.vm_nic[0].id]
  size = var.vm_size
  os_disk {
    caching = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  admin_username = var.admin_username
  disable_password_authentication = true
  admin_ssh_key {
    public_key = file(var.ssh_key_path)
    username = var.admin_username 
    }
  source_image_reference {
    publisher = "Canonical"
    offer = "ubuntu-24_04-lts"
    sku = "server"
    version = "latest"
  }
}