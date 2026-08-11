terraform {
    required_providers {
      azurerm = {
        source = "hashicorp/azurerm"
        version = "~>4.0"
      }
    }
    backend "azurerm" {
      resource_group_name = "tfstate-rg"
      storage_account_name = "tfstatetao202607022027"
      container_name = "tfstate"
      key = "terraform-rewrite.tfstate"
    }
    
}
provider "azurerm" {
  features {
    
  }
  client_id = var.arm_client_id
  client_secret = var.arm_client_secret
  tenant_id = var.arm_tenant_id
  subscription_id = var.arm_subscription_id
}



