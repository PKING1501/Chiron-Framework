// test_correct_05_comprehensive.tl
// Tests: String concatenation, all commands, goto, pen commands

:greeting string = "Hello"
:world string = "World"
:message = :greeting + " " + :world

:distance double = 100.5
:angle int = 90

penup
goto (50, 50)
pendown

forward :distance
left :angle

if (:distance > 100.0) [
    pause
]

:iterations = 4
repeat :iterations [
    forward 50
    right 90
]