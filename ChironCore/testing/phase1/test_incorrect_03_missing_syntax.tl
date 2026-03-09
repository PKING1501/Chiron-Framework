// test_incorrect_03_missing_syntax.tl
// Error: Missing brackets, parentheses, values

if :x > 5              // Missing brackets around condition body
    forward 10
]

repeat 5 [             // Missing closing bracket
    left 90

goto (50, )            // Missing second coordinate

:result = (:x + )      // Incomplete expression