import turtle

def create_obstacle(x, y, width, height, shape, color):
    
    turtle.penup()  
    turtle.goto(x, y)  
    turtle.pendown()  

    turtle.fillcolor(color)  
    turtle.begin_fill()  

    if shape == 'C':
        turtle.circle(width / 2)  
    elif shape == 'S':
        for _ in range(4):
            turtle.forward(width)  
            turtle.right(90)
    elif shape == 'R':
        for _ in range(2):
            turtle.forward(width)  
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)

    turtle.end_fill()  

# Exemple d'utilisation
if __name__ == "__main__":
    turtle.speed(1)  

    create_obstacle(0, 0, 100, 100, 'S', 'red')  # Un carré rouge
    create_obstacle(-200, 0, 50, 50, 'C', 'blue')  # Un cercle bleu
    create_obstacle(200, 0, 150, 100, 'R', 'green')  # Un rectangle vert

    turtle.done()  