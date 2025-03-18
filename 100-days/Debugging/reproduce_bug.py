from random import randint

dice_faces = [1,2,3,4,5,6]
dice_num = randint(0,5) #Every time it hits 6 is going to throw an error
print(dice_faces[dice_num])
