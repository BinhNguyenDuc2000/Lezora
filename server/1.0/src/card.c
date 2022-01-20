#include <stdio.h>
#include <stdlib.h>
#include "../inc/card.h"
#include "../inc/color_text.h"
#define MAX_CARD 4

card CardList[MAX_CARD] = {
                    {CARD_TIRED, 1, 1, 1, 0},
                    {CARD_SWORD, 1, 2, 3, 3},
                    {CARD_GUN, 1, 2, 5, 0},
                    {CARD_SHIELD, 2, 1, 0, 4}
                    };

card getCard(CardCode cc){
    int i=0;
    for (; i< MAX_CARD; i++){
        if (CardList[i].card_code == cc){
            return CardList[i];
        }
    }
    return CardList[0];
}

card drawCard(int tired_factor){
    int chance = rand()%100;
    if (chance <= tired_factor){
        return CardList[CARD_TIRED];
    }
    else {
        chance = rand()%3;
        switch (chance)
        {
        case 0:
            return CardList[CARD_SWORD];
            break;
        case 1:
            return CardList[CARD_GUN];
            break;
        case 2:
            return CardList[CARD_SHIELD];
            break;

        default:
            return CardList[CARD_TIRED];
            break;
        }
        
    }
}
