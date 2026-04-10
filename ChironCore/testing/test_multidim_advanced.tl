// Advanced Multi-dimensional Array Test Suite
// Multi-dimensional Array Test
:matrix int[2][3]

:matrix[0][0] = 1
:matrix[0][1] = 2
:matrix[0][2] = 3
:matrix[1][0] = 4
:matrix[1][1] = 5
:matrix[1][2] = 60

// Access and verify
:sum = :matrix[0][0] + (float):matrix[1][2]  // 1 + 60 = 61
backward :sum

// Nested access in assignment
:box float[2][2][2]
:box[0][0][0] = 1.1f
:box[1][1][1] = 100.2f
forward :box[1][1][1]

// 1. Nested Integer Grid with Loops
:grid_size = 3
:grid int[3][3]
:r = 0
repeat 3 [
    :c = 0
    repeat 3 [
        :grid[:r][:c] = :r + :c
        :c = :c + 1
    ]
    :r = :r + 1
]

// Verify grid contents
:val = :grid[1][1] // should be 2
if :val == 2 [
    forward 10
]

// 2. Boolean Matrix for Logic
:flags boolean[2][2]
:flags[0][0] = true
:flags[0][1] = false
:flags[1][0] = false
:flags[1][1] = true

if :flags[0][0] && :flags[1][1] [
    penup
    forward 20
    pendown
]

// 3. String Array (3D)
:cube string[2][2][2]
:cube[0][0][0] = "origin"
:cube[1][1][1] = "end"

// 4. Mixing Types with Casts
:coords float[2][2]
:coords[0][0] = 10.5f
:coords[0][1] = 20.5f
:coords[1][0] = (float):grid[0][0] // 0.0
:coords[1][1] = (float):grid[2][2] // 4.0

goto (:coords[0][0], :coords[0][1])

// 5. Array access as index for another array access
:indices int[2]
:indices[0] = 1
:indices[1] = 0
:grid[:indices[0]][:indices[1]] = 100 // sets grid[1][0] to 100
forward (float):grid[1][0]
