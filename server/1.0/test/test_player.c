#include <stdio.h>
#include <string.h>

#include "../inc/player.h"


int main(){
    playerlist *ll = loadPlayerList("player_list.txt");
    printPlayerList(ll);
    char pl1[50] = "An_1_35";
    ll = addPlayerToTop(ll, createPlayer(strdup(pl1)));
    char pl2[50] = "Zan_99_99";
    ll = addPlayerToBottom(ll, createPlayer(strdup(pl2)));
    printPlayerList(ll);
    savePlayerList(ll, "player_list.txt");
    player *temp = createPlayer(strdup(pl1));
    player *p = findPlayer(ll, temp, 0, comparePlayer);
    printPlayer(p);
    freePlayerList(&ll);
    return 0;
}