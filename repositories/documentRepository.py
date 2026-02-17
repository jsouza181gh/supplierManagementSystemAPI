from database import session
from entities.document import Document

def createDocument(
        name : str,
        path : str,
        category : str,
        supplierId : str
    ):
    newDocument = Document(
        name,
        path,
        category,
        supplierId
    )
    session.add(newDocument)
    session.commit()
    return newDocument

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
    document.name = name
    document.path = path
    document.category = category
    
    session.add(document)
    session.commit()
    return document

def deleteDocument(documentId : str):
    document = findDocumentById(documentId)
    session.delete(document)
    session.commit()