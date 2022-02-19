#ifndef __LLIST_H_
#define __LLIST_H_
// Work with all data type
typedef void *_data;

// Universal node
typedef struct _node{
    _data data;
    struct _node *nextNode; 
    struct _node *prevNode;
} node;

// List that can be both a stack and a queue
typedef struct _llist
{
    node* top;
    node* bottom;
} llist;

// Core basic
node *makeNode(_data d);
llist *makeList(_data d);
llist *addNodeToBottom(llist *ll,_data d);
llist *addNodeToTop(llist *ll,_data d);
void freeList(llist **ll);

// Core Advance
node *findNode(llist *ll, _data target, int range, int f(_data, _data));
void deleteNode(llist **ll, node *n);

// Utils
void printList(llist *ll, void f(_data));

#endif // !__LLIST_H_