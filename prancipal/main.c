#include <stdlib.h>
#include <stdio.h>

int main() {
    // Utiliser un chemin relatif pour accéder au script Python
    const char *script_name = "../fonction_dd/fnc_de_deplacement.py"; // Chemin relatif

    // Construire la commande pour exécuter le script
    char command[256]; // Assurez-vous que la taille est suffisante
    snprintf(command, sizeof(command), "python \"%s\"", script_name);

    // Exécuter le script Python
    system(command);
    return 0;
}