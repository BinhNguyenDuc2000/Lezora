SRCDIR = src
BINDIR = bin
INCDIR = inc
TESTDIR = test

CFLAGS = -c -Wall -I${INCDIR}
CC = gcc -g
LIBS =-pthread -lm

# Compiling and linking custom library
SOURCE = ${wildcard ${SRCDIR}/*.c}
OBJECT = ${patsubst %, ${BINDIR}/%, ${notdir ${SOURCE:.c=.o}}}

TARGET = server

${TARGET}: % : %.o ${OBJECT} 
	${CC} ${LIBS} -o $@ $^

#Compiling and linking test

${TESTDIR}/test_color_text: % : %.o ${BINDIR}/color_text.o
	${CC}	${LIBS} -o $@ $^

${TESTDIR}/test_llist: % : %.o ${BINDIR}/color_text.o ${BINDIR}/llist.o
	${CC}	${LIBS} -o $@ $^

${TESTDIR}/test_player: % : %.o ${OBJECT}
	${CC}	${LIBS} -o $@ $^

${TESTDIR}/test_game: % : %.o ${OBJECT}
	${CC}	${LIBS} -o $@ $^

${TESTDIR}/test_board: % : %.o ${OBJECT}
	${CC}	${LIBS} -o $@ $^

${TESTDIR}/%.o: ${TESTDIR}/%.c
	${CC}	${CFLAGS}	$< -o $@

${BINDIR}/%.o:	${SRCDIR}/%.c
	${CC}	${CFLAGS}	-c	$<	-o	$@

# Helper task
.PHONY: run runtest help clean

run: ${OBJECT}
	${OBJECT}

help: 
	@echo "objects: ${OBJECT}"
clean:
	rm -f *.o *~
