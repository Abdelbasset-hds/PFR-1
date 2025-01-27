import turtle
import math
import os
import tkinter as tk
import speech_recognition as sr
from tkinter import font
from PIL import Image, ImageTk
import shutil
from tkinter import filedialog, font 
import filtre
import subprocess



def reconaitre_la_voie () :
    recognizer = sr.Recognizer()
    with sr.Microphone() as source :
        afficher_message("parler je vous ecoute")
        try :
            audio = recognizer.listen(source , timeout= 5)
            text = recognizer.recognize_google(audio , language="fr-FR")
            entry_commande.delete(0,tk.END)
            entry_commande.insert(0,text)
            
        except sr.WaitTimeoutError : 
            afficher_message("aucun son detecté")
        except sr.UnknownValueError :
            afficher_message("Désolé je n'est pas compris")
        except sr.RequestError as e :
            afficher_message(f"Erreur avec le service de reconnaissance vocale : {e}")   




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

def analyser_image():
    # Ouvrir une boîte de dialogue pour sélectionner une image
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        executer_main2(file_path)





def afficher_message(message) :
    message_label.config(text=message)

def executer_main2(image_path):
    # Vérifiez que l'image existe
    if not os.path.exists(image_path):
        afficher_message(f"Erreur : L'image {image_path} est introuvable.")
        return
    
    # Définir le chemin vers l'exécutable main_ti dans le répertoire build
    current_directory = os.path.dirname(__file__)  # Répertoire actuel du script
    build_directory = os.path.join(current_directory, "../build")
    chemin_executable = os.path.join(build_directory, "main_ti.exe")  # Chemin relatif vers main_ti
    
    if not os.path.exists(chemin_executable):
        afficher_message("Erreur : L'exécutable 'main_ti' est introuvable. Compilez d'abord le code C.")
        return

    # Copier le fichier sélectionné dans le répertoire build
    try:
        fichier_destination = os.path.join(build_directory, os.path.basename(image_path))
        shutil.copy(image_path, fichier_destination)
    except Exception as e:
        afficher_message(f"Erreur lors de la copie du fichier dans le répertoire 'build' : {e}")
        return
    
    try:
        # Exécuter main_ti avec le fichier copié
        resultat = subprocess.run(
            [chemin_executable, os.path.basename(image_path)],
            text=True,
            capture_output=True,
            cwd=build_directory  # Change le répertoire courant pour build
        )
        
        # Vérifiez si main_ti s'est exécuté correctement
        if resultat.returncode == 0:
            afficher_message("Analyse d'image terminée.")
            lire_resultats()
        else:
            afficher_message(f"Erreur lors de l'exécution :\n{resultat.stderr}")
    except Exception as e:
        afficher_message(f"Erreur : {e}")


def lire_resultats():
    # Chemin vers le fichier result.txt
    result_path = os.path.join(current_directory, "../../result.txt")
    
    if not os.path.exists(result_path):
        afficher_message("Erreur : Le fichier 'result.txt' est introuvable.")
        return
    
    try:
        # Lire le contenu de result.txt et l'afficher
        with open(result_path, "r") as file:
            contenu = file.read()
            afficher_message(f"Résultats de l'analyse :\n{contenu}")
    except Exception as e:
        afficher_message(f"Erreur lors de la lecture des résultats : {e}")


def deplacement() :
      commande = entry_commande.get()
      commande_filtre = filtre.filtre(commande)
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
            rotated_image = rotate_image(voiture, new_heading)
            if rotated_image:
                turtle_screen.addshape(rotated_image)  # Register the rotated image as a shape
                robot.shape(rotated_image)
            
        elif commande_filtre[i] == "tourne_dr" :
            new_heading = (robot.heading() - commande_filtre[i+1]) % 360
            robot.setheading(new_heading)
            rotated_image = rotate_image(voiture, new_heading)
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

current_directory = os.path.dirname(os.path.abspath(__file__))

# Construire le chemin relatif pour l'image
voiture = os.path.join(current_directory, "voiture.gif")
#voiture = r"fonction_dd\\voiture.gif"
if os.path.exists(voiture) :
     turtle_screen.addshape(voiture)
     robot.shape(voiture)
else :
     print(f"l'image {voiture} est introuvable")     

     
spicify_font = font.Font(family = "Times New Roman",weight="bold",size=14)
tk.Label(frame_commande, text="Entez votres commandes", font=spicify_font,bg ="dodgerblue2",fg="white").pack(pady=20)

tk.Button(frame_commande,text="vocale",command=reconaitre_la_voie).pack(pady=10)
entry_commande = tk.Entry(frame_commande, width = 50, font=("Ariel",10))
entry_commande.pack(pady=20)
tk.Button(frame_commande, text="valider",command=deplacement).pack(pady=20)
tk.Label(frame_commande, text="Commontaire", font=spicify_font,bg ="dodgerblue2",fg="white").pack(pady=40)
message_label = tk.Label(frame_commande,text="",font=("Ariel",10),fg="red",bg="white",width=40,height=10,pady=2,wraplength=280)
message_label.pack(pady=2)

tk.Button(frame_commande, text="Analyser une image", command=analyser_image).pack(pady=10)
environnement(500)

root.mainloop()

    