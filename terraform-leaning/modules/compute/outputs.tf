output "vm_public_ips" {
  value = { for k, v in azurerm_public_ip.vm_ip : k => v.ip_address }
}

output "vm_ids" {
  value = { for k, v in azurerm_linux_virtual_machine.vm : k => v.id }
}