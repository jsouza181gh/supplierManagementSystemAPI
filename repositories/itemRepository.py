from database import session
from entities.item import Item
from entities.supplier import Supplier
from sqlalchemy import select, func, or_, and_

def createItem(
        newName : str, 
        newCategory : str,
        supplierIds : list[str] = None
    ):
    newItem = Item(
        name = newName,
        category = newCategory
    )
    if supplierIds:
        newItem.suppliers = loadSuppliers(supplierIds)

    try:
        session.add(newItem)
        session.commit()
        return newItem
    except:
        session.rollback()
        raise

def findItemById(itemId : str):
    item = (
        session
        .query(Item)
        .filter_by(id=itemId)
        .first()
    )
    return item

def loadItems(
        page : int =1,
        limit : int = 10,
        search : str = None
    ):
    conditions = []
    baseQuery = select(Item)
    offset = (page - 1) * limit

    if search:
        terms = search.lower().split()
        for term in terms:
            conditions.append(
                or_(
                    Item.name.ilike(f"%{term}%"),
                    Item.category.ilike(f"%{term}%")
                )
            )
        baseQuery = baseQuery.where(and_(*conditions))

    rowsCount = (
        session 
        .execute(
            select(func.count()) 
            .select_from(baseQuery.subquery())
        )
        .scalar() 
    )
    query = (
        baseQuery
        .order_by(Item.name)
        .offset(offset)
        .limit(limit)
    )

    items = (
        session
        .execute(query)
        .scalars()
        .all()
    )    
    return items, rowsCount

def updateItem(
        itemId : str, 
        newName : str, 
        newCategory : str,
        supplierIds : list[str] = None
    ):
    item = findItemById(itemId)

    if not item:
        return None

    item.name = newName
    item.category = newCategory

    if supplierIds is not None:
        item.suppliers = loadSuppliers(supplierIds)

    try:
        session.add(item)
        session.commit()
        return item
    except:
        session.rollback()
        raise

def deleteItem(itemId : str):
    item = findItemById(itemId)

    if not item:
        return False

    try:
        session.delete(item)
        session.commit()
        return True
    except:
        session.rollback()
        raise

def loadSuppliers(supplierIds : list[str]):
    return (
        session
        .query(Supplier)
        .filter(Supplier.id.in_(supplierIds))
        .all()
    )