from repositories import supplierRopository
from exceptions import NotFoundException, ConflictException, BadRequestException
from sqlalchemy.exc import IntegrityError
from uuid import UUID

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
    try:
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
    except IntegrityError:
        raise ConflictException("Supplier already exists")

    return createDTO(newSupplier)

def findSupplierById(supplierId : str):
    isValidId(supplierId)
    supplier = supplierRopository.findSupplierById(supplierId)

    if not supplier:
        raise NotFoundException("Supplier was not found")
    
    return createDTO(supplier)

def loadSuppliers(
        page : int = 1,
        limit : int =10
    ):
    suppliers, rowsCount = supplierRopository.loadSuppliers(page, limit)
    if not suppliers:
        raise NotFoundException("The suppliers were not found")

    suppliers = list(map(createDTO, suppliers))
    return suppliers, rowsCount

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
    isValidId(supplierId)
    try:
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
    except IntegrityError:
        raise ConflictException("Supplier already exists")

    if not supplier:
        raise NotFoundException("Supplier was not found")
    
    return createDTO(supplier)

def deleteSupplier(supplierId : str):
    isValidId(supplierId)
    try:
        deleted = supplierRopository.deleteSupplier(supplierId)
    except IntegrityError:
        raise ConflictException("Supplier cannot be deleted because it is in use")
    
    if not deleted:
            raise NotFoundException("Supplier was not found")
    
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

def isValidId(id: str):
    try:
        UUID(id)
        return True
    except (ValueError, AttributeError, TypeError):
        raise BadRequestException("Invalid ID")