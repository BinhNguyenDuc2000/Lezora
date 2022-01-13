#include <stdio.h>

#include "../inc/color_text.h"

void reset () {
  printf("\033[0m");
}

void printRed(char *text){
    printf("\033[1;31m");
    printf ("%s", text);
    reset();
}

void printBlue(char *text){
    printf("\033[0;34m");
    printf ("%s", text);
    reset();
}

void printGreen(char *text){
    printf("\033[0;32m");
    printf ("%s", text);
    reset();
}

void printYellow(char *text){
    printf("\033[0;33m");
    printf ("%s", text);
    reset();
}

void printPurple(char *text){
    printf("\033[0;35m");
    printf ("%s", text);
    reset();
}

