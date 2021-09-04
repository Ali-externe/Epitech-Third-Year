#include "../include/main.hpp"

void Ships::ships_fire(sf::Vector2f pos) {
    this->shot.setPosition(pos.x + 150, pos.y + 50);
    this->window.draw(this->shot);
    this->piou.play();
}

void Ships::mouve_shot(sf::Vector2f pos) {
    if (pos.x >= 1200)
        this->piou.stop();
    this->shot.setPosition(pos.x + 15, pos.y);
}

void Ships::check_kill(int id, sf::Vector2f pos, sf::Vector2f alien, sf::Vector2f alien_bomb) {
    int touch = 0;
    sf::FloatRect first =  this->alien_f.getGlobalBounds();
    sf::FloatRect second =  this->alien_s.getGlobalBounds();
    sf::FloatRect shott =  this->shot.getGlobalBounds();
    if (first.intersects(shott) == true && alien.x < 2000) {
        this->alien_f.setPosition(2000,0);
        this->basic_A = 0;
        touch++;
    }
    if (second.intersects(shott) == true && alien_bomb.x < 2000) {
        this->alien_s.setPosition(2000,0);
        this->bomb_A = 0;
        touch++;
    }
    if (id == 1) {
        this->score_red = this->score_red + touch;

    }
    if (id == 2) {
        this->score_blue = this->score_blue + touch;

    }
    if (id == 3) {
        this->score_green = this->score_green + touch;

    }
    if (id == 4) {
        this->score_yellow = this->score_yellow + touch;

    }
}
