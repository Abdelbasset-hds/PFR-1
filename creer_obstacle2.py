import turtle

def dessiner_obstacle(fichier): 
    # oouvrir le fichier pour lire les donnees
    with open(fichier, 'r') as f:
        
        largeur, hauteur = map(int, f.readline().split())
        
        pixels = []
        for ligne in f:
            pixels.extend(map(int, ligne.split()))
    
   
    screen = turtle.Screen()
    screen.bgcolor("white")  # Fond de la fenêtre

   
    obstacle = turtle.Turtle()
    obstacle.shape("turtle")
    obstacle.speed(0)  
    obstacle.penup() 

    
    taille_pixel = 20  

    x_start = -largeur * taille_pixel / 2
    y_start = hauteur * taille_pixel / 2

    obstacle.setposition(x_start, y_start)

    for i in range(hauteur):
        for j in range(largeur):
            pixel_valeur = pixels[i * largeur + j]

            couleur = (pixel_valeur / 63, pixel_valeur / 63, pixel_valeur / 63)  
            
            obstacle.goto(x_start + j * taille_pixel, y_start - i * taille_pixel)

            obstacle.fillcolor(couleur)  
            obstacle.begin_fill()
            obstacle.circle(taille_pixel / 2) 
            obstacle.end_fill()

    obstacle.hideturtle()

    turtle.done()

dessiner_obstacle("histogramme.txt")

