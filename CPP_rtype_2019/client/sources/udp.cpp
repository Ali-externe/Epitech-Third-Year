#include "../include/udp.hpp"
#include <bitset>
using namespace std;

udpClient::udpClient()
{
}

udpClient::~udpClient()
{
}

void udpClient::CreateSock(char **av)
{
    if ( (_sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) < 0 ) {
        perror("socket failed"); 
        exit(EXIT_FAILURE);
    }
    memset(&_servaddr, 0, sizeof(_servaddr));

    _servaddr.sin_family = AF_INET;
    _servaddr.sin_port = htons(atoi(av[1])); 
    _servaddr.sin_addr.s_addr = inet_addr(av[2]);
}

void udpClient::Send(server_buffer_t &info)
{
    server_buffer_t *stock = new server_buffer_t;

    stock->id = info.id;
    stock->type = info.type;
    stock->x = info.x;
    stock->y = info.y;
    sendto(_sockfd, stock, sizeof(server_buffer_t), 0, (const struct sockaddr *) &_servaddr, sizeof(struct sockaddr_in));
    printf("Hello message sent.\n");
}

server_buffer_t udpClient::GetBuffer()
{
    return (_server_buff);
}

void udpClient::Recv()
{
    char *buffer = new char[sizeof(server_buffer_t)];
    server_buffer_t *stock = new server_buffer_t;

    while (1) {
        recvfrom(_sockfd, buffer, sizeof(server_buffer_t), 0, (struct sockaddr *) &_servaddr, (socklen_t *)sizeof(struct sockaddr_in));
        stock = (server_buffer_t *)(buffer);
        _server_buff.id = stock->id;
        _server_buff.type = stock->type;
        _server_buff.x = stock->x;
        _server_buff.y = stock->y;
    }
}

void udpClient::PrintServerBuff() const
{
    std::cout << "id = " << _server_buff.id << std::endl;
    std::cout << "type = " << _server_buff.type << std::endl;
    std::cout << "x = " << _server_buff.x << std::endl;
    std::cout << "y = " << _server_buff.y << std::endl;
}
