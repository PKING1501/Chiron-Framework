
from ChironAST import ChironAST
from ChironHooks import Chironhooks
from chirontypes import Type, ArrayType
import turtle

Release="Chiron v5.3"

def addContext(node):
    if isinstance(node, str):
        return node.strip().replace(":", "self.prg.")
    
    from chirontypes import StructType, ArrayType
    
    # helper for SoA flattening in expressions
    def flatten_expr(expr):
        if isinstance(expr, ChironAST.FieldAccess):
            # Resolve the base (could be a Var or ArrayAccess or another FieldAccess)
            if isinstance(expr.obj_expr, ChironAST.Var):
                base_name = expr.obj_expr.varname.replace(":", "")
                return f"self.prg.__st_{base_name}__{expr.field_name}"
            elif isinstance(expr.obj_expr, ChironAST.ArrayAccess):
                base_var = expr.obj_expr.avar
                base_name = base_var.varname.replace(":", "")
                indices_str = "".join([f"[{flatten_expr(i)}]" for i in expr.obj_expr.indices])
                return f"self.prg.__st_{base_name}__{expr.field_name}{indices_str}"
            elif isinstance(expr.obj_expr, ChironAST.FieldAccess):
                # Nested struct: s.a.b -> __st_s__a__b
                inner_flattened = flatten_expr(expr.obj_expr)
                # inner_flattened is self.prg.__st_s__a
                # we want self.prg.__st_s__a__b
                return inner_flattened + "__" + expr.field_name
            else:
                # Fallback
                return f"({flatten_expr(expr.obj_expr)}).{expr.field_name}"
        elif isinstance(expr, ChironAST.Var):
            return "self.prg." + expr.varname.replace(":", "")
        elif isinstance(expr, ChironAST.ArrayAccess):
            base_name = expr.avar.varname.replace(":", "")
            indices_str = "".join([f"[{flatten_expr(i)}]" for i in expr.indices])
            return f"self.prg.{base_name}{indices_str}"
        else:
            # For other expressions, use the standard __str__ and replace colons
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
    
    def handleAssignment(self, stmt, tgt):
        print("  Assignment Statement")
        lhs_base = str(stmt.lvar).replace(":","")
        from chirontypes import StructType, ArrayType
        
        # Helper for recursive initialization/copying
        def perform_assign(lhs_prefix, rhs_expr_str, t):
            if isinstance(t, StructType):
                # Copying a whole struct (from another struct var)
                # RHS should be another struct var name in Python (flattened)
                for f_name, f_type in t.fields.items():
                    perform_assign(f"{lhs_prefix}__{f_name}", f"{rhs_expr_str}__{f_name}", f_type)
            else:
                # Primitive assignment
                rhs_val = rhs_expr_str
                if t in [Type.FLOAT, Type.DOUBLE]:
                    rhs_val = f"float({rhs_val})"
                elif t == Type.INT:
                    rhs_val = f"int({rhs_val})"
                elif t == Type.STRING:
                    rhs_val = f"str({rhs_val})"
                exec(f"setattr(self.prg, \"{lhs_prefix}\", {rhs_val})")

        if isinstance(stmt.rexpr, ChironAST.StructLiteral):
            # Initializing with {v1, v2, ...}
            st_type = stmt.lvar.type
            for (f_name, f_type), val_expr in zip(st_type.fields.items(), stmt.rexpr.values):
                val_rhs = addContext(val_expr)
                # Note: Literals don't need __st_ prefix on themselves, but their destination does
                perform_assign(f"__st_{lhs_base}__{f_name}", val_rhs, f_type)
        elif isinstance(stmt.lvar.type, StructType):
            # Assignment from another struct: s1 = s2
            rhs_base = addContext(stmt.rexpr) # self.prg.s2 (Wait, s2 is flattened!)
            # Actually, addContext(Var(":s2")) -> self.prg.s2. But we want self.prg.__st_s2
            # If it's a Var, we can do it easily.
            if isinstance(stmt.rexpr, ChironAST.Var):
                rhs_st_base = "__st_" + stmt.rexpr.varname.replace(":", "")
                for f_name, f_type in stmt.lvar.type.fields.items():
                    perform_assign(f"__st_{lhs_base}__{f_name}", f"self.prg.{rhs_st_base}__{f_name}", f_type)
            else:
                # Complex RHS result? Not supported yet (no function calls)
                raise NotImplementedError("Structural assignment from complex expressions not supported.")
        else:
            # Normal primitive assignment
            rhs = addContext(stmt.rexpr)
            if stmt.lvar.type in [Type.FLOAT, Type.DOUBLE]:
                rhs = f"float({rhs})"
            elif stmt.lvar.type == Type.INT:
                rhs = f"int({rhs})"
            elif stmt.lvar.type == Type.STRING:
                rhs = f"str({rhs})"
            setattr(self.prg, lhs_base, eval(rhs, {"self": self, "int": int, "float": float, "str": str}))

        return 1

    def handleFieldAssignment(self, stmt, tgt):
        print("  Field Assignment Statement")
        # s.a.b = val -> __st_s__a__b = val
        # arr[i].a = val -> __st_arr__a[i] = val
        
        if isinstance(stmt.obj_expr, ChironAST.Var):
            base_name = "__st_" + stmt.obj_expr.varname.replace(":", "")
            indices_str = ""
        elif isinstance(stmt.obj_expr, ChironAST.ArrayAccess):
            base_name = "__st_" + stmt.obj_expr.avar.varname.replace(":", "")
            indices_str = "".join([f"[{addContext(i)}]" for i in stmt.obj_expr.indices])
        else:
             raise NotImplementedError("Only Var and ArrayAccess supported as base for field assignment.")

        flattened_name = base_name + "__" + "__".join(stmt.fields)
        rhs_expr = addContext(stmt.rexpr)
        exec(f"self.prg.{flattened_name}{indices_str} = {rhs_expr}")
        return 1

    def handleStructDefinition(self, stmt, tgt):
        print(f"  Struct Definition: {stmt.name}")
        return 1

    def handleArrayAllocation(self, stmt, tgt):
        print("  Array Allocation")
        lhs_base = str(stmt.avar).replace(":", "")
        from chirontypes import StructType, ArrayType
        
        def create_primitive_multi_dim(sizes_exprs):
            if len(sizes_exprs) == 1:
                return f"[None] * ({sizes_exprs[0]})"
            else:
                return f"[{create_primitive_multi_dim(sizes_exprs[1:])} for _ in range({sizes_exprs[0]})]"
        
        sizes_exprs = [addContext(s) for s in stmt.sizes]
        
        # Element type could be a struct (SoA)
        curr_t = stmt.elem_type
        if isinstance(curr_t, StructType):
            # Create multiple arrays, one for each field
            for f_name, f_type in curr_t.fields.items():
                alloc_expr = create_primitive_multi_dim(sizes_exprs)
                exec(f"self.prg.__st_{lhs_base}__{f_name} = {alloc_expr}")
        else:
            alloc_expr = create_primitive_multi_dim(sizes_exprs)
            exec(f"self.prg.{lhs_base} = {alloc_expr}")
            
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
