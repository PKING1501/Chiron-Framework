// Struct declaration
struct Point {
    x int,
    y int
}

struct Line {
    p1 Point,
    p2 Point
}

// Struct initialization
:p1 Point = {10, 20}
:p2 Point = {30, 40}

// Field access
:x1 = :p1.x
:y1 = :p1.y

// Struct assignment (copy)
:p3 Point = :p1
:p3.x = 100

// Nested struct
:l Line = {:p1, :p2}
:lx = :l.p1.x

// Array of structs (SoA)
:points Point[5]
:points[0].x = 5
:points[0].y = 15
:px0 = :points[0].x

// Array of structs which have struct fields (AoSoA)
:lines Line[3]
:lines[0].p1 = :p1
:lines[0].p2 = :p2
:line0_p1x = :lines[0].p1.x


// Move using struct field
forward :p1.x
left :p1.y
forward :p3.x
