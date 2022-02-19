#ifndef __CARD_H_
#define __CARD_H_

typedef enum{
    CARD_TIRED,
    CARD_SWORD,
    CARD_GUN,
    CARD_SHIELD
} CardCode;

typedef struct _card
{
    CardCode card_code;
    int refund_cost;
    int use_cost;
    int atk;
    int def;
} card;

card getCard(CardCode cc);

card drawCard(int tired_factor);

#endif // !__CARD_H_
