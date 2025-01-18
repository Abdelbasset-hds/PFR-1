#include <stdio.h>
#include <stdlib.h>

/**
 * Lit le contenu d'un fichier texte et le charge dans une chaîne de caractères.
 * La chaîne retournée est terminée par un caractère nul ('\0') pour être compatible
 * avec les fonctions standard de manipulation de chaînes en C.
 *
 * @param chemin_fichier Chemin d'accès au fichier à lire.
 * @return Un pointeur vers une chaîne de caractères contenant le contenu du fichier.
 *         Retourne NULL en cas d'erreur (fichier introuvable, problème de mémoire, etc.).
 *         La mémoire allouée doit être libérée par l'appelant à l'aide de 'free'.
 */
char* lire_fichier(const char* chemin_fichier) {
    FILE* fichier = fopen(chemin_fichier, "r");
    if (fichier == NULL) {
        perror("Erreur lors de l'ouverture du fichier.");
        return NULL;
    }

    // Déplacement à la fin du fichier pour déterminer sa taille.
    fseek(fichier, 0, SEEK_END);
    const long taille_fichier = ftell(fichier);
    rewind(fichier);

    char* contenu = malloc((taille_fichier + 1) * sizeof(char));
    if (contenu == NULL) {
        perror("Erreur d'allocation mémoire.");
        fclose(fichier);
        return NULL;
    }

    // Lecture du fichier dans le tampon.
    const size_t nb_lus = fread(contenu, 1, taille_fichier, fichier);
    if (nb_lus != taille_fichier) {
        perror("Erreur lors de la lecture du fichier.");
        free(contenu);
        fclose(fichier);
        return NULL;
    }

    // Ajout du caractère nul pour terminer la chaîne.
    contenu[taille_fichier] = '\0';

    fclose(fichier);
    return contenu;
}

/**
 * Écrit une chaîne de caractères dans un fichier texte.
 *
 * @param chemin_fichier Chemin vers le fichier dans lequel écrire.
 * @param contenu Chaîne de caractères à écrire dans le fichier.
 * @return 0 en cas de succès, -1 en cas d'erreur.
 */
int écrire_dans_fichier(const char* chemin_fichier, const char* contenu) {
    FILE* fichier = fopen(chemin_fichier, "w");
    if (!fichier) {
        perror("Erreur lors de la création du fichier.");
        return -1;
    }

    fprintf(fichier, "%s", contenu);
    fclose(fichier);

    return 0;
}

/**
 * Quantifie un pixel RGB en combinant les 2 bits les plus significatifs
 * de chaque composante couleur (Rouge, Vert, Bleu).
 * Cette quantification permet de limiter les calculs et de réduire les données
 * en ne retenant que les deux premières puissances de 2 pour chaque intensité.
 *
 * @param R Composante rouge du pixel (entier entre 0 et 255).
 * @param G Composante verte du pixel (entier entre 0 et 255).
 * @param B Composante bleue du pixel (entier entre 0 et 255).
 * @return Une valeur entière représentant la quantification
 *         en combinant les 6 bits (2 bits par composante).
 *         Résultat entre 0 et 63.
 */
int quantifier_pixel(const int R, const int G, const int B) {
    const int R1 = (R & 128) >> 2;
    const int R2 = (R & 64) >> 2;
    const int G1 = (G & 128) >> 4;
    const int G2 = (G & 64) >> 4;
    const int B1 = (B & 128) >> 6;
    const int B2 = (B & 64) >> 6;

    return R1 | R2 | G1 | G2 | B1 | B2;
}

/**
 * Quantifie un pixel RGB en combinant les n bits les plus significatifs
 * de chaque composante couleur (Rouge, Vert, Bleu).
 * Cette quantification permet de limiter les calculs et de réduire les données
 * en ne retenant que les premières puissances de 2 pour chaque intensité.
 *
 * @param R Composante rouge du pixel (entier entre 0 et 255).
 * @param G Composante verte du pixel (entier entre 0 et 255).
 * @param B Composante bleue du pixel (entier entre 0 et 255).
 * @param n Nombre de bits significatifs à utiliser pour chaque composante (entier positif, 1 ≤ n ≤ 8).
 * @return Une valeur entière représentant la quantification
 *         en combinant les n bits de chaque composante.
 *         Résultat entre 0 et 2^(3n) - 1.
 */
int quantifier_pixel_n(const int R, const int G, const int B, const int n) {
    if (n < 1 || n > 8) {
        fprintf(stderr, "Erreur : le nombre de bits significatifs (n) doit être entre 1 et 8.\n");
        exit(EXIT_FAILURE);
    }

    const int mask = (1 << n) - 1;
    const int R_quant = (R >> (8 - n)) & mask;
    const int G_quant = (G >> (8 - n)) & mask;
    const int B_quant = (B >> (8 - n)) & mask;

    return (R_quant << (2 * n)) | (G_quant << n) | B_quant;
}

/**
 * Quantifie une image RGB en réduisant les données de chaque pixel à une valeur entière.
 * Cette fonction lit les métadonnées de l'image (dimensions et nombre de canaux),
 * puis parcourt chaque pixel pour appliquer la quantification
 * (voir description de la fonction quantifier_pixel).
 *
 * La chaîne d'entrée doit être formatée avec les métadonnées et les pixels sous forme
 * d'entiers séparés par des espaces, dans l'ordre suivant
 * - Largeur Hauteur Canaux
 * - R G B (pour chaque pixel, répétée largeur * hauteur fois).
 *
 * Exemple d'entrée :
 * "300 300 3\n182 186 189 190 188 187 ..."
 *
 * La sortie est une chaîne de caractères contenant
 * - Les dimensions de l'image (largeur et hauteur).
 * - Les pixels quantifiés (une valeur entière par pixel, séparée par des espaces).
 *
 * Exemple de sortie :
 * "300 300\n63 15 3 ..."
 *
 * @param image Chaîne de caractères représentant l'image en entrée.
 *              Doit contenir les métadonnées et les valeurs RGB de chaque pixel.
 * @return Une chaîne de caractères représentant l'image quantifiée.
 *         Retourne NULL en cas d'erreur (mauvais format, problème mémoire, etc.).
 *         La mémoire allouée doit être libérée par l'appelant avec 'free'.
 */
char* quantifier_image(const char* image) {
    // Lis-les métadonnées.
    char* curseur_image;
    const int largeur = strtol(image, &curseur_image, 10);
    const int hauteur = strtol(curseur_image, &curseur_image, 10);
    const int canaux = strtol(curseur_image, &curseur_image, 10);
    if (canaux != 3) {
        perror("L'image n'est pas au format RGB.");
        return NULL;
    }

    // Calcule la taille estimée de la chaîne résultat en prenant en compte
    // les dimensions et pixels (deux chiffres max) avec les espaces.
    const int taille_résultat = 10 + largeur * hauteur * 3;
    char* résultat = malloc(taille_résultat);
    if (!résultat) {
        perror("Erreur d'allocation mémoire.");
        return NULL;
    }

    // Ajoute les dimensions à la chaîne résultat.
    char* curseur_résultat = résultat;
    curseur_résultat += sprintf(curseur_résultat, "%d %d\n", largeur, hauteur);

    // Lis-les pixels et les quantifie
    for (int i = 0; i < largeur * hauteur / 3; i++) {
        const int R = strtol(curseur_image, &curseur_image, 10);
        const int G = strtol(curseur_image, &curseur_image, 10);
        const int B = strtol(curseur_image, &curseur_image, 10);

        const int pixel_quantifié = quantifier_pixel_n(R, G, B, 3);

        // Ajouter le pixel quantifié à la chaîne résultat
        curseur_résultat += sprintf(curseur_résultat, "%d ", pixel_quantifié);

        if (pixel_quantifié < 100) {
            curseur_résultat += sprintf(curseur_résultat, " ");
        }
        if (pixel_quantifié < 10) {
            curseur_résultat += sprintf(curseur_résultat, " ");
        }

        // Ajouter un saut de ligne après chaque ligne complète
        if ((i + 1) % (largeur / 3) == 0) {
            *(curseur_résultat - 1) = '\n'; // Remplace l'espace par un saut de ligne
        }
    }

    // Remplace le dernier espace par un saut de ligne
    *(curseur_résultat - 1) = '\n';

    return résultat;
}

int main() {
    char* image = lire_fichier("../IMG_300/IMG_5390.txt");

    // Quantifier l'image
    char* résultat = quantifier_image(image);

    free(image);

    // Afficher le résultat
    if (résultat) {
        écrire_dans_fichier("../histogramme.txt", résultat);
        free(résultat);  // Libérer la mémoire allouée
    }

    return 0;
}