// Array Type Checking Success Test
:arr int[5]

// Valid Index Assignments
:arr[0] = 10
:arr[1] = 20

// Valid Index Access & Math
:arr[2] = :arr[0] + :arr[1]

// Safe Promotions
:arr_float float[3]
:arr_float[0] = :arr[2]

forward :arr[4]  // Using array value in a command expression