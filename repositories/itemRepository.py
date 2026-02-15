from entities.item import Item
from database import session

def createItem(
        newName : str, 
        newCategory : str
        ):
    
    newItem = Item(
        name = newName,
        category = newCategory
    )
    session.add(newItem)
    session.commit()

def findItemById(itemId : str):
    item = (
        session
        .query(Item)
        .filter_by(id=itemId)
        .first()
        )
    return item

def updateItem(
        itemId : str, 
        newName : str, 
        newCategory : str
        ):
    
    item = findItemById(itemId)
    item.name = newName
    item.category = newCategory
    session.add(item)
    session.commit()

def deleteItem(itemId : str):
    item = findItemById(itemId)
    session.delete(item)
    session.commit()