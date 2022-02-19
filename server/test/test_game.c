#include <stdio.h>
#include <stdlib.h>

#include <string.h>
#include "../inc/game.h"

int main(){
    gamelist *gl = NULL;
    char pl1[50] = "An_1_35";
    player *p = createPlayer(strdup(pl1));
    gl = addGameToBottom(gl, createGame(0, createPlayer(strdup(pl1))));
    // gl = addGameToBottom(gl, createGame(2, createPlayer(strdup(pl1))));
    // printf("%d\n", getGameListLength(gl));
    

    game *g = (game *)malloc(sizeof(game));
	game *temp = createGame(1, p);

    g = findGame(gl, temp, 0, compareGame);
    gameToString(g, pl1);
    printf ("%s\n", pl1);
    freeGameList(&gl);
    return 0;
}