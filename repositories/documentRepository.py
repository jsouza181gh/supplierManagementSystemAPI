from database import session
from entities.document import Document
from repositories.supplierRopository import findSupplierById
from exceptions import NotFoundException

def createDocument(
        name : str,
        path : str,
        category : str,
        supplierId : str
    ):
    if not findSupplierById(supplierId):
        raise NotFoundException("No matches to supplier ID")
    
    newDocument = Document(
        name,
        path,
        category,
        supplierId
    )
    try:
        session.add(newDocument)
        session.commit()
        return newDocument
    except:
        session.rollback()
        raise

def findDocumentById(documentId : str):
    document = (
        session
        .query(Document)
        .filter_by(id=documentId)
        .first()
    )
    return document

def loadSupplierDocuments(supplierId : str):
    documents = (
        session
        .query(Document)
        .filter(Document.supplierId == supplierId)
        .all()
    )
    return documents

def updateDocument(
        documentId : str,
        name : str,
        path : str,
        category : str
    ):
    document = findDocumentById(documentId)

    if not document:
        return None
        
    document.name = name
    document.path = path
    document.category = category
    try:    
        session.add(document)
        session.commit()
        return document
    except:
        session.rollback()
        raise

def deleteDocument(documentId : str):
    document = findDocumentById(documentId)

    if not document:
        return False
    
    try:    
        session.delete(document)
        session.commit()
        return True
    except:
        session.rollback()
        raise