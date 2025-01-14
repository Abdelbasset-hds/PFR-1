#include"fctFiltrer.c"
int COMMANDE(){
    FILE *commandes; //fichier pour memoriser les commandes
    char commande[300];
    char list[100][50];
    char motCle[1000][100] = {"avance", "avancer", "marcher", "progresse", "va", "bouge", "vas-y", "en avant", "continue", "déplace", "allons-y"
    "tourner","retourner","tourne","retourne","gauche","droite","balle","cube","cercle","carré","rouge","bleu","vert","jaune","noir"};

    printf("Entrez votre commande: ");
    fgets(commande, sizeof(commande),stdin);
    commande[strcspn(commande, "\n")]='\0';
    int nbrmot=filtre(commande,list);
    fopen("C:\\commandes.txt","a");
    for (int i = 0; i < nbrmot; i++){
        for (int j=0;j<27;j++){
            if ((strcmp(list[i], motCle[j]) == 0) || isdigit(list[i][0])) {
                fprintf(commandes,"%s",list[i]);

            }
        }
        
    }
    fclose(commandes);
    return 0;
}