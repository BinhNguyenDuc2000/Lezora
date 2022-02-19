#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <pthread.h>
#include <string.h>
#include <unistd.h>

// Making seed for the RNG
#include <time.h>

#include <game.h>

//Remember to use -pthread when compiling this server's source code
void *connection_handler(void *);

player *login_player(char *client_message);

player *register_player(char *client_message);

game *create_game(char *client_message, player *p);

game *join_game(char *client_message, player *p, int room_id);

pthread_mutex_t mutex;

int no_threads = 0;

char fn[20] = "player_list.txt";

playerlist *pl;

gamelist *gl;

int main()
{
	// Initiate RNG
	srand(time(NULL));

	pthread_mutex_init(&mutex, NULL);
	pl = loadPlayerList(fn);
	gl = NULL;
	int server_socket;
	server_socket = socket(AF_INET, SOCK_STREAM, 0);

	if (server_socket == -1)
	{
		perror("Socket initialisation failed");
		exit(EXIT_FAILURE);
	}
	else
		printf("Server socket created successfully\n");

	struct sockaddr_in server_addr;
	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(5555);
	server_addr.sin_addr.s_addr = htonl(INADDR_ANY);

	//bind the socket to the specified IP addr and port
	if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) != 0)
	{
		printf("socket bind failed...\n");
		exit(0);
	}
	else
		printf("Socket successfully binded..\n");

	if (listen(server_socket, 3) != 0)
	{
		printf("Listen failed...\n");
		exit(0);
	}
	else
		printf("Server listening..\n");

	pthread_t threads[99];
	while (no_threads < 99)
	{
		printf("Listening...\n");
		int client_socket = accept(server_socket, NULL, NULL);
		puts("Connection accepted");
		if (pthread_create(&threads[no_threads], NULL, connection_handler, &client_socket) < 0)
		{
			perror("Could not create thread");
			return 1;
		}
		if (client_socket < 0)
		{
			printf("server acccept failed...\n");
			exit(0);
		}
		else
			printf("Server acccept the client...\n");
		puts("Handler assigned");
		no_threads++;
	}
	int k = 0;
	for (k = 0; k < 99; k++)
	{
		pthread_join(threads[k], NULL);
	}

	//int send_status;
	//send_status=send(client_socket, server_message, sizeof(server_message), 0);
	close(server_socket);
	freeGameList(&gl);
	pthread_mutex_destroy(&mutex);
	return 0;
}

void *connection_handler(void *client_socket)
{
	int socket = *(int *)client_socket;
	int read_len;
	char server_message[BUFSIZ] = "HELLO FROM SERVER, YOU ARE CONNECTED";
	int send_status;
	send_status = send(socket, server_message, strlen(server_message), 0);
	char client_message[BUFSIZ];
	bzero(client_message, BUFSIZ);
	player *p = NULL;
	game *g = NULL;
	while (1)
	{
		read_len = recv(socket, client_message, 100, 0);
		if (read_len < 1)
		{
			break;
		}
		//end of string marker
		client_message[read_len] = '\0';
		char command[10];
		strcpy(command, strtok(strdup(client_message), "_"));
		if (strcmp(command, "getroom") != 0 && strcmp(command, "getgame") !=0 && strcmp(command, "getboard")){
			printf("\nMessage recieve from client %s\n", client_message);
		}
		
		if (strcmp(command, "login") == 0)
		{
			if (strstr(strdup(client_message), "__") == NULL && client_message[read_len - 1] != '_')
			{
				p = login_player(client_message);
			}
			else
			{
				strcpy(client_message, "error_INVALIDINPUT");
			}
		}

		if (strcmp(command, "register") == 0)
		{
			if (strstr(strdup(client_message), "__") == NULL && client_message[read_len - 1] != '_')
			{
				p = register_player(client_message);
			}
			else
			{
				strcpy(client_message, "error_INVALIDINPUT");
			}
		}

		if (strcmp(command, "logout") == 0)
		{
			p->status = 0;
			strcpy(client_message, "logout");
		}

		if (strcmp(command, "createroom") == 0)
		{
			g = create_game(client_message, p);
		}

		if (strcmp(command, "joinroom") == 0)
		{
			int game_id = atoi(strtok(NULL, "_"));
			g = join_game(client_message, p, game_id);
		}

		if (strcmp(command, "quitroom") == 0){
			pthread_mutex_lock(&mutex);
			g->status = 0;
			if (g->phase==0){
				strcpy(client_message, "quitroom");
			}
			else {
				if (p == g->player1){
					g->phase = 6;	
				}
				else 
				{
					g->phase = 5;
				}
				gameToString(g, client_message);
			}
			pthread_mutex_unlock(&mutex);
		}

		if (strcmp(command, "pass") == 0){
			pthread_mutex_lock(&mutex);
			advancePhase(g);
			printf("phase: %d\n", g->phase);
			pthread_mutex_unlock(&mutex);
		}

		if (strcmp(command, "sell") == 0){
			pthread_mutex_lock(&mutex);
			if (!sellCard(g, atoi(strtok(NULL, "_"))))
			{
				strcpy(client_message, "error_sell");
			}
			pthread_mutex_unlock(&mutex);
		}

		if (strcmp(command, "use") == 0){
			pthread_mutex_lock(&mutex);
			if (!useCard(g, atoi(strtok(NULL, "_"))))
			{
				strcpy(client_message, "error_use");
			}
			pthread_mutex_unlock(&mutex);
		}

		//Send the message back to client
		if (strcmp(command, "getroom") == 0)
		{	
			pthread_mutex_lock(&mutex);
			gameToString(g, client_message);
			pthread_mutex_unlock(&mutex);
			send_status = send(socket, client_message, strlen(client_message), 0);
		}
		
		else if (strcmp(command, "getgame") == 0){
			pthread_mutex_lock(&mutex);
			if (g->phase > 0 && g->phase < 5){
				
				phaseToString(g, client_message);
				
				send_status = send(socket, client_message, strlen(client_message), 0);
			}
			else{
				gameToString(g, client_message);
				send_status = send(socket, client_message, strlen(client_message), 0);
			}
			pthread_mutex_unlock(&mutex);
		}
		else if (strcmp(command, "getboard") == 0){
			pthread_mutex_lock(&mutex);
			if (atoi(strtok(NULL, "_"))==1){
				boardToString(g->board1, client_message);
			}
			else {
				boardToString(g->board2, client_message);
			}
			pthread_mutex_unlock(&mutex);
			send_status = send(socket, client_message, strlen(client_message), 0);
		}
		else
		{
			send_status = send(socket, client_message, strlen(client_message), 0);
			printf("\nMessage send to client %s, size %d bytes\n", client_message, send_status);
		}
		bzero(client_message, BUFSIZ);
	}
	printf("\n Client disconnected\n");
	pthread_mutex_lock(&mutex);

	if (g != NULL)
	{
		
		g->status = 0;
		if (g->board1 != NULL)
		{
			free(g->board1);
			g->board1 = NULL;
		}
		if (g->board2 != NULL){
			free(g->board2);
			g->board2 = NULL;
		}
		if (g->phase!=0) 
		{
			if (p == g->player1){
				g->phase = 6;	
			}
			else 
			{
				g->phase = 5;
			}
		}
	}

	if (p != NULL)
	{
		p->status = 0;
	}
	
	pthread_mutex_unlock(&mutex);
	no_threads--;
	return 0;
}

player *login_player(char *client_message)
{
	player *p = (player *)malloc(sizeof(player));
	strtok(client_message, "_");
	strcpy(p->username, strtok(NULL, "_"));
	strcpy(p->password, strtok(NULL, "_"));
	pthread_mutex_lock(&mutex);
	player *temp = findPlayer(pl, p, 0, comparePlayer);
	pthread_mutex_unlock(&mutex);
	free(p);
	if (temp == NULL)
	{
		strcpy(client_message, "error_PLAYERNOTFOUND");
	}
	else
	{
		if (temp->status == 0)
		{
			char temp_string[BUFSIZ];
			bzero(temp_string, BUFSIZ);
			temp->status = 1;
			playerToString(temp, temp_string);
			sprintf(client_message, "player_%s", temp_string);
			client_message[strlen(client_message) - 1] = '\0';
		}
		else
		{
			strcpy(client_message, "error_PLAYERALREADYONLINE");
		}
	}
	return temp;
}

player *register_player(char *client_message)
{
	player *p = (player *)malloc(sizeof(player));
	strtok(client_message, "_");
	strcpy(p->username, strtok(NULL, "_"));
	strcpy(p->password, strtok(NULL, "_"));
	pthread_mutex_lock(&mutex);
	player *temp = findPlayer(pl, p, 0, comparePlayerByName);
	pthread_mutex_unlock(&mutex);
	if (temp == NULL)
	{
		p->rank = 0;
		p->status = 1;
		pthread_mutex_lock(&mutex);
		addPlayerToBottom(pl, p);
		savePlayerList(pl, fn);
		pthread_mutex_unlock(&mutex);
		char temp_string[BUFSIZ];
		bzero(temp_string, BUFSIZ);
		playerToString(p, temp_string);
		sprintf(client_message, "player_%s", temp_string);
		client_message[strlen(client_message) - 1] = '\0';
	}
	else
	{
		free(p);
		strcpy(client_message, "error_PLAYERALREADYEXIST");
	}
	return p;
}
game *create_game(char *client_message, player *p)
{
	game *g = (game *)malloc(sizeof(game));
	pthread_mutex_lock(&mutex);
	g = createGame(getGameListLength(gl), p);
	g->phase = 0; // Room is created but the game has not begin
	gl = addGameToBottom(gl, g);
	pthread_mutex_unlock(&mutex);
	gameToString(g, client_message);
	return g;
}

game *join_game(char *client_message, player *p, int game_id)
{
	printf("%d\n", game_id);
	game *g = (game *)malloc(sizeof(game));
	game *temp = createGame(game_id, p);
	pthread_mutex_lock(&mutex);
	g = findGame(gl, temp, 0, compareGame);
	pthread_mutex_unlock(&mutex);
	if (g!=NULL && g->status == 1){
		pthread_mutex_lock(&mutex);
		g->player2 = p;
		g->status = 2;
		gameToString(g, client_message);
		int rng = rand()%2;
		if (rng == 0 ){
			g->phase = 1;
		}
		else{
			g->phase = 3;
		}
		g->board1 = newBoard(g->player1->username, g->player1->rank);
		g->board2 = newBoard(g->player2->username, g->player2->rank);
		pthread_mutex_unlock(&mutex);
	}
	else {
		strcpy(client_message, "error_INVALIDGAME");
	}
	return g;
}