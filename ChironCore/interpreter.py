
from ChironAST import ChironAST
from ChironHooks import Chironhooks
from chirontypes import Type
import turtle
import time

Release="Chiron v5.3"

def addContext(s):
    return str(s).strip().replace(":", "self.prg.")

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

    def _check_type(self, value, expected_type, context=""):
        """
        Check if a runtime value matches the expected Chiron type.
        Raises a TypeError with a helpful message if there's a mismatch.
        """
        if expected_type == Type.INT and not isinstance(value, int):
            raise TypeError(f"{context}: expected int, got {type(value).__name__} ({value})")
        if expected_type == Type.FLOAT and not isinstance(value, float):
            # Allow ints to be used where float is expected (automatic promotion in Python)
            if not isinstance(value, int):
                raise TypeError(f"{context}: expected float, got {type(value).__name__} ({value})")
        if expected_type == Type.DOUBLE:
            # Python doesn't distinguish float/double; we treat both as float.
            # But we still want to disallow strings, bools, etc.
            if not isinstance(value, (int, float)):
                raise TypeError(f"{context}: expected double (numeric), got {type(value).__name__} ({value})")
        if expected_type == Type.STRING and not isinstance(value, str):
            raise TypeError(f"{context}: expected string, got {type(value).__name__} ({value})")
        if expected_type == Type.BOOLEAN and not isinstance(value, bool):
            raise TypeError(f"{context}: expected boolean, got {type(value).__name__} ({value})")

        # If the value passes the check, return it (or potentially a coerced version)
        return value

    def interpret(self):
        print("Program counter : ", self.pc)
        stmt, tgt = self.ir[self.pc]
        print(stmt, stmt.__class__.__name__, tgt)

        self.sanityCheck(self.ir[self.pc])

        if isinstance(stmt, ChironAST.AssignmentCommand):
            ntgt = self.handleAssignment(stmt, tgt)
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
        # +++ ADD THIS BRANCH +++
        elif isinstance(stmt, ChironAST.PauseCommand):
            ntgt = self.handlePauseCommand(stmt, tgt)
        # ++++++++++++++++++++++++
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
        lhs = str(stmt.lvar).replace(":", "")
        rhs_expr = stmt.rexpr

        # 1. Evaluate the right-hand side expression first.
        #    We need a way to evaluate an expression node to a Python value.
        #    Since you are using exec(), we can create a mini expression evaluator.
        #    For now, let's use exec to get the value, but we'll wrap it carefully.
        rhs_code = addContext(rhs_expr)
        local_dict = {'self': self}  # Make 'self' available so addContext works
        try:
            exec(f"__temp_val = {rhs_code}", globals(), local_dict)
            rhs_value = local_dict['__temp_val']
        except Exception as e:
            raise RuntimeError(f"Error evaluating expression '{rhs_code}': {e}")

        # 2. Get the expected type from the left-hand side variable (from static inference)
        expected_type = stmt.lvar.inferred_type
        if expected_type == Type.UNKNOWN:
            # This should not happen if type inference ran successfully.
            print(f"Warning: Variable '{lhs}' has unknown type. Skipping runtime check.")
        else:
            # 3. Check the value against the expected type
            self._check_type(rhs_value, expected_type, context=f"Assignment to '{lhs}'")

        # 4. Store the value in the program context
        exec(f"setattr(self.prg, \"{lhs}\", rhs_value)")  # Use the already-evaluated rhs_value
        return 1

    def handleCondition(self, stmt, tgt):
        print("  Branch Instruction")
        condstr = addContext(stmt)
        exec("self.cond_eval = %s" % (condstr))

        # +++ ADD RUNTIME CHECK +++
        if not isinstance(self.cond_eval, bool):
            raise TypeError(f"Condition did not evaluate to a boolean, got {type(self.cond_eval).__name__} ({self.cond_eval})")
        # +++++++++++++++++++++++++

        return 1 if self.cond_eval else tgt

    def handleMove(self, stmt, tgt):
        print("  MoveCommand")
        expr_code = addContext(stmt.expr)
        local_dict = {'self': self}
        exec(f"__move_val = {expr_code}", globals(), local_dict)
        move_val = local_dict['__move_val']

        # Runtime type check
        if not isinstance(move_val, (int, float)):
            raise TypeError(f"Move command '{stmt.direction}' requires a numeric argument, got {type(move_val).__name__} ({move_val})")

        # Directly call the turtle method
        getattr(self.trtl, stmt.direction)(move_val)
        return 1

    def handleNoOpCommand(self, stmt, tgt):
        print("  No-Op Command")
        return 1

    def handlePen(self, stmt, tgt):
        print("  PenCommand")
        getattr(self.trtl, stmt.status)()
        return 1

    def handlePauseCommand(self, stmt, tgt):
        print("  Pause Command")
        time.sleep(1)
        # Pause does nothing in the concrete interpreter, just continue
        return 1

    def handleGotoCommand(self, stmt, tgt):
        print(" GotoCommand")
        # Evaluate x coordinate
        x_code = addContext(stmt.xcor)
        local_dict = {'self': self}
        exec(f"__x_val = {x_code}", globals(), local_dict)
        x_val = local_dict['__x_val']

        # Evaluate y coordinate
        y_code = addContext(stmt.ycor)
        exec(f"__y_val = {y_code}", globals(), local_dict)
        y_val = local_dict['__y_val']

        # Runtime type checks
        if not isinstance(x_val, (int, float)):
            raise TypeError(f"Goto x-coordinate must be numeric, got {type(x_val).__name__} ({x_val})")
        if not isinstance(y_val, (int, float)):
            raise TypeError(f"Goto y-coordinate must be numeric, got {type(y_val).__name__} ({y_val})")

        # Direct call
        self.trtl.goto(x_val, y_val)
        return 1
