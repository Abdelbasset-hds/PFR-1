import turtle

color_map = {
    "orange": "orange",
    "jaune": "yellow",
    "blue": "blue",
    
}


def draw_circle(color, x, y, radius):
    turtle.penup()  
    turtle.goto(x, y - radius)  
    turtle.pendown()  
    turtle.color(color_map.get(color, "black"))  
    turtle.begin_fill() 
    turtle.circle(radius)  
    turtle.end_fill() 

def main():
    turtle.setup(width=600, height=600)
    turtle.title("Dessin des balles détectées")

    with open("result.txt", "r") as file:
        lines = file.readlines()
        cluster_count = int(lines[0].strip())  # Nombre de clusters
        for line in lines[1:]:
            color, x, y, radius = line.strip().split()
            x = int(x)
            y = int(y)
            radius = int(radius)

            draw_circle(color, x, y, radius)

    turtle.hideturtle()  
    turtle.done()  

if __name__ == "__main__":
    main()
