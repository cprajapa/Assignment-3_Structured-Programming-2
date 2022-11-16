# See the README file for how to use the golf module

import random

from Golf import Golf

golf = Golf()


def golfGame(distance):
    golf.drawHole(distance)

    if distance >= 100 and distance <= 250:

        par = 3

        golf.drawText("Hole 1: Par 3, " + str(distance) + " yards")

    elif distance >= 251 and distance <= 450:

        par = 4

        golf.drawText("Hole 1: Par 4, " + str(distance) + " yards")

    elif distance >= 451 and distance <= 650:

        par = 5

        golf.drawText("Hole 1: Par 5, " + str(distance) + " yards")

    totalShots = 0
    while distance > 10:

        wedge = "1"
        iron = "2"
        driver = "3"

        print(wedge + ") Wedge")
        print(iron + ") Iron")
        print(driver + ") Driver")
        print()

        club = input("Select club: ")

        if club == wedge:  # lower power, higher angle/loft
            powerLevel = random.randint(11, 20)
            angle = random.randint(60, 80)
        elif club == iron:  # medium power, medium angle/loft
            powerLevel = random.randint(21, 30)
            angle = random.randint(45, 59)
        elif club == driver:  # higher power, lower angle/loft
            powerLevel = random.randint(31, 40)
            angle = random.randint(30, 44)
        else:
            print("Select the correct club:")

        shot = golf.shootBall(powerLevel, angle)
        distance -= shot
        totalShots += 1

        print("You shot the ball " + str(round(shot, 1)) + " yards")
        print("You have " + str(round(distance, 1)) + " yards remaining")

    print("Finished! You got the ball in the hole")

    print("Your score is " + str(totalShots - par))

    golf.clearScreen()


d1 = random.randint(100, 650)
d2 = random.randint(100, 650)
d3 = random.randint(100, 650)

for i in range(d1, d2, d3):
    golfGame(d1)
    golfGame(d2)
    golfGame(d3)
