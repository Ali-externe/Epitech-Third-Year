/*
** EPITECH PROJECT, 2019
** r-type
** File description:
** main
*/

#include <SFML/Graphics.hpp>
#include <SFML/Audio.hpp>
#include <sys/types.h>
#include <stdexcept>
#include <iostream>
#include <cstdio>
#include <chrono>
#include <thread>
#include <unistd.h>
#include <memory>
#include <string>
#include <array>
#include "udp.hpp"

#pragma once

class Ships {
    public :
        sf::RenderWindow window;

        sf::Texture background;
        sf::Texture background2;
        sf::Texture red_ship;
        sf::Texture blue_ship;
        sf::Texture yellow_ship;
        sf::Texture green_ship;
        sf::Texture ship_shot;
        sf::Texture blue_shot;
        sf::Texture yellow_shot;
        sf::Texture green_shot;
        sf::Texture bas_alien;
        sf::Texture bombe_alien;

        sf::Sprite *space;
        sf::Sprite *space2;
        sf::Sprite red;
        sf::Sprite blue;
        sf::Sprite yellow;
        sf::Sprite green;
        sf::Sprite shot;
        sf::Sprite blue_s;
        sf::Sprite yellow_s;
        sf::Sprite green_s;
        sf::Sprite alien_f;
        sf::Sprite alien_s;

        sf::Event event;
        sf::Text scores;
        sf::Font font;
        sf::Vector2f pos;
        sf::Vector2f alien;
        sf::Vector2f alien_bomb;
        sf::IntRect rect;
        sf::IntRect shot_rect;
        sf::IntRect rect_alien;
        sf::Music ambiance;
        sf::Music piou;

        int basic_A = 0;
        int bomb_A = 0;

        int score_red = 0;
        int score_blue = 0;
        int score_yellow = 0;
        int score_green = 0;

        int id = 0;
        int nb_player = 0;

        std::string display_score = "Red = 0  Blue = 0  Yellow = 0  Green = 0";

    public:
        Ships();
        int load_textures(int nb_players);
        void begin_position(int nb_players);
        void draw_sprite(int nb_players);
        void ships_mouvement_left(int id_player, int x, int y);
        void ships_mouvement_right(int id_player, int x, int y);
        void ships_mouvement_up(int id_player, int x, int y);
        void ships_mouvement_down(int id_player, int x, int y);
        void mouve_background(sf::Vector2f pos);
        void ships_fire(sf::Vector2f pos);
        void mouve_shot(sf::Vector2f pos);
        void setpos_alien();
        void set_other_pos(int id, int x, int y);
        void mouve_alien(sf::Vector2f alien,sf::Vector2f alien_bomb);
        void deplacement(int id_player, int x, int y);
        void check_kill(int id, sf::Vector2f pos,sf::Vector2f alien,sf::Vector2f alien_bomb);
        sf::Vector2f get_ships_pos(int id_player);
};
