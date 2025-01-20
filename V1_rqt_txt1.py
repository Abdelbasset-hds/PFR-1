import turtle

commandes_avancer = ["avance", "avancer", "marcher", "progresse", "va", "bouge", "vas-y", "en avant", "continue", "déplace", "allons-y"]
commandes_tourner_gauche = ["tourne à gauche", "retourne à gauche", "tourner à gauche"]
commandes_tourner_droite = ["tourne à droite", "retourne à droite", "tourner à droite"]

def executer_commande_simple(texte):
    texte = texte.lower()
    if texte in commandes_avancer:
        turtle.forward(100)
    elif texte == "recule":
        turtle.backward(100)
    elif texte in commandes_tourner_gauche:
        turtle.left(90)
    elif texte in commandes_tourner_droite:
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
