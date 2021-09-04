/*
** EPITECH PROJECT, 2019
** server.cpp
** File description:
** server.cpp
*/

#include "../include/server.hpp"

typedef struct server_buffer
{
    int id;
    int type;
    int x;
    int y;
} server_buffer_t;

Server::Server(int port): _maxClient(4), _minClient(3)
{
    _socket = socket(AF_INET, SOCK_DGRAM, 0);
    _addr.sin_addr.s_addr = htonl(INADDR_ANY);
    _addr.sin_port = htons(port);
    _addr.sin_family = AF_INET;
    if (bind(_socket, reinterpret_cast<sockaddr *>(&_addr), sizeof(sockaddr_in)) != 0)
        std::cout << "bind fail" << std::endl;
    std::cout << "adress = " << inet_ntoa(_addr.sin_addr) << std::endl;
    std::cout << "Port = " << htons(_addr.sin_port) << std::endl;
    Server::startRecev();
}

int Server::startRecev()
{
    sockaddr_in from;
    server_buffer_t *serv_buf = new server_buffer_t;
    server_buffer_t *serv_buf_send = new server_buffer_t;
    char *buff = new char[sizeof(server_buffer_t)];
    socklen_t fromlen = sizeof(from);
    int nbr_client = 0;
 
    while(nbr_client < 3) {
        recvfrom(_socket, buff, sizeof(server_buffer_t), 0, reinterpret_cast<sockaddr*>(&from), &fromlen);
        serv_buf = reinterpret_cast<server_buffer_t *>(buff);
        std::cout << buff << std::endl;
        if (serv_buf->id == 0 && serv_buf->type == 1) {
            _addrRecev[nbr_client] = from;
            nbr_client = nbr_client + 1;
            serv_buf_send->id = nbr_client;
            serv_buf_send->type = 2;
            serv_buf_send->x = 0;
            serv_buf_send->y = 0;
            sendto(_socket, serv_buf_send, sizeof(server_buffer_t), 0,reinterpret_cast<sockaddr*>(&from), sizeof(from));
        }
    }
    Server::sendStart();
    Server::startGame();
    return 0;
}

int Server::startGame()
{
    sockaddr_in from;
    server_buffer_t *serv_buf = new server_buffer_t;
    char *buff = new char[sizeof(server_buffer_t)];
    socklen_t fromlen = sizeof(from);
    GameEngine game;

    while (1) {
        recvfrom(_socket, buff, sizeof(server_buffer_t), 0, reinterpret_cast<sockaddr*>(&from), &fromlen);
        serv_buf = reinterpret_cast<server_buffer_t *>(buff);
        std::cout << "Recev: id = "<< serv_buf->id << ", type = " << serv_buf->type << ", x = " << serv_buf->x << ", y = " << serv_buf->y << std::endl;
        if (serv_buf->type == 4)
            game.SetPos(serv_buf->id, serv_buf->x, serv_buf->y);
            Server::sendPos(serv_buf->id, serv_buf->x, serv_buf->y);
    }
    return 0;
}

int Server::sendPos(int id, int x, int y)
{
    server_buffer_t *serv_buf_send = new server_buffer_t;
    serv_buf_send->id = id;
    serv_buf_send->type = 6;
    serv_buf_send->x = x;
    serv_buf_send->y = y;

    for (int i = 0; i < 3; i++) {
        std::cout << "Send: id = "<< serv_buf_send->id << ", type = " << serv_buf_send->type << ", x = " << serv_buf_send->x << ", y = " << serv_buf_send->y << std::endl;
        sendto(_socket, serv_buf_send, sizeof(server_buffer_t), 0 ,reinterpret_cast<sockaddr*>(&_addrRecev[i]), sizeof(_addrRecev[i]));
    }
}

int Server::sendStart()
{
    server_buffer_t *serv_buf_send = new server_buffer_t;
    serv_buf_send->id = 0;
    serv_buf_send->type = 3;
    serv_buf_send->x = 0;
    serv_buf_send->y = 0;

    for (int i = 0; i < 4; i++) {
            sendto(_socket, serv_buf_send, sizeof(server_buffer_t), 0 ,reinterpret_cast<sockaddr*>(&_addrRecev[i]), sizeof(_addrRecev[i]));
    }
}