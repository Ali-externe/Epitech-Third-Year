#include "../include/main.hpp"

void Ships::begin_position(int nb_players) {
    if (nb_players >= 1)
        this->red.setPosition(0, 0);
    if (nb_players >= 2)
        this->blue.setPosition(0, 270);
    if (nb_players >= 3)
        this->yellow.setPosition(0, 540);
    if (nb_players >= 4)
        this->green.setPosition(0, 810);
}

void Ships::setpos_alien() {
    int s = 0;
    int y = 0;
    int x = 0;
    int t = 0;
    while (s < 1200) {
        s = rand() % 1750;
    }
    while (x < 1200) {
        x = rand() % 1750;
    }
    y = rand() % 960;
    t = rand() % 960;

    this->alien_f.setPosition(s,y);
    this->alien_s.setPosition(x,t);
    this->basic_A = 1;
    this->bomb_A = 1;
}

sf::Vector2f Ships::get_ships_pos(int id) {
    if (id == 1)
    return this->red.getPosition();
    if (id == 2)
    return this->blue.getPosition();
    if (id == 3)
    return this->yellow.getPosition();
    if (id == 4)
    return this->green.getPosition();
    if (id == 5)
    return this->space->getPosition();
}

void Ships::set_other_pos(int id, int x, int y) {
    if (id == 1)
        this->red.setPosition(x, y);
    if (id == 2)
        this->blue.setPosition(x, y);
    if (id == 3)
        this->yellow.setPosition(x, y);
    if (id == 4)
        this->green.setPosition(x, y);
}