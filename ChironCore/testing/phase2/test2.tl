// No type annotations – types inferred from literals and operations

:x = 10
:y = 3.5f
:z = 2.0
:msg = "Inferred"
:flag = true

// Mixed arithmetic
:sum1 = :x + :y       // float
:sum2 = :y + :z       // double
:product = :x * :z    // double
:div = :x / 3         // float (int/int → float)

// Comparisons
:cond1 = (:x > :y)    // boolean
:cond2 = (:msg == "Inferred")

// Logical
:result = :cond1 && :cond2

// Turtle commands
forward :sum1
right :div