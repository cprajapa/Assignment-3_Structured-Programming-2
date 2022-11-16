# See the README file for how to use the golf module

for i in range(3):

    from Golf import Golf
    import random

    golf = Golf()

    distance = random.randint(100, 650)

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

        print()
        print(wedge + ") Wedge")
        print(iron + ") Iron")
        print(driver + ") Driver")
        print()

        club = input("Select club: ")

        print()

        forward = "1"
        back = "2"

        direction = input("Type 1 to go forward or 2 to go back: ")

        if direction == forward:

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

        if direction == back:

            if club == wedge:  # lower power, higher angle/loft
                powerLevel = random.randint(-20, -11)
                angle = random.randint(60, 80)
            elif club == iron:  # medium power, medium angle/loft
                powerLevel = random.randint(-30, -21)
                angle = random.randint(45, 59)
            elif club == driver:  # higher power, lower angle/loft
                powerLevel = random.randint(-40, -31)
                angle = random.randint(30, 44)
            else:
                print("Select the correct club:")

        else:
            print("Select the correct direction:")

        shot = golf.shootBall(powerLevel, angle)
        distance -= shot
        totalShots += 1

        print()

        print("You shot the ball " + str(round(shot, 1)) + " yards")
        print()

        print("You have " + str(round(distance, 1)) + " yards remaining")
        print()

    print("Finished! You got the ball in the hole")
    print()

    print("Your score is " + str(totalShots - par))
    print()

    golf.clearScreen()
