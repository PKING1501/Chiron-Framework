// test_correct_02_inference.tl
// Tests: Type inference without explicit annotations

:a = 10
:b = 20
:sum = :a + :b
:product = :a * :b

forward :sum
right :product