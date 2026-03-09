// test_incorrect_02_bad_literals.tl
// Error: Invalid literal formats

:a = 3.14.5            // Double decimal point
:b = 42f               // Integer with float suffix (missing decimal)
:c = "unterminated     // Unclosed string
:d = truee             // Misspelled boolean
:e = 3.14ff            // Double 'f' suffix