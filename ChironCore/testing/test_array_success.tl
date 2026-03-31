// Array Type Checking Success Test
:arr int[5]

// Valid Index Assignments
:arr[0] = 10
:arr[1] = 20

// Valid Index Access & Math
:arr[2] = :arr[0] + :arr[1]

// Safe Promotions
:arr_float float[3]
:arr_float[0] = :arr[2]  // int -> float promotion

forward :arr[2]  // Using array value in a command expression

// Multiple types
:names string[2]
:names[0] = "Chiron"
:names[1] = "Turtle"

:flags boolean[2]
:flags[0] = true
:flags[1] = false

if :flags[0] [
    forward 50
]

// Array access as index
:indices int[2]
:indices[0] = 1
:arr[:indices[0]] = 100