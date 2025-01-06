#include"fctFiltrer.c"
int main(){
    char commande[300];
    char list[100][50];
    printf("Entrez votre commande: ");
    fgets(commande, sizeof(commande),stdin);
    commande[strcspn(commande, "\n")]='\0';
    int nbrmot=filtre(commande,list);
    for (int i = 0; i < nbrmot; i++){
        printf("Mot %d: %s\n", i + 1,list[i]);
    }

    return 0;


}