:count = 5
:step = 10
:angle = 72

repeat :count [
    forward :step
    right :angle
    :step = :step + 5
]

// nested loop
:outer = 3
:inner = 4
repeat :outer [
    forward 30
    repeat :inner [
        forward 10
        left 90
    ]
    right 120
]