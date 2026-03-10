// Mix of all features: types, annotations, inference, ops, conditionals, loops, commands

:score int = 100
:ratio float = 0.75f
:factor double = 1.5
:name string = "Turtle"
:debug boolean = true

// Arithmetic with promotion
:calc1 = :score * :ratio           // float
:calc2 = :calc1 + :factor          // double
:calc3 = :score / 2                // float

// Comparisons
:cond1 = (:calc1 > 50.0)
:cond2 = (:name == "Turtle")
:cond3 = :debug && !:cond2

// Conditional
if (:cond1) [
    forward :calc2
    right 90
] else [
    if (:cond3) [
        left 45
    ] else [
        right 45
    ]
]

// Loop with counter update
:count = 4
repeat :count [
    forward 30
    right 90
    :count = :count - 1
]

// Goto and pen
penup
goto (:calc1, :calc2)
pendown

pause
forward 50