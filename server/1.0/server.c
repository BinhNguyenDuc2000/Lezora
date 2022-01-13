#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <pthread.h>
#include <string.h>
#include <unistd.h>

#include <player.h>


//Remember to use -pthread when compiling this server's source code
void *connection_handler(void *);

int no_threads=0;

char fn[20] = "player_list.txt";

playerlist *pl;

int main()
{
	pl = loadPlayerList(fn);
    int server_socket;
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
	
    if (server_socket==-1){
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
    if (bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr))!=0){
	printf("socket bind failed...\n"); 
        exit(0);
	}
    else
	printf("Socket successfully binded..\n"); 
    
    if (listen(server_socket, 3)!=0){
		printf("Listen failed...\n"); 
        exit(0); 
    } 
    else
        printf("Server listening..\n"); 
    
    
    pthread_t threads[3];
    while (no_threads<3){
	printf("Listening...\n");
	int client_socket = accept(server_socket, NULL, NULL);
	puts("Connection accepted");
	if( pthread_create( &threads[no_threads], NULL ,  connection_handler , &client_socket) < 0){
	perror("Could not create thread");
	return 1;}
    	if (client_socket < 0) { 
        	printf("server acccept failed...\n"); 
        	exit(0); 
    		} 
    	else
        	printf("Server acccept the client...\n");
	puts("Handler assigned");
	no_threads++;
	}
	int k=0;
    for (k=0;k<9;k++){
	pthread_join(threads[k],NULL);
}

    //int send_status;
    //send_status=send(client_socket, server_message, sizeof(server_message), 0);
    close(server_socket);
    
    return 0;
}


void *connection_handler(void *client_socket){
	int socket = *(int*) client_socket;
	int read_len;
	char server_message[BUFSIZ] = "HELLO FROM SERVER, YOU ARE CONNECTED";
	int send_status;
    send_status=send(socket, server_message, strlen(server_message), 0);
	char client_message[BUFSIZ];
	while(1)
	{
		read_len=recv(socket,client_message, 100,0);
		if (read_len<1){
			break;
		}
		//end of string marker
		client_message[read_len] = '\0';
		printf ("\nMessage recieve from client %s\n", client_message);
		//Send the message back to client
		send_status=send(socket , client_message, strlen(client_message),0);
		printf("\nMessage send to client %s, size %d bytes\n", client_message, send_status);	
	}
	printf ("\n Client disconnected\n");
	no_threads--;
	return 0;
}
