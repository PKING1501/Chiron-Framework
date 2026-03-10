// Tests: int, float, double, string, boolean literals and assignments

:a int = 42
:b float = 3.14f
:c double = 2.718
:d string = "Hello"
:e boolean = true

// Arithmetic with promotion
:f = :a + :b          // int + float → float
:g = :a * :c          // int * double → double
:h = :b / :c          // float / double → double
:i = :a + 5           // int + int → int

// String concatenation
:j = :d + " World"    // string + string

// Boolean operations
:k = :e && (:a > 10)
:l = !:e || (:b < 5.0)

// Use in turtle commands
forward :a
backward :b
left :c
right (:a + :b)

penup
goto (:a, :b)
pendown