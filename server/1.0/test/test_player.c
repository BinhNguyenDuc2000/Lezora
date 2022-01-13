#include <stdio.h>

#include "../inc/player.h"


int main(){
    playerlist *ll = loadPlayerList("player_list.txt");
    printPlayerList(ll);
    char pl1[50] = "An_1_35_1";
    ll = addPlayerToTop(ll, createPlayer(pl1));
    char pl2[50] = "Zan_99_99_1";
    ll = addPlayerToBottom(ll, createPlayer(pl2));
    printPlayerList(ll);
    savePlayerList(ll, "player_list.txt");
    freePlayerList(&ll);
    return 0;
}