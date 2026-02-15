from repositories import itemRepository

def createItem(
        newName : str,
        newCategory : str,
        supplierIds : list[str] = None
    ):
    
    newItem = itemRepository.createItem(
        newName,
        newCategory,
        supplierIds
    )
    return newItem

def findItemById(itemId : str):
    item = itemRepository.findItemById(itemId)
    return item

def updateItem(
        itemId : str,
        newName : str,
        newCategory : str,
        supplierIds : list[str]
    ):
    
    item = itemRepository.updateItem(
        itemId,
        newName,
        newCategory,
        supplierIds
    )
    return item

def deleteItem(itemId):
    itemRepository.deleteItem(itemId)