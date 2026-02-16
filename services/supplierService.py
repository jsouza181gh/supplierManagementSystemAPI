from repositories import supplierRopository

def createSupplier(
        newName : str,
        newCnpj : str,
        newLocation : str,
        newRepresentative : str,
        newPhoneNumber : str,
        newEmail : str,
        newSite : str,
        newDescription : str,
        itemIds : list[str] = None
    ):
    
    newSupplier = supplierRopository.createSupplier(
        newName, 
        newCnpj, 
        newLocation, 
        newRepresentative, 
        newPhoneNumber, 
        newEmail, 
        newSite, 
        newDescription,
        itemIds
    )
    return createDTO(newSupplier)

def findSupplierById(supplierId : str):
    supplier = supplierRopository.findSupplierById(supplierId)
    return createDTO(supplier)

def updateSupplier(
        supplierId : str,
        newName : str,
        newCnpj : str,
        newLocation : str,
        newRepresentative : str,
        newPhoneNumber : str,
        newEmail : str,
        newSite : str,
        newDescription : str,
        itemIds: list[str],
        isPreferred : bool
    ):
    
    supplier = supplierRopository.updateSupplier(
        supplierId,
        newName,
        newCnpj,
        newLocation,
        newRepresentative,
        newPhoneNumber,
        newEmail,
        newSite,
        newDescription,
        isPreferred,
        itemIds
    )
    return createDTO(supplier)

def deleteSupplier(supplierId : str):
    supplierRopository.deleteSupplier(supplierId)

def createDTO(supplier):
    return {
        "id" : str(supplier.id),
        "name" : supplier.name,
        "cnpj" : supplier.cnpj,
        "location" : supplier.location,
        "representative" : supplier.representative,
        "phoneNumber" : supplier.phoneNumber,
        "email" : supplier.email,
        "site" : supplier.site,
        "description" : supplier.description,
        "isPreferred" : supplier.preferredSupplier,
        "items" : list(
            map(
                lambda x : {
                    "id" : str(x.id), 
                    "item" : x.name,
                    "category" : x.category
                },
                supplier.items
            )
        )
    }