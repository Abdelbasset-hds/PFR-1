import turtle
def executer_commande_simple(texte):
    texte = texte.lower()
    if texte == "avance":
        turtle.forward(100)
    elif texte == "recule":
        turtle.backward(100)
    elif texte == "tourne à gauche":
        turtle.left(90)
    elif texte == "tourne à droite":
        turtle.right(90)
    elif texte == "arrête":
        print("Robot arrêté.")
    else:
        print("Commande non reconnue :", texte)

def main():
    turtle.setup(800, 600)
    turtle.speed(1)
    print("Entrez des commandes simples : 'avance', 'recule', 'tourne à gauche', 'tourne à droite', 'arrête'.")
    print("Tapez 'quit' pour arrêter.")
    while True:
        texte = input("Requête : ")
        if texte.lower() == 'quit':
            break
        executer_commande_simple(texte)
    turtle.done()
main()