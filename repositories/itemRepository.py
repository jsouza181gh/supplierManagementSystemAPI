from database import session
from entities.item import Item
from entities.supplier import Supplier

def createItem(
        newName : str, 
        newCategory : str,
        supplierIds : list[str] = None
    ):
    
    newItem = Item(
        name = newName,
        category = newCategory
    )

    if supplierIds is not None:
        newItem.suppliers = loadSuppliers(supplierIds)

    session.add(newItem)
    session.commit()
    return newItem

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

    if supplierIds is not None:
        item.suppliers = loadSuppliers(supplierIds)

    session.add(item)
    session.commit()
    return item

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