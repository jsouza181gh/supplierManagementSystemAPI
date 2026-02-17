from repositories import itemRepository
from exceptions import NotFoundException, ConflictException, BadRequestException
from sqlalchemy.exc import IntegrityError
from uuid import UUID

def createItem(
        newName : str,
        newCategory : str = None,
        supplierIds : list[str] = None
    ):
    try:
        newItem = itemRepository.createItem(
            newName,
            newCategory,
            supplierIds
        )
    except IntegrityError:
        raise ConflictException("Item already exists")
    
    return createDTO(newItem)

def findItemById(itemId : str):
    isValidId(itemId)
    item = itemRepository.findItemById(itemId)

    if not item:
        raise NotFoundException("Item was not found")
    
    return createDTO(item)

def loadItems(
        page : int = 1,
        limit : int =10,
        search : str = None
    ):
    items, rows = itemRepository.loadItems(page, limit, search)
    if not items:
        raise NotFoundException("The items were not found")
    
    return list(map(createDTO, items)), rows

def updateItem(
        itemId : str,
        newName : str,
        newCategory : str = None,
        supplierIds : list[str] = None
    ):
    isValidId(itemId)
    try:
        item = itemRepository.updateItem(
            itemId,
            newName,
            newCategory,
            supplierIds
        )
    except IntegrityError:
        raise ConflictException("Item already exists")
    
    if not item:
        raise NotFoundException("Item was not found")
    
    return createDTO(item)

def deleteItem(itemId : str):
    isValidId(itemId)
    try:
        deleted = itemRepository.deleteItem(itemId)
    except IntegrityError:
        raise ConflictException("Item cannot be deleted because it is in use")
    
    if not deleted:
            raise NotFoundException("Item was not found")

def createDTO(item):
    return {
        "id" : str(item.id),
        "name" : item.name,
        "category" : item.category,
        "suppliers" : list(
            map(
                lambda x : {
                    "id" : str(x.id),
                    "name" : x.name,
                    "cnpj" : x.cnpj,
                    "location" : x.location,
                    "representative" : splitInfo(x.representative),
                    "phoneNumber" : splitInfo(x.phoneNumber),
                    "email" : x.email,
                    "site" : x.site,
                    "description" : x.description,
                    "isPreferred" : x.preferredSupplier
                    },
                item.suppliers
            )
        )
    }

def splitInfo(info):
    if info is None:
        return info
    else:
        return [x.strip() for x in str(info).split("/")]
    
def isValidId(id: str):
    try:
        UUID(id)
        return True
    except (ValueError, AttributeError, TypeError):
        raise BadRequestException("Invalid ID")