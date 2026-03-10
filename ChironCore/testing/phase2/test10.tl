// Int division yields float
:div_result = 5 / 2      // 2.5 (float)

// Mixed type comparisons
:cmp1 = 10 > 3.14        // true
:cmp2 = 5.5 <= 6         // true

// Boolean logic
:bool_val = true
:not_bool = !:bool_val
:and_bool = :bool_val && (10 > 5)

// String equality
:str_eq = ("hi" == "hi")

// Parentheses for precedence
:expr = (2 + 3) * 4 - 5 / 2   // (5*4) - 2.5 = 20 - 2.5 = 17.5 (float)

// Unary minus on float
:neg_float = -3.14f

// Repeat with integer count
:repeat_count = 3
repeat :repeat_count [
    forward 10
    pause
]