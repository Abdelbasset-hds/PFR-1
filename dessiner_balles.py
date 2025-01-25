import turtle

def draw_ball(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def main():
    with open('C:/Users/hp/Desktop/final/result.txt', 'r') as file:
        lines = file.readlines()
    
    num_balls = int(lines[0].strip())
    
    turtle.title("Dessiner les balles")
    turtle.speed(0)
    turtle.hideturtle()

    for i in range(1, num_balls + 1):
        color, x, y, radius = lines[i].strip().split()
        x, y, radius = int(x), int(y), int(radius)
        draw_ball(color, x, y, radius)

    turtle.done()

if __name__ == "__main__":
    main()