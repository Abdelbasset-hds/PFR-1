import turtle


def environnement(taill_environnement) :
       coin_hd = (taill_environnement / 2,taill_environnement / 2)
       turtle.hideturtle()
       turtle.up()
       turtle.goto(coin_hd)
       turtle.down()
       turtle.pensize(5)
       turtle.pencolor("blue")
       turtle.speed(10)
       for i in range (4) :
            turtle.right(90)
            turtle.forward(taill_environnement)
       turtle.up()
       turtle.home()
       turtle.down()  
       turtle.showturtle()
          
