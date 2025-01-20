import turtle

def cree_obstacle(x, y, diametre, couleur):
    
    turtle.penup()  
    turtle.goto(x, y)  
    turtle.pendown()  
    turtle.color(couleur)  
    turtle.begin_fill()  
    turtle.circle(diametre / 2)  
    turtle.end_fill()  

# Exemple d'utilisation
if __name__ == "__main__":
    turtle.speed(1)  
    cree_obstacle(5, 6, 50, "red")  
    cree_obstacle(100, 100, 30, "blue")  
    turtle.done() 