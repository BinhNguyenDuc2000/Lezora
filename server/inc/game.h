#ifndef __GAME_H_
#define __GAME_H_

#include "player.h"
#include "board.h"

typedef struct _game
{
    int game_id;
    int status; // Game status: 1 waitting for 1 more player, 2 ready
    player *player1;
    player *player2;
    int phase; // Phase in a game, 1: player 1 attack, 2 player 2 defend, 3 player 2 attack, 4 player 1 defend
            // Special phase include 0: room is created but the game has not started, 
            // 5: player 1 win, 6: player 2 win, 7: tie 
    int round; // Round in game, every 1-3 or 3-1 phase avance round by 1
    board *board1;
    board *board2;
} game;

typedef llist gamelist;

game *createGame(int game_id, player *p1);
int gameToString(game *g, char *buf);
int phaseToString(game *g, char *buf);

gamelist *addGameToBottom(gamelist *gl,game *g);
gamelist *addGameToTop(gamelist *gl,game *g);

void freeGameList(gamelist **gl);

int compareGame(game *g1, game *g2);
game *findGame(gamelist *gl, game *target, int range, int f(game *, game *));

int getGameListLength(gamelist *gl);

// Game related
void advancePhase(game *g);

int sellCard(game *g, int card_index);

int useCard(game *g, int card_index);

#endif // !__LLIST_H_