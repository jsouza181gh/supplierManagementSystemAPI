from repositories import documentRepository
from exceptions import NotFoundException, ConflictException, BadRequestException
from sqlalchemy.exc import IntegrityError
from uuid import UUID

def createDocument(
        name : str,
        path : str,
        category : str,
        supplierId : str    
    ):
    try:
        newDocument = documentRepository.createDocument(
            name,
            path,
            category,
            supplierId
        )
    except IntegrityError:
        raise ConflictException("Document already exists")

    return createDTO(newDocument)

def findDocumentById(documentId : str):
    isValidId(documentId)
    document = documentRepository.findDocumentById(documentId)

    if not document:
        raise NotFoundException("Document was not found")

    return createDTO(document)

def loadSupplierDocuments(supplierId : str):
    documents = documentRepository.loadSupplierDocuments(supplierId)

    if not documents:
        raise NotFoundException("The documents were not found")
    
    return list(map(createDTO, documents))

def updateDocument(
        documentId : str,
        name : str,
        path : str,
        category : str
    ):
    isValidId(documentId)
    try:
        document = documentRepository.updateDocument(
            documentId,
            name,
            path,
            category
        )
    except IntegrityError:
        raise ConflictException("Document already exists")
    
    if not document:
        raise NotFoundException("Document was not found")
    
    return createDTO(document)

def deleteDocument(documentId : str):
    isValidId(documentId)
    try:
        deleted = documentRepository.deleteDocument(documentId)
    except IntegrityError:
        raise ConflictException("Document cannot be deleted because it is in use")
    
    if not deleted:
            raise NotFoundException("Document was not found")

def createDTO(document):
    return {
        "id" : str(document.id),
        "name" : document.name,
        "path" : document.path,
        "category" : document.category,
        "created_at" : document.createdAt.isoformat()
    }

def isValidId(id: str):
    try:
        UUID(id)
        return True
    except (ValueError, AttributeError, TypeError):
        raise BadRequestException("Invalid ID")