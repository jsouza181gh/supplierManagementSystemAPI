from repositories import documentRepository

def createDocument(
        name : str,
        path : str,
        category : str,
        supplierId : str    
    ):

    newDocument = documentRepository.createDocument(
        name,
        path,
        category,
        supplierId
    )
    return createDTO(newDocument)

def findDocumentById(documentId : str):
    document = documentRepository.findDocumentById(documentId)
    return createDTO(document)

def loadSupplierDocuments(supplierId : str):
    documents = documentRepository.loadSupplierDocuments(supplierId)
    return list(map(createDTO, documents))

def updateDocument(
        documentId : str,
        name : str,
        path : str,
        category : str
    ):
    document = documentRepository.updateDocument(
        documentId,
        name,
        path,
        category
    )
    return createDTO(document)

def deleteDocument(documentId : str):
    documentRepository.deleteDocument(documentId)

def createDTO(document):
    return {
        "id" : str(document.id),
        "name" : document.name,
        "path" : document.path,
        "category" : document.category,
        "created_at" : document.createdAt.isoformat()
    }