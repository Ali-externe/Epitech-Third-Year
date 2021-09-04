#include "../include/main.hpp"

int Ships::load_textures(int nb_players) {
    this->rect = {50, 80, 150, 150};

    if (nb_players >= 1) {
        if (!this->red_ship.loadFromFile("../../client/template/red_ship.png"))
        return EXIT_FAILURE;
        this->red.setTexture(this->red_ship);
        this->red.setTextureRect(this->rect);
    }
    if (nb_players >= 2) {
        if (!this->blue_ship.loadFromFile("../../client/template/blue_ship.png"))
        return EXIT_FAILURE;
        this->blue.setTexture(this->blue_ship);
        this->blue.setTextureRect(this->rect);

    }
    if (nb_players >= 3) {
        if (!this->yellow_ship.loadFromFile("../../client/template/yellow_ship.png"))
        return EXIT_FAILURE;
        this->yellow.setTexture(this->yellow_ship);
        this->yellow.setTextureRect(this->rect);

    }
    if (nb_players >= 4) {
        if (!this->green_ship.loadFromFile("../../client/template/green_ship.png"))
        return EXIT_FAILURE;
        this->green.setTexture(this->green_ship);
        this->green.setTextureRect(this->rect);

    }
}

void Ships::draw_sprite(int nb_players) {
    this->window.clear();
    this->window.draw(*this->space);
    this->window.draw(*this->space2);
    this->window.draw(this->shot);
    this->window.draw(this->blue_s);
    this->window.draw(this->green_s);
    this->window.draw(this->yellow_s);
    this->scores.setString(this->display_score);
    this->window.draw(this->scores);

    if (basic_A == 1)
    this->window.draw(this->alien_f);
    if (bomb_A == 1)
    this->window.draw(this->alien_s);

    if (nb_players >= 1)
        this->window.draw(this->blue);
    if (nb_players >= 2)
        this->window.draw(this->red);
    if (nb_players >= 3)
        this->window.draw(this->yellow);
    if (nb_players >= 4)
        this->window.draw(this->green);
    this->window.display();

}