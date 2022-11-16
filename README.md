# Directions

Create a text based golf program using the "Golf.py" module provided.

**The Golf.py file**

The Golf.py file has been created for you to visualize the golf program. You do not need to look at or understand the
code in that file, but please do not delete it.

You only need to understand these functions inside the file:

* golf = Golf()
    * initializes the Golf class so that you can use it
* golf.drawHole(distance)
    * draws the hole at the distance specified
* golf.drawText(text, x=0, y=0)
    * draws text at the top left of the screen
* golf.clearScreen()
    * clears all turtle art on the screen
* golf.shootBall(power, angle=45)
    * shoots the ball in a parabolic arc at the power level specified. This function will also return the distance the
      ball was shot

**Example:**
> from Golf import Golf  
> golf = Golf()  
> golf.drawHole(100)  
> golf.drawText("Hole 1: 100 yards")  
> distance = golf.shootBall(30)  
> print(distance)

**Output**
91.85317087613151

Use this to get started at the developing level.
You may want to round the resulting distance using the round function.

## Assessment Levels

Start at developing and work your way up. To pass the course you only need to demonstrate a developing level of
understanding.

* Create a flowchart or pseudocode algorithm using the files in Replit. Remember to update your algorithm as your
  progress through the levels.
* Use if statements, while loops, and for loops. * Try to avoid code duplication, and make your code as simple as
  possible.
* Use proper variable names and reassign variables instead of creating unnecessary new ones.

### Developing

* Create a distance to the hole
* Allow the user to continuously enter a number between 10 and 40, until they get the golf ball past the hole, using a
  while loop
* After each shot, display the distance the user shot the ball, and the distance remaining
* When the ball is past the hole output "Finished! You got the ball in the hole."

**Code Hint:**
> from Golf import Golf  
> golf = Golf()  
> distance = 500  
> golf.drawHole(distance)  
> golf.drawText("Hole 1: "+str(distance) +" yards")


> #Create while loop that continues as long as the distance is greater than 0
>> #input user power level between 10 and 40  
> > #calculate shot distance using shot = golf.shootBall(power level)  
> > #output shot distance  
> > #calculate remaining distance #output yards remaining

> #output finished

**Example Output**
> Enter power level between 10 and 40 to shoot the ball: 20  
> You shot the ball 40.9 yards  
> You have 259.1 yards remaining  
> Enter power level between 10 and 40 to shoot the ball: 33  
> You shot the ball 111.1 yards  
> You have 148.0 yards remaining  
> Enter power level between 10 and 40 to shoot the ball: 40  
> Finished! You got the ball in the hole

### Proficient

* Use the random module to create a random distance to the hole between 100 and 650.
* Create a corresponding par related to the distance. Par represents the recommended number of shots to get the ball in
  the hole. Display this par and the distance in the top corner of the graphics window
    * Par 3: 100 yards to 250 yards
    * Par 4: 251 yards to 450 yards
    * Par 5: 451 yards to 650 yards
* Allows the user to continuously enter a number between 10 and 40, until they get the golf ball past the hole, using a
  while loop
* If they enter a value outside the range allow them to try again
* After each shot, display the distance the user shot the ball, and the distance remaining
  when the ball is past the hole output "Finished! You got the ball in the hole."
* Calculate and display the users score once their ball is past the hole by taking their total shots-par

**Example Output:**
> Enter power level between 10 and 40 to shoot the ball: 40  
> You shot the ball 163.2 yards  
> You have 351.8 yards remaining  
> Enter power level between 10 and 40 to shoot the ball: 20  
> You shot the ball 40.9 yards  
> You have 310.9 yards remaining  
> Enter power level between 10 and 40 to shoot the ball: 40  
> You shot the ball 163.2 yards  
> You have 147.7 yards remaining  
> Enter power level between 10 and 40 to shoot the ball: 40  
> Finished! You got the ball in the hole  
> Your score is -1

### Exemplary

* Create a Golf game that has three holes, each hole must have a new random distance and corresponding par
    * Use a nested loop to make this more efficient. Don't just use three separate while loops.
* Use the random module to create a random distance to the hole between 100 and 650.
* Create a corresponding par related to the distance.
    * Par 3: 100 yards to 250 yards
    * Par 4: 251 yards to 450 yards
    * Par 5: 451 yards to 650 yards
* Allow the user to select a club 1) wedge 2) Iron 3) Driver.
* Create a random power level and angle for each club. Choose values that make sense
* Allow the user to shoot the ball forward or backward. Look at the shootBall() function to see how to accomplish this.
* If the user enters an incorrect club, allow them to try again
* The user completes the hole when they are within 10 yards of the hole in either direction.
* Calculate and display the users score once their ball is past the hole by taking their total shots-par
* When the user has completed all three holes, calculate their total score (The total amount above or below par)

**Example Output:**
> Choose club:

1) wedge
2) iron
3) driver   
   3  
   Type 1 to go forward or 2 to go back:
   1  
   You shot the ball 343.3 yards  
   You have -60.3 yards remaining  
   Choose club:
1) wedge
2) iron
3) driver  
   .  
   .  
   .  
   Finished! You got the ball in the hole.
   Your score on hole 1 is 1.  
   .  
   .  
   .  
   .  
   Finished! You got the ball in the hole.
   Your score on hole 2 is -1.  
   .  
   .  
   .  
   Finished! You got the ball in the hole.
   Your score on hole 3 is 1.

> You completed all the holes.
> Your total score on all holes is 1.



**To get Exemplary 2 in the course you must show understanding beyond what has been taught.**

See D2L for examples of the Turtle graphics window output.
