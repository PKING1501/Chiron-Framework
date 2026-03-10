:x = 5
:y = 10
:flag = true
:another = false

// Logical expressions
:and_expr = (:x < :y) && :flag
:or_expr = (:x > :y) || :another
:not_expr = !:flag
:complex = (:x < :y) && !:another || (:y == 10)

// if-else with boolean condition
if (:and_expr) [
    forward 50
] else [
    backward 50
]

// if with simple condition
if (:x > 3) [
    right 90
]

// if-else with complex condition
if (:complex) [
    penup
] else [
    pendown
]

// repeat loop
repeat 4 [
    forward 20
    left 90
]