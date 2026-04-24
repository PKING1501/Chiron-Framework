
from ChironAST import ChironAST
from ChironHooks import Chironhooks
from chirontypes import Type, ArrayType, StructType
import turtle

Release="Chiron v5.3"

def addContext(node):
    if isinstance(node, str):
        return node.strip().replace(":", "self.prg.")
    
    
    # helper for SoA flattening in expressions
    def flatten_expr(expr):
        def is_struct_based(t):
            if isinstance(t, StructType):
                return True
            if isinstance(t, ArrayType):
                return is_struct_based(t.element_type)
            return False

        def resolve(e):
            # Returns (flattened_name_segment, indices_str)
            if isinstance(e, ChironAST.FieldAccess):
                name, indices = resolve(e.obj_expr)
                return f"{name}__{e.field_name}", indices
            elif isinstance(e, ChironAST.ArrayAccess):
                name, indices = resolve(e.avar)
                new_indices = "".join([f"[{flatten_expr(i)}]" for i in e.indices])
                return name, indices + new_indices
            elif isinstance(e, ChironAST.Var):
                prefix = "__st_" if is_struct_based(e.type) else ""
                name = prefix + e.varname.replace(":", "")
                return name, ""
            else:
                return str(e).replace(":", "self.prg."), ""

        if isinstance(expr, (ChironAST.FieldAccess, ChironAST.ArrayAccess, ChironAST.Var)):
            name, indices = resolve(expr)
            return f"self.prg.{name}{indices}"
        elif isinstance(expr, ChironAST.BinArithOp):
            return f"({flatten_expr(expr.lexpr)} {expr.symbol} {flatten_expr(expr.rexpr)})"
        elif isinstance(expr, ChironAST.UnaryArithOp):
            return f"{expr.symbol}{flatten_expr(expr.expr)}"
        elif isinstance(expr, ChironAST.BinCondOp):
            return f"({flatten_expr(expr.lexpr)} {expr.symbol} {flatten_expr(expr.rexpr)})"
        elif isinstance(expr, ChironAST.NOT):
            return f"(not {flatten_expr(expr.expr)})"
        elif hasattr(expr, "val"): # Literals
            return str(expr)
        elif isinstance(expr, ChironAST.PenStatus):
            return "self.trtl.isdown()"
        else:
            return str(expr).replace(":", "self.prg.")

    return flatten_expr(node)

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
     
    def perform_assign(self, lhs_prefix, rhs_expr_str, t, indices_str=""):
        # Resolve string type to StructType if possible
        if isinstance(t, str) and t in self.structs:
            t = self.structs[t]
            
        print(f"    Performing assign: {lhs_prefix}{indices_str} = {rhs_expr_str} (type: {t})")
        if isinstance(t, StructType):
            # Copying a whole struct (from another struct var)
            for f_name, f_type in t.fields.items():
                self.perform_assign(f"{lhs_prefix}__{f_name}", f"{rhs_expr_str}__{f_name}", f_type, indices_str)
        else:
            # Primitive assignment
            rhs_val = rhs_expr_str
            if t in [Type.FLOAT, Type.DOUBLE]:
                rhs_val = f"float({rhs_val})"
            elif t == Type.INT:
                rhs_val = f"int({rhs_val})"
            elif t == Type.STRING:
                rhs_val = f"str({rhs_val})"
            
            print(f"    Final assignment: self.prg.{lhs_prefix}{indices_str} = {rhs_val}")
            exec(f"self.prg.{lhs_prefix}{indices_str} = {rhs_val}")

    def handleAssignment(self, stmt, tgt):
        print("  Assignment Statement")
        lhs_base = str(stmt.lvar).replace(":","")
        
        if isinstance(stmt.rexpr, ChironAST.StructLiteral):
            # Initializing with {v1, v2, ...}
            st_type = stmt.lvar.type
            for (f_name, f_type), val_expr in zip(st_type.fields.items(), stmt.rexpr.values):
                val_rhs = addContext(val_expr)
                self.perform_assign(f"__st_{lhs_base}__{f_name}", val_rhs, f_type)
        elif isinstance(stmt.lvar.type, StructType):
            # Assignment from another struct: s1 = s2
            if isinstance(stmt.rexpr, ChironAST.Var):
                rhs_st_base = "__st_" + stmt.rexpr.varname.replace(":", "")
                for f_name, f_type in stmt.lvar.type.fields.items():
                    self.perform_assign(f"__st_{lhs_base}__{f_name}", f"self.prg.{rhs_st_base}__{f_name}", f_type)
            else:
                # Fallback for general expressions that evaluate to a struct
                rhs_expr_str = addContext(stmt.rexpr)
                for f_name, f_type in stmt.lvar.type.fields.items():
                    self.perform_assign(f"__st_{lhs_base}__{f_name}", f"{rhs_expr_str}__{f_name}", f_type)
        else:
            # Normal primitive assignment
            rhs = addContext(stmt.rexpr)
            if stmt.lvar.type in [Type.FLOAT, Type.DOUBLE]:
                rhs = f"float({rhs})"
            elif stmt.lvar.type == Type.INT:
                rhs = f"int({rhs})"
            elif stmt.lvar.type == Type.STRING:
                rhs = f"str({rhs})"
            print(f"    Performing primitive assign: self.prg.{lhs_base} = {rhs}")
            setattr(self.prg, lhs_base, eval(rhs, {"self": self, "int": int, "float": float, "str": str}))

        return 1

    def handleFieldAssignment(self, stmt, tgt):
        print("  Field Assignment Statement")
        # Resolve base name and any indices
        if isinstance(stmt.obj_expr, ChironAST.Var):
            base_name = "__st_" + stmt.obj_expr.varname.replace(":", "")
            indices_str = ""
            curr_type = stmt.obj_expr.type
        elif isinstance(stmt.obj_expr, ChironAST.ArrayAccess):
            base_name = "__st_" + stmt.obj_expr.avar.varname.replace(":", "")
            indices_str = "".join([f"[{addContext(i)}]" for i in stmt.obj_expr.indices])
            curr_type = stmt.obj_expr.type 
        else:
             raise NotImplementedError("Only Var and ArrayAccess supported as base for field assignment.")

        # Resolve the type of the field we are assigning to
        for field_name in stmt.fields:
            if isinstance(curr_type, StructType):
                curr_type = curr_type.fields[field_name]
            else:
                # Should have been caught by type checking
                raise TypeError(f"Cannot access field {field_name} on non-struct type {curr_type}")

        flattened_name = base_name + "__" + "__".join(stmt.fields)
        rhs_expr = addContext(stmt.rexpr)
        
        if isinstance(curr_type, StructType):
            # Structural copy to a field
            self.perform_assign(flattened_name, rhs_expr, curr_type, indices_str)
        else:
            # Primitive assignment to a field
            if curr_type in [Type.FLOAT, Type.DOUBLE]:
                rhs_expr = f"float({rhs_expr})"
            elif curr_type == Type.INT:
                rhs_expr = f"int({rhs_expr})"
            elif curr_type == Type.STRING:
                rhs_expr = f"str({rhs_expr})"
            
            exec(f"self.prg.{flattened_name}{indices_str} = {rhs_expr}")
        
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
        
        sizes_exprs = [addContext(s) for s in stmt.sizes]
        
        # Element type could be a struct (SoA)
        curr_t = stmt.elem_type
        if isinstance(curr_t, str) and curr_t in self.structs:
            curr_t = self.structs[curr_t]

        namespace = {"self": self, "int": int, "float": float, "str": str}

        def allocate_soa(prefix, t):
            # Resolve string type to StructType if possible
            if isinstance(t, str) and t in self.structs:
                t = self.structs[t]
                
            if isinstance(t, StructType):
                for f_name, f_type in t.fields.items():
                    print(f"    Allocating field {prefix}__{f_name} of type {f_type}")
                    allocate_soa(f"{prefix}__{f_name}", f_type)
            else:
                alloc_expr = create_primitive_multi_dim(sizes_exprs)
                code = f"self.prg.{prefix} = {alloc_expr}"
                print(f"    Allocating array for leaf field {prefix}: {code}")
                exec(code, namespace, namespace)

        if isinstance(curr_t, StructType):
            allocate_soa(f"__st_{lhs_base}", curr_t)
        else:
            alloc_expr = create_primitive_multi_dim(sizes_exprs)
            code = f"self.prg.{lhs_base} = {alloc_expr}"
            exec(code, namespace, namespace)
        
        return 1

    def handleArrayAssignment(self, stmt, tgt):
        print("  Array Assignment Statement")
        lhs_var = str(stmt.avar).replace(":", "")
        indices_str = "".join([f"[{addContext(i)}]" for i in stmt.indices])
        rhs_expr = addContext(stmt.rexpr)
        
        # Get the leaf element type (drill down through ArrayTypes)
        curr_t = stmt.avar.type
        while isinstance(curr_t, ArrayType):
            curr_t = curr_t.element_type
            
        if curr_t in [Type.FLOAT, Type.DOUBLE]:
            rhs_expr = f"float({rhs_expr})"
        elif curr_t == Type.INT:
            rhs_expr = f"int({rhs_expr})"
        elif curr_t == Type.STRING:
            rhs_expr = f"str({rhs_expr})"
            
        exec(f"self.prg.{lhs_var}{indices_str} = {rhs_expr}")
        return 1

    def handleCondition(self, stmt, tgt):
        print("  Branch Instruction")
        condstr = addContext(stmt)
        exec("self.cond_eval = %s" % (condstr))
        return 1 if self.cond_eval else tgt

    def handleMove(self, stmt, tgt):
        print("  MoveCommand")
        exec("self.trtl.%s(%s)" % (stmt.direction,addContext(stmt.expr)))
        return 1

    def handleNoOpCommand(self, stmt, tgt):
        print("  No-Op Command")
        return 1

    def handlePen(self, stmt, tgt):
        print("  PenCommand")
        exec("self.trtl.%s()"%(stmt.status))
        return 1

    def handleGotoCommand(self, stmt, tgt):
        print(" GotoCommand")
        xcor = addContext(stmt.xcor)
        ycor = addContext(stmt.ycor)
        exec("self.trtl.goto(%s, %s)" % (xcor, ycor))
        return 1
