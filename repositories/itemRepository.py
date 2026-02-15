from database import session
from entities.item import Item
from entities.supplier import Supplier

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
        newCategory : str,
        supplierIds : list[str] = None
        ):
    
    item = findItemById(itemId)
    item.name = newName
    item.category = newCategory

    if supplierIds:
        item.suppliers = loadSuppliers(supplierIds)

    session.add(item)
    session.commit()

def deleteItem(itemId : str):
    item = findItemById(itemId)
    session.delete(item)
    session.commit()

def loadSuppliers(supplierIds : list[str]):
    return (
        session
        .query(Supplier)
        .filter(Supplier.id.in_(supplierIds))
        .all()
    )