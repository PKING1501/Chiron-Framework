// ChironCore/testing/struct_edge_cases.tl
// Comprehensive test for complex struct interactions

struct Point {
    x int,
    y int
}

struct Line {
    p1 Point,
    p2 Point
}

struct Polygon {
    vertices Point[4],
    center Point,
    id int
}

struct Mesh {
    polys Polygon[2],
    name string
}

// 1. Basic struct and structural assignment
:p1 Point = {10, 20}

:p2 Point = :p1
:p2.x = 30

// 2. Struct of structs
:l Line = {:p1, :p2}
:l.p1.y = 50

// 3. Array of structs
:points Point[3]
:points[0] = :p1
:points[1] = {100, 200}
:points[2].x = 5
:points[2].y = 6

// 4. Struct having array of structs (Deep nesting)
:poly Polygon = {}
:poly.vertices[0] = :p1
:poly.vertices[1] = {50, 60}
:poly.center = {0, 0}
:poly.id = 1

// 5. Array of structs having array of structs
:scene Mesh[2]
:scene[0].name = "Square"
:scene[0].polys[0] = :poly
:scene[0].polys[0].vertices[2] = {10, 10}

// 6. Deep access in expressions
:val = :scene[0].polys[0].vertices[2].x + :l.p1.y

// 7. Drawing with deep access
penup
goto (:scene[0].polys[0].vertices[1].x, :scene[0].polys[0].vertices[1].y)
pendown
forward :val
