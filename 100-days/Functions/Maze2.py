def turn_right():
    for i in range(3):
        turn_left()

def turn_180():
    for i in range(2):
        turn_left()

def go_straight():
    while front_is_clear():  # Move while possible
        if right_is_clear():  # If there's an opening on the right, turn immediately
            turn_right()
            move()
            go_straight()  # Continue moving recursively after turning
            return  # Stop further execution after turning
        move()
    
    # If front is blocked and no right turn was taken, stop and turn left
    turn_left()  

while not at_goal():
    go_straight()
