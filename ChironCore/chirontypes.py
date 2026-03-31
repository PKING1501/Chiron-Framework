from enum import Enum

class Type(Enum):
    INT = "int"
    FLOAT = "float"
    DOUBLE = "double"
    STRING = "string"
    BOOLEAN = "boolean"
    UNKNOWN = "unknown"
    # ERROR = "error"
    TYPE_ERROR = "type_error"
    VOID = "void"
    
    def is_numeric(self):
        return self in [Type.INT, Type.FLOAT, Type.DOUBLE]
    
    def can_promote_to(self, other):
        """Check if this type can be promoted to another type"""
        promotions = {
            Type.INT: [Type.FLOAT, Type.DOUBLE],
            Type.FLOAT: [Type.DOUBLE],
        }
        return other in promotions.get(self, [])