// Explicit Typecasting Demo (Corrected Syntax)

:f float = (float) 100.9
:d double = 90.7

// Cast float to int for movement
forward (int) :f

// Cast double to int for rotation
left (int) :d

// Mixed types with casting
:result float = :f + (float) :d
forward (int) (:result / 2.0)

// String casting
:s string = (string) :f

// Repeat loop with casted variable
:loop_count float = (float) 5.0
:c int = (int) :loop_count
repeat :c [
    forward 10
    left 72
]

penup
goto((int) :f, (int) :d)
pendown
forward 20
