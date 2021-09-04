/*
** EPITECH PROJECT, 2019
** GameEngine
** File description:
** GameEngine
*/

#include "../include/gameEngine.hpp"

GameEngine::GameEngine()
{
    for (int i = 0; i < 4; i++) {
        _x[i] = 0;
        _y[i] = 0;
    }
}

int GameEngine::SetPos(int id, int x, int y)
{
    return 0;
}

int GameEngine::GetX(int id)
{
    return _x[id - 1];
}

int GameEngine::GetY(int id)
{
    return _y[id - 1];
}