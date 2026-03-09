// test_incorrect_01_bad_type_annotation.tl
// Error: Type annotation without '='

:x int 42              // Missing '=' between type and value
:y float               // Type annotation without assignment
:z = int 5             // Type on wrong side of '='