output "vnet_id" {
  value = module.networking.vnet_id
}

output "subnet_id" {
  value = module.networking.subnet_id
}


output "nsg_id" {
  value = module.networking.nsg_id
}


output "vm_public_ip" {
  value = module.compute.vm_public_ips
}

output "vm_ids" {
  value = module.compute.vm_ids
}