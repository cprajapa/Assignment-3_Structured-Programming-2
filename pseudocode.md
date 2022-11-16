	DECLARE direction<-input("Type1togoforwardor2togoback:") : STRING
	DECLARE club<-input("Selectclub:") : STRING
	// See the README file FOR how to use the golf module  //Pseudocode can't handle this
	
	FOR i 0 TO 3
	NEXT
	
	    from Golf import Golf
	    import random
	
	    golf<-Golf()
	
	    distance<-random.randint(100, 650)
	
	    golf.drawHole(distance)
	
	    IF distance >= 100 and distance <= 250
	    THEN
	
	        par<-3
	
	        golf.drawText("Hole 1: Par 3, " + str(distance) + " yards")
	
	    elif distance >= 251 and distance <= 450:  //You will need to change this to CASE OF
	
	        par<-4
	
	        golf.drawText("Hole 1: Par 4, " + str(distance) + " yards")
	
	    elif distance >= 451 and distance <= 650:  //You will need to change this to CASE OF
	
	        par<-5
	
	        golf.drawText("Hole 1: Par 5, " + str(distance) + " yards")
			ENDIF
	
	    totalShots<-0
	    WHILE distance > 10:
	
	        wedge<-"1"
	        iron<-"2"
	        driver<-"3"
	
	        OUTPUT
	        OUTPUT wedge + " Wedge"
	        OUTPUT iron + " Iron"
	        OUTPUT driver + " Driver"
	        OUTPUT
	
	INPUT club<-input("Selectclub:")
	
	        OUTPUT
	
	        forward<-"1"
	        back<-"2"
	
	INPUT direction<-input("Type1togoforwardor2togoback:")
	
	        IF direction = forward
	        THEN
	
	            IF club = wedge  // lower power, higher angle/loft
	                THEN
	                powerLevel<-random.randint(11, 20)
	                angle<-random.randint(60, 80)
	            elif club = iron:  // medium power, medium angle/loft  //You will need to change this to CASE OF
	                powerLevel<-random.randint(21, 30)
	                angle<-random.randint(45, 59)
	            elif club = driver:  // higher power, lower angle/loft  //You will need to change this to CASE OF
	                powerLevel<-random.randint(31, 40)
	                angle<-random.randint(30, 44)
	            ELSE
	                OUTPUT "Select the correct club:"
						ENDIF
			
	        IF direction = back
	        THEN
	
	            IF club = wedge  // lower power, higher angle/loft
	                THEN
	                powerLevel<-random.randint(-20, -11)
	                angle<-random.randint(60, 80)
	            
	            elif club = iron:  // medium power, medium angle/loft  //You will need to change this to CASE OF
	                powerLevel<-random.randint(-30, -21)
	                angle<-random.randint(45, 59)
	            elif club = driver:  // higher power, lower angle/loft  //You will need to change this to CASE OF
	                powerLevel<-random.randint(-40, -31)
	                angle<-random.randint(30, 44)
	            ELSE
	                OUTPUT "Select the correct club:"
	
	        ELSE
	            OUTPUT "Select the correct direction:"
					ENDIF
	        shot<-golf.shootBall(powerLevel, angle)
	        distance -= shot
	        totalShots += 1
	ENDWHILE
	        OUTPUT
	
	        OUTPUT "You shot the ball " + str(round(shot, 1 + " yards"
	        OUTPUT
	
	        OUTPUT "You have " + str(round(distance, 1 + " yards remaining"
	        OUTPUT
	
	    OUTPUT "Finished! You got the ball in the hole"
	    OUTPUT
	
	    OUTPUT "Your score is " + str(totalShots - par
	    OUTPUT
	
	    golf.clearScreen()

ENDFOR