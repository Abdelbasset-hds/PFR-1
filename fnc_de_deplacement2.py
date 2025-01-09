import turtle
import math
import os
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import filtre2






def environnement(taill_environnement) :
       coin_hd = (taill_environnement / 2,taill_environnement / 2)
       robot.hideturtle()
       robot.up()
       robot.goto(coin_hd)
       robot.down()
       robot.pensize(5)
       robot.pencolor("blue")
       robot.speed(10)
       for i in range (4) :
            robot.right(90)
            robot.forward(taill_environnement)
       robot.up()
       robot.home()
       robot.down()  
       robot.pensize(2)
       robot.pencolor("black")
       robot.speed(1)
       robot.showturtle()
       
       
def rotate_image(filename, angle):
    if not os.path.exists(filename):
        print(f"Erreur : Le fichier '{filename}' est introuvable.")
        return None
    img = Image.open(filename)
    rotated_img = img.rotate(angle, expand=True)
    rotated_filename = "rotated.gif"  # Define the filename for saving
    rotated_img.save(rotated_filename)  # Save the rotated image
    return rotated_filename

def afficher_message(message) :
    message_label.config(text=message)

def deplacement() :
      commande = entry_commande.get()
      commande_filtre = filtre2.filtre(commande)
      if not commande :
          afficher_message("veuillez entrer une commande")
          return
      afficher_message(f"commande reçue {commande_filtre}")
      for i in range (0,len(commande_filtre),2) :
        if commande_filtre[i+1] is None :
                 afficher_message("vous dever specifier la valeur de l'action ")  
                 break
                 
        
        if commande_filtre[i] == "avance" :
            if abs(commande_filtre[i+1]*math.cos(math.radians(robot.heading())) + robot.xcor()) > 235    or  abs(commande_filtre[i+1]*math.sin(math.radians(robot.heading())) + robot.ycor()) > 235 :
              afficher_message("***Hors des limites***") 
              print(abs(commande_filtre[i+1]*math.cos(math.radians(robot.heading())) + robot.xcor()) + abs(robot.xcor()) , abs(commande_filtre[i+1]*math.sin(math.radians(robot.heading())) + robot.ycor()))
              break
            else :
                  robot.forward(commande_filtre[i+1])
        elif commande_filtre[i] == "tourne_gch" :
            new_heading = (robot.heading() + commande_filtre[i+1]) % 360
            robot.setheading(new_heading)
            rotated_image = rotate_image(r"C:\\Users\\Abdo\\Desktop\\PFR_1\\fonction_dd\\voiture2.gif", new_heading)
            if rotated_image:
                turtle_screen.addshape(rotated_image)  # Register the rotated image as a shape
                robot.shape(rotated_image)
            
        elif commande_filtre[i] == "tourne_dr" :
            new_heading = (robot.heading() - commande_filtre[i+1]) % 360
            robot.setheading(new_heading)
            rotated_image = rotate_image(r"C:\\Users\\Abdo\\Desktop\\PFR_1\\fonction_dd\\voiture2.gif", new_heading)
            if rotated_image:
                turtle_screen.addshape(rotated_image)  # Register the rotated image as a shape
                robot.shape(rotated_image)
            
                 
                    
      print(robot.heading())  

root = tk.Tk()
root.title("PFR 1")
root.geometry("1280x720") 

frame_turtle=tk.Frame(root,width=850,height=720,bg="white")
frame_turtle.pack(side = "left" ,fill="both",expand=True)

frame_commande=tk.Frame(root,width=330,height=720,bg="dodgerblue2")
frame_commande.pack(side="right",fill="both",expand=True)

canvas=tk.Canvas(frame_turtle,width=850,height=720)
canvas.pack(fill="both",expand=True)

turtle_screen = turtle.TurtleScreen(canvas)
turtle_screen.bgcolor("white")
robot = turtle.RawTurtle(turtle_screen)

voiture = r"C:\\Users\\Abdo\\Desktop\\PFR_1\\fonction_dd\\voiture2.gif"
if os.path.exists(voiture) :
     turtle_screen.addshape(voiture)
     robot.shape(voiture)
else :
     print(f"l'image {voiture} est introuvable")     

     
spicify_font = font.Font(family = "Times New Roman",weight="bold",size=14)
tk.Label(frame_commande, text="Entez votres commandes", font=spicify_font,bg ="dodgerblue2",fg="white").pack(pady=20)


entry_commande = tk.Entry(frame_commande, width = 50, font=("Ariel",10))
entry_commande.pack(pady=20)
tk.Button(frame_commande, text="valider",command=deplacement).pack(pady=20)
tk.Label(frame_commande, text="Commontaire", font=spicify_font,bg ="dodgerblue2",fg="white").pack(pady=40)
message_label = tk.Label(frame_commande,text="",font=("Ariel",10),fg="red",bg="white",width=40,height=5,pady=2,wraplength=280)
message_label.pack(pady=2)

environnement(500)

root.mainloop()

    