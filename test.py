import turtle
import math
import os
import tkinter as tk
from tkinter import font, filedialog
import speech_recognition as sr
from PIL import Image, ImageTk


# Dictionnaire de couleurs
color_map = {
    "orange": "orange",
    "yellow": "yellow",
    "blue": "blue",
}

def draw_circle(color, x, y, radius):
    """Dessine un cercle à une position donnée avec une couleur et un rayon."""
    turtle.penup()
    turtle.goto(x, y - radius)  # Positionner en bas du cercle
    turtle.pendown()
    turtle.color(color_map.get(color, "black"))  # Utilise la couleur correspondante ou noir par défaut
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def convert_coordinates(x, y, screen_width, screen_height):
    """Convertit les coordonnées de Processing en coordonnées de Turtle."""
    converted_x = x - screen_width // 2
    converted_y = screen_height // 2 - y
    return converted_x, converted_y

def afficher_message(message):
    message_label.config(text=message)

def deplacement():
    commande = entry_commande.get()
    if not commande:
        afficher_message("Veuillez entrer une commande")
        return
    # Placeholder pour la logique de déplacement (à adapter selon vos besoins)
    afficher_message(f"Commande reçue : {commande}")

def analyser_image():
    # Ouvrir une boîte de dialogue pour sélectionner une image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.gif")])
    if file_path:
        # Traitement de l'image ici (si nécessaire)
        afficher_message(f"Image sélectionnée : {file_path}")

def main():
    # Dimensions de l'écran Turtle
    screen_width = 600
    screen_height = 600

    # Configurer Turtle
    turtle.setup(width=screen_width, height=screen_height)
    turtle.title("Turtle avec image de fond")

    # Lire les clusters depuis le fichier result.txt
    if os.path.exists("result.txt"):
        with open("result.txt", "r") as file:
            lines = file.readlines()
            for line in lines[1:]:
                color, x, y, radius = line.strip().split()
                x = int(x)
                y = int(y)
                radius = int(radius)

                # Conversion des coordonnées
                x, y = convert_coordinates(x, y, screen_width, screen_height)

                # Dessiner le cercle
                draw_circle(color, x, y, radius)

    turtle.hideturtle()  # Masquer le curseur
    turtle.done()

# Interface Tkinter
root = tk.Tk()
root.title("Interface Graphique")
root.geometry("800x600")

frame_commande = tk.Frame(root, bg="dodgerblue2")
frame_commande.pack(side="right", fill="y")

spicify_font = font.Font(family="Times New Roman", weight="bold", size=14)
tk.Label(frame_commande, text="Entrez vos commandes", font=spicify_font, bg="dodgerblue2", fg="white").pack(pady=20)

entry_commande = tk.Entry(frame_commande, width=50, font=("Arial", 10))
entry_commande.pack(pady=20)
tk.Button(frame_commande, text="Valider", command=deplacement).pack(pady=20)
tk.Button(frame_commande, text="Analyser une image", command=analyser_image).pack(pady=10)

message_label = tk.Label(frame_commande, text="", font=("Arial", 10), fg="red", bg="white", width=40, height=5, pady=2)
message_label.pack(pady=2)

# Créer le canevas Turtle
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(side="left", fill="both", expand=True)

turtle_screen = turtle.TurtleScreen(canvas)
turtle_screen.bgcolor("white")

# Lancez la fonction principale pour dessiner
main()

root.mainloop()
