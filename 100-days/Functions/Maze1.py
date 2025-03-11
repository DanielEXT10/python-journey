def turn_right():
    for i in range(3):
        turn_left()

def turn_180():
    for i in range(2):
        turn_left()

def go_straight():
    
    if front_is_clear():
        move()
        go_straight()  # Recursive call

while not at_goal():
    if right_is_clear():
        turn_right()
        go_straight()
    elif front_is_clear():
        go_straight()
    elif not front_is_clear() and right_is_clear():
        turn_right()
        go_straight()
    elif not front_is_clear() and not right_is_clear():
        turn_left()
        go_straight()