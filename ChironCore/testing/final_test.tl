// Final Test for Type System and Casting

:x = 10.5 // Inferred as double
forward (int) :x // Explicit cast double to int

:s string = (string) 42
:y float = (float) 3.14

// This should fail (uncomment to test):
:x = "hello" // Error: cannot assign string to double

// This should be a syntax error (uncomment to test):
:u unknown = 10 // Error: unknown is not a valid type keyword
