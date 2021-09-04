/*
** EPITECH PROJECT, 2018
** main
** File description:
** main
*/

#include "../include/main.hpp"

std::chrono::system_clock::time_point a = std::chrono::system_clock::now();
std::chrono::system_clock::time_point b = std::chrono::system_clock::now();

Ships::Ships()
{
    space = new sf::Sprite;
    space2 = new sf::Sprite;
    this->scores.setFont(font);
    this->scores.setString(this->display_score);
    this->scores.setPosition(700, 980);

    this->scores.setCharacterSize(24);
    this->scores.setStyle(sf::Text::Bold);

    this->rect_alien = {70, 100, 120, 60};
    this->shot_rect = {0, 50, 100, 75};

    this->ambiance.openFromFile("../../client/template/nitro.wav");
    this->piou.openFromFile("../../client/template/shot.wav");

    this->font.loadFromFile("../../client/template/font/Basic.ttf");

    this->ambiance.play();
    this->ambiance.setLoop(true);

    this->background.loadFromFile("../../client/template/background.png");
    this->space->setTexture(this->background);

    this->background2.loadFromFile("../../client/template/background.png");
    this->space2->setTexture(this->background2);

    this->ship_shot.loadFromFile("../../client/template/Shot.png");
    this->shot.setTexture(this->ship_shot);
    this->shot.setTextureRect(this->shot_rect);

    this->blue_shot.loadFromFile("../../client/template/Shot_2.png");
    this->blue_s.setTexture(this->blue_shot);
    this->blue_s.setTextureRect(this->shot_rect);

    this->yellow_shot.loadFromFile("../../client/template/Shot_3.png");
    this->yellow_s.setTexture(this->yellow_shot);
    this->yellow_s.setTextureRect(this->shot_rect);

    this->green_shot.loadFromFile("../../client/template/Shot_4.png");
    this->green_s.setTexture(this->green_shot);
    this->green_s.setTextureRect(this->shot_rect);

    this->bas_alien.loadFromFile("../../client/template/AlienBasic.png");
    this->alien_f.setTexture(this->bas_alien);
    this->alien_f.setTextureRect(this->rect_alien);

    this->bombe_alien.loadFromFile("../../client/template/AlienBomber.png");
    this->alien_s.setTexture(this->bombe_alien);
    this->alien_s.setTextureRect(this->rect_alien);

    this->space->setPosition(0,0);
    this->space2->setPosition(11520,0);
    this->shot.setPosition(2000,0);
    this->blue_s.setPosition(2000,0);
    this->yellow_s.setPosition(2000,0);
    this->green_s.setPosition(2000,0);
}

int rand_nb() {
    int s = 0;
    s = rand() % 1000;

    return s;
}

int main(int ac, char **argv) {
    srand(getpid());
    Ships ships;
    udpClient client;
    server_buffer_t info;
    server_buffer_t receive;

    info.id = 0;
    info.type = 1;
    info.x = 0;
    info.y = 0;

    client.CreateSock(argv);
    std::thread communication(&udpClient::Recv, &client);
    client.Send(info);
    receive = client.GetBuffer();
    int s = 0;
    while (receive.id == 0) {
        receive = client.GetBuffer();
    }
    ships.id = receive.id;
    cout << ships.id << endl;
    while (receive.type != 3){
        receive = client.GetBuffer();
    }
    ships.nb_player = 3;
    ships.window.create(sf::VideoMode(1920, 1080), "R-type");
    ships.load_textures(ships.nb_player);
    ships.begin_position(ships.nb_player);
    while (ships.window.isOpen())
    {
        receive = client.GetBuffer();
        ships.display_score = "Red = " + std::to_string(ships.score_red) + "  Blue = " + std::to_string(ships.score_blue) + "  Yellow = " + std::to_string(ships.score_yellow) + "  Green = " + std::to_string(ships.score_green);
        a = std::chrono::system_clock::now();
        std::chrono::duration<double, std::milli> work_time = a - b;
        if (work_time.count() < 10.0)
      {
          std::chrono::duration<double, std::milli> delta_ms(10.0 - work_time.count());
          auto delta_ms_duration = std::chrono::duration_cast<std::chrono::milliseconds>(delta_ms);
          std::this_thread::sleep_for(std::chrono::milliseconds(delta_ms_duration.count()));
      }
      b = std::chrono::system_clock::now();
      std::chrono::duration<double, std::milli> sleep_time = b - a;
        ships.pos = ships.get_ships_pos(5);
        ships.mouve_background(ships.pos);

        ships.pos = ships.shot.getPosition();
        ships.mouve_shot(ships.pos);

        ships.pos = ships.shot.getPosition();
        ships.alien = ships.alien_f.getPosition();
        ships.alien_bomb = ships.alien_s.getPosition();

        ships.check_kill(ships.id, ships.pos, ships.alien, ships.alien_bomb);

        s = rand_nb();
        if (s == 25 && ships.basic_A == 0 && ships.bomb_A == 0)
            ships.setpos_alien();
        if (receive.type == 6)
        {
            cout << " ID: " << receive.id << " X: "<< receive.x << " Y: "<< receive.y << endl;
            ships.set_other_pos(receive.id, receive.x, receive.y);
        }

        while (ships.window.pollEvent(ships.event))
        {
            if (ships.event.type == sf::Event::Closed)
                ships.window.close();
            ships.pos = ships.get_ships_pos(ships.id);
            if (ships.event.type == sf::Event::KeyPressed) {
                switch (ships.event.key.code) {
                    case sf::Keyboard::Left:
                        if (ships.pos.x > 0) {
                            ships.pos = ships.get_ships_pos(ships.id);
                            ships.ships_mouvement_left(ships.id,ships.pos.x,ships.pos.y);

                            ships.pos = ships.get_ships_pos(ships.id);

                            info.id = ships.id;
                            info.type = 4;
                            info.x = ships.pos.x;
                            info.y = ships.pos.y;

                            client.Send(info);
                        }
                        break;
                    case sf::Keyboard::Right:
                        if (ships.pos.x < 1820) {
                            ships.pos = ships.get_ships_pos(ships.id);
                            ships.ships_mouvement_right(ships.id,ships.pos.x,ships.pos.y);

                            ships.pos = ships.get_ships_pos(ships.id);

                            info.id = ships.id;
                            info.type = 4;
                            info.x = ships.pos.x;
                            info.y = ships.pos.y;

                            client.Send(info);
                        }
                        break;
                    case sf::Keyboard::Up:
                        if (ships.pos.y > 0) {
                            ships.pos = ships.get_ships_pos(ships.id);
                            ships.ships_mouvement_up(ships.id,ships.pos.x,ships.pos.y);

                            ships.pos = ships.get_ships_pos(ships.id);

                            info.id = ships.id;
                            info.type = 4;
                            info.x = ships.pos.x;
                            info.y = ships.pos.y;

                            client.Send(info);
                        }
                        break;
                    case sf::Keyboard::Down:
                        if (ships.pos.y < 980) {
                            ships.pos = ships.get_ships_pos(ships.id);
                            ships.ships_mouvement_down(ships.id,ships.pos.x,ships.pos.y);

                            ships.pos = ships.get_ships_pos(ships.id);

                            info.id = ships.id;
                            info.type = 4;
                            info.x = ships.pos.x;
                            info.y = ships.pos.y;

                           client.Send(info);
                        }
                        break;
                    case sf::Keyboard::Space:
                    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Space)) {
                        ships.pos = ships.shot.getPosition();
                        if (ships.pos.x > 2000) {
                            ships.pos = ships.get_ships_pos(ships.id);
                            ships.ships_fire(ships.pos);
                        }
                    }
                }
            }
        }
        ships.draw_sprite(ships.nb_player);
    }
    return 0;
}
