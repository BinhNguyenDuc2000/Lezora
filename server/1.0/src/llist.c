#include <stdio.h>
#include <stdlib.h>

#include "../inc/llist.h"

// Core basic

/**
 * @brief create node from given data
 * 
 * @param d data of the node
 * @return node* 
 */
node *makeNode(_data d){
    node *n = (node*) malloc(sizeof(node));
    n->data = d;
    n->nextNode = n;
    n->prevNode = n;
    return n;
}

/**
 * @brief create list from given data
 * 
 * @param d data of the node
 * @return llist* 
 */
llist *makeList(_data d){
    node *n = makeNode(d);
    llist *ll = (llist *)malloc(sizeof(llist));
    ll->bottom=n;
    ll->top=n;
    return ll;
}

/**
 * @brief Create and add a node to the bottom of the list
 * 
 * @param ll destination list
 * @param d data of the node
 * @return ll* 
 */
llist *addNodeToBottom(llist *ll,_data d){
    if (ll==NULL){
        ll = makeList(d);
        return ll;
    }
    node *n = makeNode(d);
    n->prevNode = ll->bottom;
    n->nextNode = ll->top;
    
    ll->bottom->nextNode = n;
    ll->top->prevNode = n;
    ll->bottom = n;
    return ll;
}

/**
 * @brief Create and add a node to the top of the list
 * 
 * @param ll destination list
 * @param d data of the node
 * @return void* 
 */
llist *addNodeToTop(llist *ll,_data d){
    if (ll==NULL){
        ll = makeList(d);
        return ll;
    }
    node *n = makeNode(d);
    n->prevNode = ll->bottom;
    n->nextNode = ll->top;

    ll->bottom->nextNode = n;
    ll->top->prevNode = n;
    ll->top = n; 
    return ll;
}

/**
 * @brief free list and change list pointer to NULL
 * 
 * @param ll pointer of the destination list
 */
void freeList(llist **ll){
    if (ll == NULL || *ll == NULL){
        return;
    }
    node *n = (*ll)->top;
    while (n!=NULL && n!=(*ll)->bottom)
    {
        free(n->data);
        n=n->nextNode;
        free(n->prevNode);
    }
    free(n->data);
    free((*ll));
    *ll=NULL;
}

// Core Advance

/**
 * @brief find node in list that match requirement
 * 
 * @param ll destination list
 * @param target target data
 * @param range how loose is the requirement, for exact searches, set range to 0
 * @param f requirement
 * @return node* 
 */
node *findNode(llist *ll, _data target, int range, int f(_data, _data)){
    if (ll == NULL){
        return NULL;
    }
    node *n = ll->top;
    while (n!=ll->bottom)
    {
        if (f(n->data, target)<=range){
            return n;
        }
        n=n->nextNode;
    }
    if (f(n->data, target)<=range){
        return n;
    }
    return NULL;
}

/**
 * @brief delete list with 1 element or delete node from list 
 * 
 * @param ll pointer to destination list
 * @param n node that needs to be deleted
 */
void deleteNode(llist **ll, node *n){
    if (n==NULL)
        return;
    if ((*ll)->top==(*ll)->bottom){
        freeList(ll);
        return;
    }
    if (n==(*ll)->top)
        (*ll)->top = n->nextNode;
    if (n==(*ll)->bottom)
        (*ll)->bottom = n->prevNode;
    
    n->nextNode->prevNode = n->prevNode;
    n->prevNode->nextNode = n->nextNode;
    free(n->data);
    free(n);
}

// Utils

/**
 * @brief Print the entire list
 * 
 * @param ll destination list
 * @param f how to print the list
 */
void printList(llist *ll, void f(_data)){
    if (ll==NULL){
        printf("List is empty\n");
        return;
    }
    node *n = ll->top;
    while (n!=ll->bottom)
    {
        f(n->data);
        n=n->nextNode;
    }
    f(n->data);
    return;
}

