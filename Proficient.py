#See the README file for how to use the golf module

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
while distance > 0:

    powerLevel = int(input("Enter Distance between 10 and 40: "))

	
	
    if powerLevel >= 10 and powerLevel <= 40:
			
        shot = golf.shootBall(powerLevel)
        distance -= shot
        totalShots += 1
			
        print("You shot the ball " + str(round(shot, 1)) + " yards")
        print("You have " + str(round(distance, 1)) + " yards remaining")
			
    else:
        print("Please try again!")

print("Finished! You got the ball in the hole")

print("Your score is " + str(totalShots - par))
