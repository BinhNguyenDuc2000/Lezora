#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "../inc/board.h"

int main(){
    srand(time(NULL));
    board *b = newBoard("Binh", 30);
    char buf[1024];
    
    (b->card_status)[0] = 1;
    boardToString(b, buf);
    printf("%s\n", buf);
    
    refreshBoard(b);
    boardToString(b, buf);
    printf("%s\n", buf);
    free(b);
    return 0; 
}