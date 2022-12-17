#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
int main(int argc, char *argv[1])
{
    struct hostent *hen;
    if (argc != 2)
    {
        fprintf(stderr, "Enter the hostname \n");
        exit(1);
    }
    hen = gethostbyname(argv[1]);
    if (hen == NULL)
    {
        fprintf(stderr, "Host not found \n");
    }
    printf("Hostname is %s \n", hen->h_name);
    printf("IP address is %d \n", inet_ntoa(*((struct in_addr *)hen->h_addr)));
}