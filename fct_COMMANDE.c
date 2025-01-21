#include<stdio.h>
#include<string.h>
#include <ctype.h>
int filtre(char *commande,char list[100][50]){
    int i = 0; //nbr de mots;
    char *mot=strtok(commande," ");
    while (mot!=NULL){
        strncpy(list[i],mot,49);
        list[i][49]='\0';
        i++;
        if (i>=100){
            break;
        }
        mot=strtok(NULL," ");
    }
    return i;

}
int estEntier(char chaine[3]){
    int i = 0;
    for (; chaine[i] != '\0'; i++) {
        if (!isdigit(chaine[i])) {
            return 0;
        }
    }
    return 1;
}


void COMMANDE(){
    FILE *commandes; //fichier pour memoriser les commandes
    char commande[300];
    char list[100][50];
    char motCleAvancer[11][10]={"avance", "avancer", "marcher", "progresse", "va", "bouge", "vas-y", "en avant", "continue", "déplace", "allons-y"};
    char motCleTourner[4][10]={"tourner","retourner","tourne","retourne"};
    int i,j;
    printf("Entrez votre commande: ");
    fgets(commande, sizeof(commande),stdin);
    commande[strcspn(commande, "\n")]='\0';
    int nbrmot=filtre(commande,list);
    commandes = fopen("commandes.txt", "a");
    if (commandes == NULL) {
        perror("Erreur lors de l'ouverture du fichier");
        return; // Arrête la fonction si le fichier n'a pas pu être ouvert
    }
    for ( i = 0; i < nbrmot; i++){
        for ( j=0;j<11;j++){
            if ((strcmp(list[i], motCleAvancer[j]) == 0)) {
                fprintf(commandes,"%s ,","avance");
                if (i + 1 < nbrmot && estEntier(list[i+1])) {
                    fprintf(commandes,"%s ,",list[i+1]);
                }
                else if (i + 2 < nbrmot && estEntier(list[i+2])) {
                    fprintf(commandes,"%s ,",list[i+2]);
                }
                else {
                        fprintf(commandes,"%s ,","None");
                    }
            }
        }
        for ( j=0;j<4;j++){
            if ((strcmp(list[i], motCleTourner[j]) == 0)) {
                if (i + 2 < nbrmot &&strcmp(list[i + 2], "droite")==0){
                    fprintf(commandes,"%s ,","tourne_dr");
                    if (i + 3 < nbrmot && estEntier(list[i+3])) {
                        fprintf(commandes,"%s ,",list[i+3]);
                    }
                    else if (i + 4< nbrmot && estEntier(list[i+4])) {
                        fprintf(commandes,"%s ,",list[i+4]);
                    }
                    else {
                        fprintf(commandes,"%s ,","None");
                    }
                }
                else if (i + 2 < nbrmot &&strcmp(list[i + 2], "gauche")==0){
                    fprintf(commandes,"%s ,","tourne_gch");
                    if (i + 4 < nbrmot && estEntier(list[i+4])) {
                        fprintf(commandes,"%s ,",list[i+4]);
                    }
                    else if (i + 3 < nbrmot && estEntier(list[i+3])) {
                        fprintf(commandes,"%s ,",list[i+3]);
                    }
                    else {
                        fprintf(commandes,"%s ,","None");
                    }
                }
                else {
                    fprintf(commandes,"%s ,","tourne");
                    if (i + 1 < nbrmot && estEntier(list[i+1])) {
                        fprintf(commandes,"%s ,",list[i+1]);
                    }
                    else if (i + 2 < nbrmot && estEntier(list[i+2])) {
                        fprintf(commandes,"%s ,",list[i+2]);
                    }
                    else {
                        fprintf(commandes,"%s ,","None");
                    }
                }

            }
        }
    }
    fclose(commandes);
}




int main(){
    COMMANDE();
    return 0;
}
