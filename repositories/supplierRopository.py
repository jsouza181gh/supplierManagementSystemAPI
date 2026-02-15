from database import session
from entities.supplier import Supplier
from entities.item import Item

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