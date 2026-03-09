// test_correct_03_expressions.tl
// Tests: Nested expressions, operator precedence, parentheses

:x = 5
:y = 3
:result = (:x + :y) * 2 - 1
:calc = :x * :y + :x / :y

forward (:result + 10)
backward (:calc)