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
    return newSupplier

def findSupplierById(supplierId : str):
    supplier = supplierRopository.findSupplierById(supplierId)
    return supplier

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
    return supplier

def deleteSupplier(supplierId : str):
    supplierRopository.deleteSupplier(supplierId)