#include <stdio.h>
#include <stdlib.h>

#include "../inc/board.h"

board *newBoard(char *username, int rank){
    board *b = (board *)malloc(sizeof(board));
    b->username = username;
    b->rank = rank;
    b->hp = 12;
    b->atk = 0;
    b->def = 0;
    b->res = 0;
    b->tired_factor = 0;
    int i = 0;
    for (;i<4;i++)
    {
        (b->card_status)[i] = 2;
    }
    refreshBoard(b);
    return b;
}

void refreshBoard(board *b)
{
    b->res = 0;
    b->atk = 0;
    b->def = 0;
    int i = 0;
    for (;i<4;i++)
    {
        if (b->card_status[i] != 0) {
            b->hand[i] = drawCard(b->tired_factor);
            b->card_status[i] = 0;
            b->tired_factor+=2;
        }
    }
}

int boardToString(board *b, char *buf){
    return sprintf(buf, "board_%s_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d", 
            b->username, b->rank, b->hp, b->res, b->atk, b->def, b->tired_factor, 
            ((b->hand)[0].card_code), (b->card_status)[0],
            ((b->hand)[1].card_code), (b->card_status)[1],
            ((b->hand)[2].card_code), (b->card_status)[2],
            ((b->hand)[3].card_code), (b->card_status)[3]
            );

}