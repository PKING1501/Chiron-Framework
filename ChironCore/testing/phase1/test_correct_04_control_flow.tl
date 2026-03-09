// test_correct_04_control_flow.tl
// Tests: Conditionals, loops, boolean expressions

:count int = 5
:flag boolean = true

if (:count > 3) [
    forward 100
    right 90
]

if (:flag && !:flag) [
    left 45
] else [
    right 45
]

repeat :count [
    forward 50
    right 72
]