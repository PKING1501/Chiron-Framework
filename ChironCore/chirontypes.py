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
    
    def is_subtype_of(self, other):
        """Check if this type is a subtype of another type"""
        # UNKNOWN (like {}) can be assigned to anything (inferred from context).
        if self == other or self == Type.UNKNOWN:
            return True
        
        promotions = {
            Type.INT: [Type.FLOAT, Type.DOUBLE],
            Type.FLOAT: [Type.DOUBLE],
        }
        return other in promotions.get(self, [])

class ArrayType:
    def __init__(self, element_type, size):
        self.element_type = element_type
        self.size = size
        if isinstance(element_type, ArrayType):
            # If element_type is int[10], and size is 5, it becomes int[5][10]
            base_type_str = element_type.value.split('[')[0]
            existing_dims = element_type.value[len(base_type_str):]
            self.value = f"{base_type_str}[{size}]{existing_dims}"
        else:
            et_val = element_type.value if hasattr(element_type, 'value') else str(element_type)
            self.value = f"{et_val}[{size}]"
        
    def __eq__(self, other):
        if not isinstance(other, ArrayType):
            return False
        return self.element_type == other.element_type and self.size == other.size
        
    def is_numeric(self):
        return False
        
    def is_subtype_of(self, other):
        return self == other

class StructType:
    def __init__(self, name, fields):
        """
        :param name: Name of the struct
        :param fields: Dictionary mapping field names to their Types
        """
        self.name = name
        self.fields = fields
        # Value string representation for logging/debugging
        fields_str = ", ".join([f"{n}: {t.value if hasattr(t, 'value') else str(t)}" for n, t in fields.items()])
        self.value = f"struct {name} {{{fields_str}}}"

    def __eq__(self, other):
        if not isinstance(other, StructType):
            return False
        return self.name == other.name and self.fields == other.fields

    def is_numeric(self):
        return False

    def is_subtype_of(self, other):
        return self == other or self == Type.UNKNOWN