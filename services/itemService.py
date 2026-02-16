from repositories import itemRepository

def createItem(
        newName : str,
        newCategory : str = None,
        supplierIds : list[str] = None
    ):
    
    newItem = itemRepository.createItem(
        newName,
        newCategory,
        supplierIds
    )
    return createDTO(newItem)

def findItemById(itemId : str):
    item = itemRepository.findItemById(itemId)
    return createDTO(item)

def updateItem(
        itemId : str,
        newName : str,
        newCategory : str = None,
        supplierIds : list[str] = None
    ):
    
    item = itemRepository.updateItem(
        itemId,
        newName,
        newCategory,
        supplierIds
    )
    return createDTO(item)

def deleteItem(itemId : str):
    itemRepository.deleteItem(itemId)

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