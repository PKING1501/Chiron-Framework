// Array Type Checking Failure Test

// Error: Accessing before allocation
:arr_no[0] = 5

:arr int[5]

// Error: Assigning string to int[]
:arr[0] = "hello"

// Error: Assigning float to int[] (Demotion not allowed by is_assignable)
:arr[1] = 10.5

// Error: Using float as index
:arr[1.5] = 10

// Error: Using string as index
:arr["0"] = 5

// Error: Using boolean as index
:arr[true] = 1

// Error: Using non-array as array
:x int = 10
:x[0] = 5

// Error: Redeclaring variable as array
:y float = 1.1
:y float[5]

