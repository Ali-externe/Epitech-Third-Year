#include "../include/main.hpp"

void Ships::ships_mouvement_left(int id, int x, int y) {
    if (id == 1)
    this->red.setPosition(x - 10, y);
    if (id == 2)
    this->blue.setPosition(x - 10, y);
    if (id == 3)
    this->yellow.setPosition(x - 10, y);
    if (id == 4)
    this->green.setPosition(x - 10, y);
}

void Ships::ships_mouvement_right(int id, int x, int y) {
    if (id == 1)
    this->red.setPosition(x + 10, y);
    if (id == 2)
    this->blue.setPosition(x + 10, y);
    if (id == 3)
    this->yellow.setPosition(x + 10, y);
    if (id == 4)
    this->green.setPosition(x + 10, y);
}

void Ships::ships_mouvement_up(int id, int x, int y) {
    if (id == 1)
    this->red.setPosition(x, y - 10);
    if (id == 2)
    this->blue.setPosition(x, y - 10);
    if (id == 3)
    this->yellow.setPosition(x, y - 10);
    if (id == 4)
    this->green.setPosition(x, y - 10);
}

void Ships::ships_mouvement_down(int id, int x, int y) {
    if (id == 1)
    this->red.setPosition(x , y + 10);
    if (id == 2)
    this->blue.setPosition(x, y + 10);
    if (id == 3)
    this->yellow.setPosition(x, y + 10);
    if (id == 4)
    this->green.setPosition(x, y + 10);
}

void Ships::mouve_background(sf::Vector2f pos) {
    this->space->setPosition(pos.x - 10, pos.y);
    if (space->getPosition().x < -11520) {
        sf::Sprite *temp = space;
        space = space2;
        space2 = temp;
    }
    this->space2->setPosition(pos.x + 11500,0);
}

void Ships::mouve_alien(sf::Vector2f alien,sf::Vector2f alien_bomb) {
    int positive_x = rand() % 2;
    int positive_y = rand() % 2;
    if (positive_x == 0 && positive_y == 0 && alien.x < 1820 && alien.y < 980)
        this->alien_f.setPosition(alien.x + 5, alien.y + 5);
    if (positive_x == 1 && positive_y == 1 && alien.x > 1200 && alien.y > 0 )
        this->alien_f.setPosition(alien.x - 5, alien.y - 5);
    if (positive_x == 0 && positive_y == 1 && alien.x > 1820 && alien.y < 980)
        this->alien_f.setPosition(alien.x - 5, alien.y + 5);
    if (positive_x == 1 && positive_y == 0 && alien.x > 1200 && alien.y > 0)
        this->alien_f.setPosition(alien.x + 5, alien.y - 5);

    positive_x = rand() % 2;
    positive_y = rand() % 2;
    if (positive_x == 0 && positive_y == 0 && alien_bomb.x < 1820 && alien_bomb.y < 980)
        this->alien_s.setPosition(alien_bomb.x + 5, alien_bomb.y + 5);
    if (positive_x == 1 && positive_y == 1 && alien_bomb.x < 1200 && alien_bomb.y > 0)
        this->alien_s.setPosition(alien_bomb.x - 5, alien_bomb.y - 5);
    if (positive_x == 1 && positive_y == 0 && alien_bomb.x < 1820 && alien_bomb.y < 980)
        this->alien_s.setPosition(alien_bomb.x - 5, alien_bomb.y + 5);
    if (positive_x == 0 && positive_y == 1 && alien_bomb.x < 1200 && alien_bomb.y > 0)
        this->alien_s.setPosition(alien_bomb.x + 5, alien_bomb.y - 5);

}