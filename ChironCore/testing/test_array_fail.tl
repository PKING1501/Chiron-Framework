// Array Type Checking Failure Test
:arr int[5]

// Error: Assigning string to int[]
:arr[0] = "hello"

// Error: Accessing before allocation
:arr2[0] = 5

// Error: Using float as index
:arr[1.5] = 10

// Error: Using non-array as array
:x int = 10
:x[0] = 5
