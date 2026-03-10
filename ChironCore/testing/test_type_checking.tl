:x int = 50         // Correct: int assigned to int variable
:y string = "hello" // Correct: string assigned to string variable

// This line has a TYPE ERROR - will only be caught with --tis
:z int = "world"    // ERROR: assigning string to int variable

// Simple command to verify execution
forward :x