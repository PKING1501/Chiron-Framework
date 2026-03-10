:greeting = "Hello"
:name = "Chiron"
:message = :greeting + " " + :name + "!"

if (:message == "Hello Chiron!") [
    forward 100
] else [
    backward 100
]