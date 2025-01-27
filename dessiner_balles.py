import turtle

color_map = {
    "orange": "orange",
    "jaune": "yellow",
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
    """
    Convertit les coordonnées de Processing (0,0 en haut à gauche)
    en coordonnées de Turtle (0,0 au centre).
    """
    converted_x = x - screen_width // 2
    converted_y = screen_height // 2 - y
    return converted_x, converted_y

def main():
    # Dimensions de l'écran Turtle
    screen_width = 300
    screen_height = 300

    # Étape 2 : Configurer Turtle
    turtle.setup(width=screen_width, height=screen_height)
    turtle.title("Turtle avec image de fond")

    # Définir l'image de fond (remplacer par le chemin de l'image GIF)
    turtle.bgpic("IMG_5390.gif")

    # Étape 3 : Lire les clusters depuis le fichier result.txt
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

if __name__ == "__main__":
    main()
