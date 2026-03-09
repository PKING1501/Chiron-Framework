// test_incorrect_04_bad_variables.tl
// Error: Variables must start with ':'

x = 10                 // Missing ':' prefix
:123invalid = 5        // Variable name starts with number
:-name = "test"        // Hyphen not allowed after ':'
: space = 42           // Space in variable name