// ChironCore/testing/struct_invalid.tl
// Testing incorrect struct usage (Type errors and Syntax errors)

struct Point {
    x int,
    y int
}

:p Point

// 1. Incorrect literal size (Too many)
// :p = {1, 2, 3}

// 2. Incorrect literal type
// :p = {1, "hello"}

// 3. Accessing non-existent field
// :p.z = 10

// 4. Assigning primitive to struct
// :p = 10

// 5. Using struct where int expected
// forward :p

// 6. Array of unknown type
// :arr NonExistent[5]

// 7. Field access on non-struct
:i int
// :i.x = 10
