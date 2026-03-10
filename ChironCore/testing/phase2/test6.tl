:x = 100
:y = 200
:step = 50

penup
goto (:x, :y)
pendown

forward :step
left 90
forward :step
right 90
goto (:x / 2, :y / 2)