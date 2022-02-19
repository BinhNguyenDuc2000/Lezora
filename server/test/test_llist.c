#include <stdio.h>
#include <stdlib.h>
#include "../inc/llist.h"

void printInt(_data d){
    if (d==NULL){
        printf("NULL\n");
        return;
    }
    printf("%d\n", *(int*)d);
}

int compareInt(_data a, _data b){
    return abs(*(int*)a - *(int*)b);
}

int main(int argc, char const *argv[])
{
    int *a= (int *) malloc(sizeof(int));
    *a=3;
    llist *ll = makeList(a);
    int *b= (int *) malloc(sizeof(int));
    *b=1;
    ll = addNodeToTop(ll, b);
    int *c= (int *) malloc(sizeof(int));
    *c=5;
    ll = addNodeToBottom(ll, c);
    printList(ll, printInt);
    int d = 3;
    deleteNode(&ll, findNode(ll, &d, 0, compareInt));
    printList(ll, printInt);
    freeList(&ll);
    return 0;
}
