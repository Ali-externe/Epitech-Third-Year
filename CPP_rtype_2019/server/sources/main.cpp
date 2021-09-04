/*
** EPITECH PROJECT, 2019
** main
** File description:
** main
*/

#include <iostream>
#include <thread>
#include <string>
#include "../include/server.hpp"

int main(int ac, char ** av)
{
    if (ac != 2)
        return 84;
    Server serv(std::stoi(av[1]));
    return 0;
}