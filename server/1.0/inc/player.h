#ifndef __PLAYER_H
#define __PLAYER_H_

#include "llist.h"

typedef struct _player
{
    char username[50];
    char password[50];
    int rank;

    int deck_id;

    int status; // Game connection status, 0: offline, 1: online, 2: ingame

} player;

typedef llist playerlist;

player *createPlayer(char *pd);
int playerToString(player *p, char *buf);
playerlist *loadPlayerList(char *fn);
int savePlayerList(playerlist *pl, char *fn);

playerlist *addPlayerToBottom(playerlist *pl,player *p);
playerlist *addPlayerToTop(playerlist *pl,player *p);

void freePlayerList(playerlist **pl);

void printPlayer(_data d);
void printPlayerList(playerlist *pl);
#endif // !__PLAYER_H