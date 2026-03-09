// test_incorrect_05_bad_operators.tl
// Error: Wrong operators, invalid keywords

:x = 5 % 2             // Modulo operator not defined
:y = 10 ** 2           // Exponentiation not defined
:z = true & false      // Single '&' instead of '&&'

iif (:x > 5) [         // Typo in 'if' keyword
    forward 10
]

:type int = 5          // 'type' is keyword, can't be variable name

forwrd 100             // Typo in command