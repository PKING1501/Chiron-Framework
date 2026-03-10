:a = 10
:b = 3
:c = 2.5f
:d = 4.0

// Arithmetic
:sum = :a + :b
:diff = :a - :b
:prod = :a * :c        // float
:quot = :a / :b        // float (int/int)
:neg = -:a
:paren = (:a + :b) * (:c - :d)

// Comparisons (all produce boolean)
:lt = :a < :b
:gt = :a > :b
:lte = :a <= :b
:gte = :a >= :b
:eq = :a == :b
:neq = :a != :b

// Mixed type comparisons
:mixed_lt = :a < :c     // int < float
:mixed_eq = :a == :d    // int == double

// String comparisons
:str1 = "abc"
:str2 = "def"
:str_lt = :str1 < :str2
:str_eq = :str1 == "abc"

// Boolean comparisons (only == and !=)
:bool1 = true
:bool2 = false
:bool_eq = :bool1 == :bool2