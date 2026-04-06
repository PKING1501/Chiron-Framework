:x = 10.0
:x = 42
:x = "hello" // Uncomment to see if it fails (should fail if locked to INT)

:u unknown = 10
:u = "hello" // Should work because :u is universal
:u = 3.14

:a float = 10
:a = (float) 20 // Should work
:a = "err" // Should fail
