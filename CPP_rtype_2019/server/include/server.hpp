/*
** EPITECH PROJECT, 2019
** server.hpp
** File description:
** server.hpp
*/

#ifndef Server_udp
#define Server_udp

#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <net/if.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include "gameEngine.hpp"

class Server
{
    public:
        Server(int port);
    private:
        int startRecev();
        int startGame();
        int sendStart();
        int sendPos(int id, int x, int y);
        int _socket;
        sockaddr_in _addr;
        sockaddr_in _addrRecev[4];
        int _maxClient;
        int _minClient;
};

#endif /* !Server_udp */
