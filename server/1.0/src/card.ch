#include "../inc/card.h"
#define MAX_CARD 4

card CardList[MAX_CARD] = {
                    {CARD_TIRED, KW_NONE,1, 1, 1, 0},
                    {CARD_SWORD, KW_UNBLOCKABLE, 3, 2, 7, 3},
                    {CARD_BOW, KW_CRITICAL,2, 1, 5, 0},
                    {CARD_SHILED, KW_NONE,1, 1, 2, 4}
                    };

card getCard(CardCode cc){
    int i=0;
    for (int i=0; i< MAX_CARD; i++){
        if (CardList[i].card_code == cc){
            return CardList[i];
        }
    }
    return CardList[0];
}
