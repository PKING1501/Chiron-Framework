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

class ArrayType:
    def __init__(self, element_type, size):
        self.element_type = element_type
        self.size = size
        self.value = f"{element_type.value}[{size}]"
        
    def __eq__(self, other):
        if not isinstance(other, ArrayType):
            return False
        return self.element_type == other.element_type and self.size == other.size
        
    def is_numeric(self):
        return False
        
    def can_promote_to(self, other):
        return False