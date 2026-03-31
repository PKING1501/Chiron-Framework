// test_fail.tl
:name string = "hello"
:y int = 20
// Error 1: Cannot add a string and int
:z = :name + :y
// Error 2: Forward command requires a number
forward :name
