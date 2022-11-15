#See the README file for how to use the golf module

from Golf import Golf
import random

golf = Golf()
distance1 = random.randint(100, 650)
distance2 = random.randint(100, 650)
distance3 = random.randint(100, 650)
golf.drawHole(distance1)
golf.drawHole(distance2)
golf.drawHole(distance3)

#golf.shootBall(50,30)

if distance1 >= 100 and distance1 <= 250:

    par = 3

    golf.drawText("Hole 1: Par 3, " + str(distance1) + " yards")

elif distance1 >= 251 and distance1 <= 450:

    par = 4

    golf.drawText("Hole 1: Par 4, " + str(distance1) + " yards")

elif distance1 >= 451 and distance1 <= 650:

    par = 5

    golf.drawText("Hole 1: Par 5, " + str(distance1) + " yards")

totalShots = 0
while distance1 > 10:
	
	wedge = "1"
	iron = "2"
	driver = "3"

	print(wedge + ") Wedge")
	print(iron + ") Iron")
	print(driver + ") Driver")
	print()

	club = int(input("Select club: "))
	
	if club == wedge: #lower power, higher angle/loft
		powerLevel = random.randit(11, 20)
	elif club == iron: #medium power, medium angle/loft
		powerLevel = random.randit(21, 30)
	elif club == driver: #higher power, lower angle/loft
		powerLevel = random.randit(31, 40)
	else:
		print("Select the correct club:")
  
	
	shot = golf.shootBall(powerLevel)
	distance1 -= shot
	totalShots += 1
	
	print("You shot the ball " + str(round(shot, 1)) + " yards")
	print("You have " + str(round(distance1, 1)) + " yards remaining")

print("Finished! You got the ball in the hole")

print("Your score is " + str(totalShots - par))
