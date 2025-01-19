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
    char motCleTournerDroite[4][17]={"tourner à droite","tourner a droite","tourne à droite","tourne a droite"};
    char motCleTournerGauche[4][17]={"tourner à gauche","tourner a gauche","tourne à gauche","tourne a gauche"};

    printf("Entrez votre commande: ");
    fgets(commande, sizeof(commande),stdin);
    commande[strcspn(commande, "\n")]='\0';
    int nbrmot=filtre(commande,list);
    fopen("C:\\commandes.txt","a");
    for (int i = 0; i < nbrmot; i++){
        for (int j=0;j<11;j++){
            if ((strcmp(list[i], motCleAvancer[j]) == 0)) {
                fprintf(commandes,"%s ,","avance");
                if (estEntier(list[i+1])) {
                    fprintf(commandes,"%s ,",list[i+1]);
                }
                else if (estEntier(list[i+2])) {
                    fprintf(commandes,"%s ,",list[i+2]);
                }
            }
        }
        for (int j=0;j<4;j++){
            if ((strcmp(list[i], motCleTourner[j]) == 0)) {
                fprintf(commandes,"%s ,","tourne");
                if (estEntier(list[i+1])) {
                    fprintf(commandes,"%s ,",list[i+1]);
                }
                else if (estEntier(list[i+2])) {
                    fprintf(commandes,"%s ,",list[i+2]);
                }
                else {
                    fprintf(commandes,"%s ,","None");
                }
            }
        }
        for (int j=0;j<4;j++){
            if ((strcmp(list[i], motCleTournerGauche[j]) == 0)) {
                fprintf(commandes,"%s ,","tourne_gch");
                if (estEntier(list[i+1])) {
                    fprintf(commandes,"%s ,",list[i+1]);
                }
                else if (estEntier(list[i+2])) {
                    fprintf(commandes,"%s ,",list[i+2]);
                }
                else {
                    fprintf(commandes,"%s ,","None");
                }
            }
        }
        for (int j=0;j<4;j++){
            if ((strcmp(list[i], motCleTournerDroite[j]) == 0)) {
                fprintf(commandes,"%s ,","tourne_dr");
                if (estEntier(list[i+1])) {
                    fprintf(commandes,"%s ,",list[i+1]);
                }
                else if (estEntier(list[i+2])) {
                    fprintf(commandes,"%s ,",list[i+2]);
                }
                else {
                    fprintf(commandes,"%s ,","None");
                }
            }
        }
        
        
    }
    fclose(commandes);
}




int main(){
    COMMANDE();
}