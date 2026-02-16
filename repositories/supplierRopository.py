from database import session
from entities.item import Item
from entities.supplier import Supplier
from sqlalchemy import select, func

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
    newSupplier = Supplier(
        name = newName,
        cnpj = newCnpj,
        location = newLocation,
        representative = newRepresentative,
        phoneNumber = newPhoneNumber,
        email = newEmail,
        site = newSite,
        description = newDescription
    )

    if itemIds:
        newSupplier.items = loadItems(itemIds)

    session.add(newSupplier)
    session.commit()
    return newSupplier

def findSupplierById(supplierId : str):
    supplier = (
        session
        .query(Supplier)
        .filter_by(id=supplierId)
        .first()
    )
    return supplier

def loadSuppliers(
        page : int =1,
        limit : int = 10
        ):
    offset = (page - 1) * limit
    rowsCount = (
        session
        .execute(
            select(func.count())
            .select_from(Supplier)
            )
            .scalar()
        )

    suppliers = (
        session
        .execute(
            select(Supplier)
            .order_by(
                Supplier.preferredSupplier.desc(),
                Supplier.name.asc()
            )
            .offset(offset)
            .limit(limit)
        )
        .scalars()
        .all()
    )
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
        isPreferred : bool,
        itemIds : list[str] = None
    ):
    
    supplier = findSupplierById(supplierId)
    supplier.name = newName
    supplier.cnpj = newCnpj
    supplier.location = newLocation
    supplier.representative = newRepresentative
    supplier.phoneNumber = newPhoneNumber
    supplier.email = newEmail
    supplier.site = newSite
    supplier.description = newDescription
    supplier.preferredSupplier = isPreferred

    if itemIds:
        supplier.items = loadItems(itemIds)

    session.add(supplier)
    session.commit()
    return supplier

def deleteSupplier(supplierId : str):
    supplier = findSupplierById(supplierId)
    session.delete(supplier)
    session.commit()

def loadItems(itemIds : list[str]):
    return (
        session
        .query(Item)
        .filter(Item.id.in_(itemIds))
        .all()
    )