from .itemController import itemBlueprint
from .supplierController import supplierBlueprint
from .userController import userBlueprint
from .documentController import documentBlueprint

blueprints = [
    itemBlueprint,
    supplierBlueprint,
    userBlueprint,
    documentBlueprint
]