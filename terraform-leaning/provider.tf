terraform {
  backend "azurerm" {
    resource_group_name = "tfstate-rg"
    storage_account_name = "tfstatetao202607022027"
    container_name = "tfstate"
    key = "terraform-leaning.tfstate"
  }
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>4.0"
    }
  }
}



provider "azurerm" {
  features {}
  subscription_id = "2061430f-368d-46f8-8bb4-0c416da8e0ad"
}


