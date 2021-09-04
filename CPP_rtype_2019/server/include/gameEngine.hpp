/*
** EPITECH PROJECT, 2019
** GameEngine
** File description:
** GameEngine
*/

#ifndef Engine
#define Engine

class GameEngine
{
    public:
        GameEngine();
        int SetPos(int id, int x, int y);
        int GetX(int id);
        int GetY(int id);
    private:
        int _x[4];
        int _y[4];
};

#endif /* !Engine */
