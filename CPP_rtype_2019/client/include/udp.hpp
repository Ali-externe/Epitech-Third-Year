#include <iostream>
#include <string>
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <string.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <arpa/inet.h> 
#include <netinet/in.h>
#include <thread>

using namespace std;

typedef struct server_buffer
{
    int id;
    int type;
    int x;
    int y;
} server_buffer_t;

class udpClient
{
    public:
    udpClient();
    ~udpClient();
    void Send(server_buffer_t &info);
    server_buffer_t GetBuffer();
    void Recv();
    void CreateSock(char **av);
    void PrintServerBuff() const;
    protected:
    int _sockfd;
    struct sockaddr_in _servaddr;
    server_buffer_t _server_buff;
};