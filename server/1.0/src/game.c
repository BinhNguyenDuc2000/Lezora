#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "../inc/color_text.h"
#include "../inc/llist.h"
#include "../inc/game.h"

// Core basic
/**
 * @brief Create a Game object.
 * 
 * @param game_id id representing the game
 * @param p1 the player who created the room
 * @return player* 
 */
game *createGame(int game_id, player *p1)
{
    game *g = (game *)malloc(sizeof(game));
    g->game_id = game_id;
    g->player1 = p1;
    g->status = 1;
    g->round = 1;
    return g;
}

/**
 * @brief create a string that represent the game.
 * 
 * @param g
 * @param buf 
 * @return int 
 */
int gameToString(game *g, char *buf)
{
    if (g == NULL)
    {
        return sprintf(buf, "null");
    }
    if (g->status == 1)
    {
        return sprintf(buf, "waiting_%d", g->game_id);
    }
    else if (g->status == 2)
    {
        return sprintf(buf, "ready_%d", g->game_id);
    }

    switch (g->phase)
    {
    case 0:
        return sprintf(buf, "closed_%d", g->game_id);
        break;
    case 5:
        return sprintf(buf, "win_1");
        break;
    case 6:
        return sprintf(buf, "win_2");
        break;
    case 7:
        return sprintf(buf, "tie");
        break;
    default:
        break;
    }

    return sprintf(buf, "closed_%d", g->game_id);
}

int phaseToString(game *g, char *buf)
{
    switch (g->phase)
    {
    case 1:
        return sprintf(buf, "atk_1");
        break;
    case 2:
        return sprintf(buf, "def_2");
        break;
    case 3:
        return sprintf(buf, "atk_2");
        break;
    case 4:
        return sprintf(buf, "def_1");
    default:
        return sprintf(buf, "error_INVALIDPHASE");
        break;
    }
}

/**
 * @brief add game to the bottom of the game list
 * 
 * @param gl 
 * @param g
 * @return gamelist* 
 */
gamelist *addGameToBottom(gamelist *gl, game *g)
{
    printGreen("Adding game: ");
    printf("%d\n", g->game_id);
    return (gamelist *)addNodeToBottom((llist *)gl, (_data)g);
}

/**
 * @brief add game to the top of the game list
 * 
 * @param gl 
 * @param g 
 * @return gamelist* 
 */
gamelist *addGameToTop(gamelist *gl, game *g)
{
    printGreen("Adding game: ");
    printf("%d\n", g->game_id);
    return (gamelist *)addNodeToTop((llist *)gl, (_data)g);
}

/**
 * @brief free the game list
 * 
 * @param gl 
 */
void freeGameList(gamelist **gl)
{
    freeList(gl);
}

// Core advance
int compareGame(game *g1, game *g2)
{
    return abs(g1->game_id - g2->game_id);
}

game *findGame(gamelist *gl, game *target, int range, int f(game *, game *))
{
    node *n = findNode((llist *)gl, (_data)target, 0, (int (*)(_data, _data))f);
    if (n == NULL)
    {
        return NULL;
    }
    return (game *)n->data;
}

int getGameListLength(gamelist *gl)
{
    if (gl == NULL)
    {
        return 0;
    }
    node *temp = gl->top;
    int length = 0;
    while (temp != gl->bottom)
    {
        length++;
        temp = temp->nextNode;
    }
    return (length + 1);
}

void advancePhase(game *g)
{
    int phase = g->phase;
    if (phase < 4)
    {
        g->phase++;
    }
    else
    {
        g->phase = 1;
    }
    if (g->phase == 1)
    {
        int lost_hp = g->board2->atk - g->board1->def;
        if (lost_hp > 0)
        {
            g->board1->hp -= lost_hp;    
        }
        if (g->board1->hp <= 0)
        {
            g->phase = 6;
            g->status = 0;
            return;
        } 
        g->round++;
        refreshBoard(g->board1);
    }

    if (g->phase == 3)
    {
        int lost_hp = g->board1->atk - g->board2->def;
        if (lost_hp > 0)
        {
            g->board2->hp -= lost_hp;    
        }
        if (g->board2->hp <= 0)
        {
            g->phase = 5;
            g->status = 0;
            return;
        } 
        g->round++;
        refreshBoard(g->board2);
    }

    if (g->round == 8)
    {
        g->status = 0;
        if (g->board1->hp > g->board2->hp)
        {
            g->phase = 5;
        }
        else if (g->board1->hp < g->board2->hp)
        {
            g->phase = 6;
            g->status = 0;
        }
        else 
        {
            g->phase = 7;
            g->status = 0;
        }
    }
}

int sellCard(game *g, int card_index)
{
    if (g->phase == 1 || g->phase == 4)
    {
        g->board1->res += ((g->board1->hand)[card_index]).refund_cost;
        ((g->board1->card_status)[card_index]) = 1;
        return 1;
    }

    if (g->phase == 2 || g->phase == 3)
    {
        g->board2->res += ((g->board2->hand)[card_index]).refund_cost;
        ((g->board2->card_status)[card_index]) = 1;
        return 1;
    }
    return 0;
}

int useCard(game *g, int card_index){
    switch (g->phase)
    {
    case 1:
        if (g->board1->res >= ((g->board1->hand)[card_index]).use_cost){
            g->board1->atk += ((g->board1->hand)[card_index]).atk;
            ((g->board1->card_status)[card_index]) = 2;
            g->board1->res -= ((g->board1->hand)[card_index]).use_cost;
            advancePhase(g);
            return 1;
        }
        break;
    case 2:
        if (g->board2->res >= ((g->board2->hand)[card_index]).use_cost){
            g->board2->def += ((g->board2->hand)[card_index]).def;
            (g->board2->card_status)[card_index] = 2;
            g->board2->res -= ((g->board2->hand)[card_index]).use_cost;
            advancePhase(g);
            return 1;
        }
        break;
    case 3:
        if (g->board2->res >= ((g->board2->hand)[card_index]).use_cost){
            g->board2->atk += ((g->board2->hand)[card_index]).atk;
            ((g->board2->card_status)[card_index]) = 2;
            g->board2->res -= ((g->board2->hand)[card_index]).use_cost;
            advancePhase(g);
            return 1;
        }
        break;
    case 4:
        if (g->board1->res >= ((g->board1->hand)[card_index]).use_cost){
            g->board1->def += ((g->board1->hand)[card_index]).def;
            ((g->board1->card_status)[card_index]) = 2;
            g->board1->res -= ((g->board1->hand)[card_index]).use_cost;
            advancePhase(g);
            return 1;
        }
        break;

    default:
        break;
    }
    return 0;
}