#ifndef __CARD_H_
#define __CARD_H_

typedef enum{
    KW_NONE,
    KW_UNBLOCKABLE,
    KW_CRITICAL
} KeyWord;
typedef enum{
    CARD_TIRED,
    CARD_SWORD,
    CARD_BOW,
    CARD_SHILED
} CardCode;

typedef struct _card
{
    CardCode card_code;
    KeyWord keyWord;
    int refund_cost;
    int use_cost;
    int atk;
    int def;
} card;

card getCard(CardCode cc);

#endif // !__CARD_H_
