#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../inc/color_text.h"
#include "../inc/llist.h"
#include "../inc/player.h"

// Core basic
/**
 * @brief Create a Player object.
 * 
 * @param pd the charater string representing the player
 * @return player* 
 */
player *createPlayer(char *pd){
    player *p = (player *) malloc(sizeof(player));
    strcpy(p->username, strtok(pd, "_"));
    strcpy(p->password, strtok(NULL, "_"));
    p->rank = atoi(strtok(NULL, "_"));
    p->status = 0;
    return p;
}

/**
 * @brief create a string that represent the player.
 * 
 * @param p 
 * @param buf 
 * @return int 
 */
int playerToString(player *p, char* buf){
    return sprintf(buf, "%s_%s_%d\n", p->username, p->password, p->rank);
}

/**
 * @brief read player data file and create a player list
 * 
 * @param fn name of the player data file
 * @return llist* 
 */
playerlist *loadPlayerList(char *fn){
    printGreen("Loading file: ");
    printBlue(fn);
    printf("\n");
    FILE *f = fopen(fn, "r");
    if (f == NULL){
        printRed("Could not open file ");
        printYellow(fn);
        printf("\n");
        return NULL;
    }

    char line[1024];
    playerlist *pl = NULL;

    while (fgets(line, sizeof(line), f) != NULL && strlen(line) >=1)
    {
        player *p = createPlayer(line);
        pl = addPlayerToBottom(pl, p);
    }   
    fclose(f);
    printGreen("Load file completed");
    printf("\n");
    return pl;
}

/**
 * @brief save the player list to a file
 * 
 * @param ll 
 * @param fn file to save the player list
 * @return int 
 */
int savePlayerList(playerlist *pl, char *fn){
    printGreen("Saving player list\n");
    if (pl == NULL){
        printYellow("Player list is empty\n");
        return 1;
    }
    printGreen("Opening file: ");
    printBlue(fn);
    printf("\n");
    FILE *f = fopen(fn, "w");
    if (f == NULL){
        printRed("Could not open file ");
        printYellow(fn);
        printf("\n");
        return 1;
    }

    node *n = ((llist *)pl)->top;
    player *p = (player *)n->data;
    char buf[1024];
    bzero(buf, 1024);
    do {
        playerToString(p, buf);
        fputs(buf, f);
        printGreen("saved player: ");
        printBlue(p->username);
        printf("\n");
        bzero(buf, 1024);
        n = n->nextNode;
        p = n->data;
    } while(n != ((llist *)pl)->top);
    fclose(f);
    printGreen("Saved player list\n");
    return 0;
}

/**
 * @brief add player to the bottom of the player list
 * 
 * @param pl 
 * @param p 
 * @return playerlist* 
 */
playerlist *addPlayerToBottom(playerlist *pl, player *p){
    printGreen("Adding player: ");
    printBlue(p->username);
    printf("\n");
    return (playerlist *)addNodeToBottom((llist *) pl,  (_data)p);
}

/**
 * @brief add player to the top of the player list
 * 
 * @param pl 
 * @param p 
 * @return playerlist* 
 */
playerlist *addPlayerToTop(playerlist *pl, player *p){
    printGreen("Adding player: ");
    printBlue(p->username);
    printf("\n");
    return (playerlist *)addNodeToTop((llist *) pl,  (_data)p);
}

/**
 * @brief free the player list
 * 
 * @param pl 
 */
void freePlayerList(playerlist **pl){
    freeList(pl);
}


// Core advance
int comparePlayer(player *p1, player *p2){
    // printf ("\n%s/%s\n%s-%s\n", p1->username, p2->username, p1->password, p2->password);
    if (strcmp(p1->username, p2->username)==0 && strcmp(p1->password, p2->password)==0){
        return 0;
    }
    return 1;
}

int comparePlayerByName(player *p1, player *p2){
    if (strcmp(p1->username, p2->username)==0){
        return 0;
    }
    return 1;
}

player *findPlayer(playerlist *pl, player *target, int range, int f(player *, player *)){
    node *n = findNode((llist *)pl, (_data) target, 0, (int (*)(_data, _data)) f);
    if (n==NULL){
        return NULL;
    }
    return (player *)n->data;
}

// Utils
/**
 * @brief print a player data
 * 
 * @param p 
 */
void printPlayer(_data d){
    if (d==NULL){
        printYellow("NULL\n");
        return;
    }
    player *p = (player *)d;
    printGreen("Player: ");
    char buf[1024];
    bzero(buf, 1024);
    playerToString(p, (char *)buf);
    printf("%s", buf);
}

void printPlayerList(playerlist *pl){
    printGreen("Printing player list\n");
    printList((llist *)pl, printPlayer);
}