:x float = (float) 10.5
:y int = (int) :x
forward :y

:s string = (string) 3.14
:z double = (double) 42
forward (int) :z

// This should work because unknown is universal
:u unknown = (float) 100
:w float = (float) :u

// This should fail type checking if uncommented
:err string = (string)(float) 10
