#ifndef __BOARD_H_
#define __BOARD_H_

#include <card.h>

typedef struct _board
{
    char *username;
    int rank;
    int hp;
    int res;
    int atk;
    int def;
    int tired_factor;
    card hand[4];
    int card_status[4]; // Status of each card in hand: 0 is normal, 1 is sold, 2 is used 
} board;

board *newBoard(char *username, int rank);

void refreshBoard(board *b);

int boardToString(board *b, char *buf);


#endif // !__CARD_H_