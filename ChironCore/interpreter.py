
from ChironAST import ChironAST
from ChironHooks import Chironhooks
from chirontypes import Type, ArrayType, StructType
import turtle
import copy

Release="Chiron v5.3"

def addContext(node):
    if isinstance(node, str):
        return node.strip().replace(":", "self.prg.")
    return node

class Interpreter:
    # Turtle program should not contain variable with names "ir", "pc", "t_screen"
    ir = None
    pc = None
    t_screen = None
    trtl = None

    def __init__(self, irHandler, params):
        self.ir = irHandler.ir
        self.cfg = irHandler.cfg
        self.pc = 0
        self.t_screen = turtle.getscreen()
        self.trtl = turtle.Turtle()
        self.trtl.shape("turtle")
        self.trtl.color("blue", "yellow")
        self.trtl.fillcolor("green")
        self.trtl.begin_fill()
        self.trtl.pensize(4)
        self.trtl.speed(1) # TODO: Make it user friendly

        if params is not None:
            self.args = params
        else:
            self.args = None

        turtle.title(Release)
        turtle.bgcolor("white")
        turtle.hideturtle()

    def handleAssignment(self, stmt,tgt):
        raise NotImplementedError('Assignments are not handled!')

    def handleCondition(self, stmt, tgt):
        raise NotImplementedError('Conditions are not handled!')

    def handleMove(self, stmt, tgt):
        raise NotImplementedError('Moves are not handled!')

    def handlePen(self, stmt, tgt):
        raise NotImplementedError('Pens are not handled!')

    def handleGotoCommand(self, stmt, tgt):
        raise NotImplementedError('Gotos are not handled!')

    def handleNoOpCommand(self, stmt, tgt):
        raise NotImplementedError('No-Ops are not handled!')

    def handlePauseCommand(self, stmt, tgt):
        raise NotImplementedError('No-Ops are not handled!')

    def sanityCheck(self, irInstr):
        stmt, tgt = irInstr
        # if not a condition command, rel. jump can't be anything but 1
        if not isinstance(stmt, ChironAST.ConditionCommand):
            if tgt != 1:
                raise ValueError("Improper relative jump for non-conditional instruction", str(stmt), tgt)
    
    def interpret(self):
        pass

    def initProgramContext(self, params):
        pass

class ProgramContext:
    pass

# TODO: move to a different file
class ConcreteInterpreter(Interpreter):
    # Ref: https://realpython.com/beginners-guide-python-turtle
    cond_eval = None # used as a temporary variable within the embedded program interpreter
    prg = None

    def __init__(self, irHandler, params):
        super().__init__(irHandler, params)
        self.prg = ProgramContext()
        # Hooks Object:
        if self.args is not None and self.args.hooks:
            self.chironhook = Chironhooks.ConcreteChironHooks()
        self.pc = 0
        self.structs = {}

    # helper for SoA flattening in expressions
    def is_struct_based(self, t):
        from chirontypes import StructType, ArrayType
        if isinstance(t, str) and t in self.structs:
            t = self.structs[t]
        if isinstance(t, StructType):
            return True
        if isinstance(t, ArrayType):
            return self.is_struct_based(t.element_type)
        return False

    def resolve(self, e):
        # Returns (flattened_name_segment, indices_str)
        if isinstance(e, ChironAST.FieldAccess):
            name, indices = self.resolve(e.obj_expr)
            return f"{name}__{e.field_name}", indices
        elif isinstance(e, ChironAST.ArrayAccess):
            name, indices = self.resolve(e.avar)
            new_indices = "".join([f"[{self.flatten_expr(i)}]" for i in e.indices])
            return name, indices + new_indices
        elif isinstance(e, ChironAST.Var):
            prefix = "__st_" if self.is_struct_based(e.type) else ""
            name = prefix + e.varname.replace(":", "")
            return name, ""
        else:
            return str(e).replace(":", "self.prg."), ""

    def flatten_expr(self, expr):
        if isinstance(expr, (ChironAST.FieldAccess, ChironAST.ArrayAccess, ChironAST.Var)):
            name, indices = self.resolve(expr)
            if name.startswith("self.prg."):
                return f"{name}{indices}"
            return f"self.prg.{name}{indices}"
        elif isinstance(expr, ChironAST.BinArithOp):
            return f"({self.flatten_expr(expr.lexpr)} {expr.symbol} {self.flatten_expr(expr.rexpr)})"
        elif isinstance(expr, ChironAST.UnaryArithOp):
            return f"{expr.symbol}{self.flatten_expr(expr.expr)}"
        elif isinstance(expr, ChironAST.BinCondOp):
            return f"({self.flatten_expr(expr.lexpr)} {expr.symbol} {self.flatten_expr(expr.rexpr)})"
        elif isinstance(expr, ChironAST.NOT):
            return f"(not {self.flatten_expr(expr.expr)})"
        elif hasattr(expr, "val"): # Literals
            return str(expr)
        elif isinstance(expr, ChironAST.PenStatus):
            return "self.trtl.isdown()"
        else:
            return str(expr).replace(":", "self.prg.")

    def allocate_soa(self, prefix, t, current_dims):
        # Resolve string type to StructType if possible
        if isinstance(t, str) and t in self.structs:
            t = self.structs[t]
            
        from chirontypes import ArrayType, StructType
        namespace = {"self": self, "int": int, "float": float, "str": str}

        if isinstance(t, ArrayType):
            # Combine dimensions
            self.allocate_soa(prefix, t.element_type, current_dims + [t.size])
        elif isinstance(t, StructType):
            for f_name, f_type in t.fields.items():
                print(f"    Allocating field {prefix}__{f_name} of type {f_type}")
                self.allocate_soa(f"{prefix}__{f_name}", f_type, current_dims)
        else:
            # Leaf primitive: allocate multi-dim array or scalar
            if not current_dims:
                code = f"self.prg.{prefix} = None"
            else:
                # Helper to create multi-dim structure
                def create_primitive_list(dims):
                    if len(dims) == 1:
                        return f"[None] * ({dims[0]})"
                    else:
                        return f"[{create_primitive_list(dims[1:])} for _ in range({dims[0]})]"
                
                alloc_expr = create_primitive_list(current_dims)
                code = f"self.prg.{prefix} = {alloc_expr}"
            
            print(f"    Allocating leaf field {prefix}: {code}")
            exec(code, namespace, namespace)

    def _assign_struct_literal(self, lhs_prefix, st_type, lit_node, lhs_idx):
        from chirontypes import StructType
        if isinstance(st_type, str) and st_type in self.structs:
            st_type = self.structs[st_type]
            
        for (f_name, f_type), val_expr in zip(st_type.fields.items(), lit_node.values):
            if isinstance(val_expr, ChironAST.StructLiteral):
                self._assign_struct_literal(f"{lhs_prefix}__{f_name}", f_type, val_expr, lhs_idx)
            elif self.is_struct_based(f_type):
                rhs_p, rhs_i = self.resolve(val_expr)
                self.perform_assign(f"{lhs_prefix}__{f_name}", rhs_p, f_type, lhs_idx, rhs_i)
            else:
                rhs_val = self.flatten_expr(val_expr)
                namespace = {"self": self, "int": int, "float": float, "str": str, "bool": bool, "copy": copy}
                exec(f"self.prg.{lhs_prefix}__{f_name}{lhs_idx} = {rhs_val}", namespace, namespace)

    def interpret(self):
        print("Program counter : ", self.pc)
        stmt, tgt = self.ir[self.pc]
        print(stmt, stmt.__class__.__name__, tgt)

        self.sanityCheck(self.ir[self.pc])

        if isinstance(stmt, ChironAST.AssignmentCommand):
            ntgt = self.handleAssignment(stmt, tgt)
        elif isinstance(stmt, ChironAST.ArrayAllocation):
            ntgt = self.handleArrayAllocation(stmt, tgt)
        elif isinstance(stmt, ChironAST.ArrayAssignmentCommand):
            ntgt = self.handleArrayAssignment(stmt, tgt)
        elif isinstance(stmt, ChironAST.ConditionCommand):
            ntgt = self.handleCondition(stmt, tgt)
        elif isinstance(stmt, ChironAST.MoveCommand):
            ntgt = self.handleMove(stmt, tgt)
        elif isinstance(stmt, ChironAST.PenCommand):
            ntgt = self.handlePen(stmt, tgt)
        elif isinstance(stmt, ChironAST.GotoCommand):
            ntgt = self.handleGotoCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.NoOpCommand):
            ntgt = self.handleNoOpCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.StructDefinition):
            ntgt = self.handleStructDefinition(stmt, tgt)
        elif isinstance(stmt, ChironAST.FieldAssignmentCommand):
            ntgt = self.handleFieldAssignment(stmt, tgt)
        else:
            raise NotImplementedError("Unknown instruction: %s, %s."%(type(stmt), stmt))

        # TODO: handle statement
        self.pc += ntgt

        if self.pc >= len(self.ir):
            # This is the ending of the interpreter.
            self.trtl.write("End, Press ESC", font=("Arial", 15, "bold"))
            if self.args is not None and self.args.hooks:
                self.chironhook.ChironEndHook(self)
            return True
        else:
            return False
    
    def initProgramContext(self, params):
        # This is the starting of the interpreter at setup stage.
        if self.args is not None and self.args.hooks:
            self.chironhook.ChironStartHook(self)
        self.trtl.write("Start", font=("Arial", 15, "bold"))
        for key,val in params.items():
            var = key.replace(":","")
            exec("setattr(self.prg,\"%s\",%s)" % (var, val))
     
    def perform_assign(self, lhs_prefix, rhs_prefix, t, lhs_idx="", rhs_idx=""):
        # Resolve string type to StructType if possible
        if isinstance(t, str) and t in self.structs:
            t = self.structs[t]
        
        from chirontypes import Type, ArrayType, StructType
        namespace = {"self": self, "int": int, "float": float, "str": str, "bool": bool, "copy": copy}

        if isinstance(t, StructType):
            for f_name, f_type in t.fields.items():
                self.perform_assign(f"{lhs_prefix}__{f_name}", f"{rhs_prefix}__{f_name}", f_type, lhs_idx, rhs_idx)
        elif isinstance(t, ArrayType):
            from chirontypes import ArrayType
            if self.is_struct_based(t.element_type):
                # Array of structs (SoA intermediate): 
                # Recurse into the fields of the element type, but WRAP each field type 
                # with this array dimension to maintain the SoA structure.
                st_type = t.element_type
                # If element_type is another ArrayType (nested arrays of structs), it will recurse again.
                # If it's a StructType, we iterate its fields.
                if isinstance(st_type, StructType):
                    for f_name, f_type in st_type.fields.items():
                        wrapped_f_type = ArrayType(f_type, t.size)
                        self.perform_assign(f"{lhs_prefix}__{f_name}", f"{rhs_prefix}__{f_name}", wrapped_f_type, lhs_idx, rhs_idx)
                else:
                    # element_type is another ArrayType, just recurse
                    self.perform_assign(lhs_prefix, rhs_prefix, st_type, lhs_idx, rhs_idx)
            else:
                # Array of primitives (SoA leaf array): perform deep copy
                code = f"self.prg.{lhs_prefix}{lhs_idx} = copy.deepcopy(self.prg.{rhs_prefix}{rhs_idx})"
                print(f"    Array Copy: {code}")
                exec(code, namespace, namespace)
        else:
            # Primitive assignment
            rhs_expr = f"self.prg.{rhs_prefix}{rhs_idx}"
            
            cast_func = "int" if t == Type.INT else ("float" if t in [Type.FLOAT, Type.DOUBLE] else "str")
            if t == Type.BOOLEAN:
                rhs_val = f"bool({rhs_expr})"
            elif t in [Type.INT, Type.FLOAT, Type.DOUBLE, Type.STRING]:
                rhs_val = f"{cast_func}({rhs_expr})"
            else:
                rhs_val = rhs_expr
            
            print(f"    Final assignment: self.prg.{lhs_prefix}{lhs_idx} = {rhs_val}")
            exec(f"self.prg.{lhs_prefix}{lhs_idx} = {rhs_val}", namespace, namespace)

    def handleAssignment(self, stmt, tgt):
        print("  Assignment Statement")
        namespace = {"self": self, "int": int, "float": float, "str": str, "bool": bool}

        # 1. Handle Struct Initialization (Allocation)
        if isinstance(stmt.lvar, ChironAST.Var) and self.is_struct_based(stmt.lvar.type):
             lhs_base_name = stmt.lvar.varname.replace(":", "")
             # Only allocate if proxy field doesn't exist to avoid re-allocation on reassignment
             # Wait, a safer check: does the prefix exist?
             if not hasattr(self.prg, f"__st_{lhs_base_name}"):
                 # Check any leaf field. If Point, check __st_p__x
                 # Actually, simpler: try to reach any field
                 pass # allocate_soa is called below if it's a first-time Var

        # 2. Perform Assignment
        if isinstance(stmt.rexpr, ChironAST.StructLiteral):
            lhs_prefix, lhs_indices = self.resolve(stmt.lvar)
            # Allocation check for new Var
            if isinstance(stmt.lvar, ChironAST.Var) and not hasattr(self.prg, f"__st_{stmt.lvar.varname.replace(':','')}"):
                self.allocate_soa(f"__st_{stmt.lvar.varname.replace(':','')}", stmt.lvar.type, [])
            self._assign_struct_literal(lhs_prefix, stmt.lvar.type, stmt.rexpr, lhs_indices)
        elif self.is_struct_based(stmt.lvar.type):
            lhs_prefix, lhs_indices = self.resolve(stmt.lvar)
            rhs_prefix, rhs_indices = self.resolve(stmt.rexpr)
            # Allocation check
            if isinstance(stmt.lvar, ChironAST.Var) and not hasattr(self.prg, f"__st_{stmt.lvar.varname.replace(':','')}"):
                 self.allocate_soa(f"__st_{stmt.lvar.varname.replace(':','')}", stmt.lvar.type, [])
            self.perform_assign(lhs_prefix, rhs_prefix, stmt.lvar.type, lhs_indices, rhs_indices)
        else:
            # Primitive or complex path assignment
            lhs_str = self.flatten_expr(stmt.lvar)
            rhs_str = self.flatten_expr(stmt.rexpr)
            
            # Cast if needed
            t = stmt.lvar.type
            if t == Type.INT:
                rhs_str = f"int({rhs_str})"
            elif t in [Type.FLOAT, Type.DOUBLE]:
                rhs_str = f"float({rhs_str})"
            elif t == Type.STRING:
                rhs_str = f"str({rhs_str})"
            elif t == Type.BOOLEAN:
                rhs_str = f"bool({rhs_str})"
                
            print(f"    Performing final assign: {lhs_str} = {rhs_str}")
            exec(f"{lhs_str} = {rhs_str}", namespace, namespace)

        return 1

    def handleStructDefinition(self, stmt, tgt):
        print(f"  Struct Definition: {stmt.name}")
        self.structs[stmt.name] = StructType(stmt.name, dict(stmt.fields))
        return 1

    def handleArrayAllocation(self, stmt, tgt):
        print("  Array Allocation")
        lhs_base = str(stmt.avar).replace(":", "")
        
        def create_primitive_multi_dim(sizes_exprs):
            if len(sizes_exprs) == 1:
                return f"[None] * ({sizes_exprs[0]})"
            else:
                return f"[{create_primitive_multi_dim(sizes_exprs[1:])} for _ in range({sizes_exprs[0]})]"
        
        sizes_exprs = [self.flatten_expr(s) for s in stmt.sizes]
        
        # Element type could be a struct (SoA)
        curr_t = stmt.elem_type
        if isinstance(curr_t, str) and curr_t in self.structs:
            curr_t = self.structs[curr_t]

        namespace = {"self": self, "int": int, "float": float, "str": str}

        # Convert sizes_exprs to raw integers for the base allocation
        base_dims = [eval(self.flatten_expr(s), namespace, namespace) for s in sizes_exprs]

        if isinstance(curr_t, StructType) or isinstance(curr_t, ArrayType):
            self.allocate_soa(f"__st_{lhs_base}", curr_t, base_dims)
        else:
            # Primitive array allocation
            alloc_expr = create_primitive_multi_dim(sizes_exprs)
            code = f"self.prg.{lhs_base} = {alloc_expr}"
            exec(code, namespace, namespace)
        
        return 1

        return 1

    def handleCondition(self, stmt, tgt):
        print("  Branch Instruction")
        condstr = self.flatten_expr(stmt.cond)
        namespace = {"self": self, "int": int, "float": float, "str": str, "bool": bool, "copy": copy}
        exec("self.cond_eval = %s" % (condstr), namespace, namespace)
        return 1 if self.cond_eval else tgt

    def handleMove(self, stmt, tgt):
        print("  MoveCommand")
        namespace = {"self": self, "int": int, "float": float, "str": str, "bool": bool, "copy": copy}
        exec("self.trtl.%s(%s)" % (stmt.direction, self.flatten_expr(stmt.expr)), namespace, namespace)
        return 1

    def handleNoOpCommand(self, stmt, tgt):
        print("  No-Op Command")
        return 1

    def handlePen(self, stmt, tgt):
        print("  PenCommand")
        namespace = {"self": self, "int": int, "float": float, "str": str, "bool": bool, "copy": copy}
        exec("self.trtl.%s()"%(stmt.status), namespace, namespace)
        return 1

    def handleGotoCommand(self, stmt, tgt):
        print(" GotoCommand")
        xcor = self.flatten_expr(stmt.xcor)
        ycor = self.flatten_expr(stmt.ycor)
        namespace = {"self": self, "int": int, "float": float, "str": str, "bool": bool, "copy": copy}
        exec("self.trtl.goto(%s, %s)" % (xcor, ycor), namespace, namespace)
        return 1
