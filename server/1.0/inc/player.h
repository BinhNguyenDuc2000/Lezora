#ifndef __PLAYER_H
#define __PLAYER_H_

#include "llist.h"

typedef struct _player
{
    char username[20];
    char password[20];
    int rank;

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

int comparePlayer(player *p1, player *p2);
int comparePlayerByName(player *p1, player *p2);
player *findPlayer(playerlist *pl, player *target, int range, int f(player *, player *));

void printPlayer(_data d);
void printPlayerList(playerlist *pl);
#endif // !__PLAYER_H