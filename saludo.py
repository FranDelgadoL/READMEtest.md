{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "virtualMachines_test_ubuntu_cus_vm_name": {
            "defaultValue": "test-ubuntu-cus-vm",
            "type": "String"
        },
        "disks_test_ubuntu_cus_vm_disk1_f26af65dfdbf42629f3be42a1a0fe545_externalid": {
            "defaultValue": "/subscriptions/826d0748-8207-40ad-9e9c-44be4fa3f764/resourceGroups/learn-88f79462-179f-48da-80c4-f18cdada965b/providers/Microsoft.Compute/disks/test-ubuntu-cus-vm_disk1_f26af65dfdbf42629f3be42a1a0fe545",
            "type": "String"
        },
        "networkInterfaces_test_ubuntu_cus_v842_externalid": {
            "defaultValue": "/subscriptions/826d0748-8207-40ad-9e9c-44be4fa3f764/resourceGroups/learn-88f79462-179f-48da-80c4-f18cdada965b/providers/Microsoft.Network/networkInterfaces/test-ubuntu-cus-v842",
            "type": "String"
        }
    },
    "variables": {},
    "resources": [
        {
            "type": "Microsoft.Compute/virtualMachines",
            "apiVersion": "2022-03-01",
            "name": "[parameters('virtualMachines_test_ubuntu_cus_vm_name')]",
            "location": "brazilsouth",
            "properties": {
                "hardwareProfile": {
                    "vmSize": "Standard_D2s_v3"
                },
                "storageProfile": {
                    "imageReference": {
                        "publisher": "canonical",
                        "offer": "0001-com-ubuntu-server-focal",
                        "sku": "20_04-lts-gen2",
                        "version": "latest"
                    },
                    "osDisk": {
                        "osType": "Linux",
                        "name": "[concat(parameters('virtualMachines_test_ubuntu_cus_vm_name'), '_disk1_f26af65dfdbf42629f3be42a1a0fe545')]",
                        "createOption": "FromImage",
                        "caching": "ReadWrite",
                        "managedDisk": {
                            "storageAccountType": "Premium_LRS",
                            "id": "[parameters('disks_test_ubuntu_cus_vm_disk1_f26af65dfdbf42629f3be42a1a0fe545_externalid')]"
                        },
                        "deleteOption": "Delete",
                        "diskSizeGB": 30
                    },
                    "dataDisks": []
                },
                "osProfile": {
                    "computerName": "[parameters('virtualMachines_test_ubuntu_cus_vm_name')]",
                    "adminUsername": "azureuser",
                    "linuxConfiguration": {
                        "disablePasswordAuthentication": true,
                        "ssh": {
                            "publicKeys": [
                                {
                                    "path": "/home/azureuser/.ssh/authorized_keys",
                                    "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDGp8RU/Yal8QD0i7aapY0dXG/veWZtpGvS69BRUZ9E7snojwJsCSh7u9s4QmySZntiBQiRjisyD4a7G9ByeAZwMEtAkeIkwYilNMIatz2aZ5Hqvp8L3jS5NSevvCQHM9Y6PBybLHOiFQtQjXpPDMv8gl29esAb/S+YLXLfBKWy1+KELMtmS8BUjVMarrkxvRbyyHuES3dS1b0b58TKKFRBNSIi6Wlsu8MduRCE0rmYlD+67whMnsVhtONnAuE4w8y3dGtXHRlHCinIlanZgER6Vkh4Agr2+wQQ9WYamM3RRh3HubLOoZ669eBHpx5B+9Fmb6XKDzLJNTgxgNKjiwDYSR2E29r2trryym8aUTvEuBtohQpxtUcjbCG5HrGnPMgfOZM+F/FhcMs4GqLUgrwOuChMSfHWix29NPz8wsvmHt3jAKc4F8y4sePh63DG9dfsQGHj5C1w4wC4boTIlVcNPsFc3EyX/hT4Mm4Wew1wnmvj7xSQFzpaxg7jx85Dep0= generated-by-azure"
                                }
                            ]
                        },
                        "provisionVMAgent": true,
                        "patchSettings": {
                            "patchMode": "ImageDefault",
                            "assessmentMode": "ImageDefault"
                        }
                    },
                    "secrets": [],
                    "allowExtensionOperations": true,
                    "requireGuestProvisionSignal": true
                },
                "networkProfile": {
                    "networkInterfaces": [
                        {
                            "id": "[parameters('networkInterfaces_test_ubuntu_cus_v842_externalid')]",
                            "properties": {
                                "deleteOption": "Detach"
                            }
                        }
                    ]
                },
                "diagnosticsProfile": {
                    "bootDiagnostics": {
                        "enabled": true
                    }
                }
            }
        }
    ]
}
    


