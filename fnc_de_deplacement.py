import turtle
import math
import environnement
import filter


robot = turtle.Turtle() 


environnement.environnement(500)

   
robot.pensize(2)
robot.pencolor("black")
robot.speed(1)



while True :
      commande = input("entrer la commande : ")
      commande_filtre = filter.filtre(commande)
      print(commande_filtre)
      for i in range (0,len(commande_filtre),2) :
        if commande_filtre[i+1] is None :
                 print("vous dever specifier la valeur de l'action ")  
                 break
                 
        
        if commande_filtre[i] == "avance" :
            if abs(commande_filtre[i+1]*math.cos(math.radians(robot.heading())) + robot.xcor()) > 200    or  abs(commande_filtre[i+1]*math.sin(math.radians(robot.heading())) + robot.ycor()) > 200 :
              print("***out door***") 
              print(abs(commande_filtre[i+1]*math.cos(math.radians(robot.heading())) + robot.xcor()) + abs(robot.xcor()) , abs(commande_filtre[i+1]*math.sin(math.radians(robot.heading())) + robot.ycor()))
              break
            else :
                  robot.forward(commande_filtre[i+1])
        elif commande_filtre[i] == "tourne_gch" :
                 robot.left(commande_filtre[i+1])
        elif commande_filtre[i] == "tourne_dr" :
                 robot.right(commande_filtre[i+1])   
      print(robot.heading())     
turtle.done()      