#include<stdio.h>
#include<string.h>
int filtre(char *commande,char list[100][50]){
    int i = 0; //nbr de mots;
    char *mot=strtok(commande," ");
    while (mot!=NULL){
        strncpy(list[i],mot,49);
        list[100][49]='\0';
        i++;
        if (i>=100){
            break;
        }
        mot=strtok(NULL," ");
    }
    return i ;

}
