#!/usr/bin/env python3
from random import randint

def tab_printer(tab):
    s = 0
    while s < l + 1:
        print (tab[s])
        s = s + 1

def min_fct(tab, s, w):
    if (w != (len(tab) - 1) and tab[s][w + 1] != 'A' and tab[s][w + 1] != 'H'):
        tab[s][w + 1] = tab[s][w + 1] + 1
    if (w != 0 and tab[s][w - 1] != 'A' and tab[s][w - 1] != 'H'):
        tab[s][w - 1] = tab[s][w - 1] + 1
    if (s != (len(tab) - 1) and tab[s + 1][w] != 'A' and tab[s + 1][w] != 'H'):
        tab[s + 1][w] = tab[s + 1][w] + 1
    if (s != 0 and tab[s - 1][w] != 'A' and tab[s - 1][w] != 'H'):
        tab[s - 1][w] = tab[s - 1][w] + 1

def min_fct_2(tab, a, b):
    tab[a][b + 1] = 1
    tab[a][b - 1] = 1
    tab[a + 1][b] = 1
    tab[a - 1][b] = 1
    tab[a + 1][b + 1] = 1
    tab[a - 1][b - 1] = 1
    tab[a + 1][b - 1] = 1
    tab[a - 1][b + 1] = 1

def in_middle_of_map(tab, l):
    a = ((l - 1)/2)
    a = int(a)
    b = a

    tab [a][a] = 'A'
    tab[a][a] = 'A'

    turn = str(a) + ',' + str(a) + '\0'
    #min_fct_2(tab, a, b)
    print (turn)


def hight_number(tab):
    s = 0
    w = 0
    posy = 0
    posx = 0
    hight = 0
    while s < (len(tab)):
        if tab[s][w] != 'A' and tab[s][w] != 'H' and  int(tab[s][w]) >= int(hight):
            posy = s
            posx = w
        if (w == (len(tab) - 1)):
            w = 0
            s = s + 1
        w = w + 1
    return [posy, posx]

def random_play(tab, l,):
    pos = hight_number(tab)
    y = int(pos[0])
    x = int(pos[1])
    tab [y][x] = 'A'
    tab[y][x] = 'A'

    max_fct(tab, y, x)
    turn = str(x) + ',' + str(y) + '\0'
    print (turn)
    #tab_printer(tab, tab)
def begin(tab, l):
    in_middle_of_map(tab, l)

def info(tab, l):
    random_play(tab,l)

def board(tab, l, inp, line):

    while line[0] != "DONE":
        inp = input()
        if inp.split():
            line = inp.split()
            if line[0] != "DONE":
                [x,y,field] = line[0].split(',')
                if int(field) == 1:
                    y = int(y)
                    x = int(x)
                    tab[y][x] = 'A'
                elif int(field) == 2:
                    y = int(y)
                    x = int(x)
                    tab[y][x] = 'H'    

def check_if_loose(tab, y, x):
    i = 0
    s = 0
    w = 0
    while s < len(tab):
        if tab[s][w] == 'A' and i == 0:
            if w <= (len(tab) - 5) and tab[s][w + 1] == 'A' and tab[s][w + 2] == 'A' and tab[s][w + 3] == 'A' and tab[s][w + 4] == 0:
                i = i + 1
                turn = str(w + 4) + ',' + str(s) + '\0'
                tab[s][w + 4] = 'A'
                print(turn)
            elif w >= 4 and tab[s][w - 1] == 'A' and tab[s][w - 2] == 'A' and tab[s][w - 3] == 'A' and tab[s][w - 4] == 0:
                i = i + 1
                turn = str(w - 4) + ',' + str(s) + '\0'
                tab[s][w - 4] = 'A'
                print(turn)
            elif s <= (len(tab) - 5) and tab[s + 1][w] == 'A' and tab[s + 2][w] == 'A' and tab[s + 3][w] == 'A' and tab[s + 4][w] == 0:
                i = i + 1
                turn = str(w) + ',' + str(s + 4) + '\0'
                tab[s + 4][w] = 'A'
                print(turn)
            elif s >= 4 and tab[s - 1][w] == 'A' and tab[s - 2][w] == 'A' and tab[s - 3][w] == 'A' and tab[s - 4][w] == 0:
                i = i + 1
                turn = str(w) + ',' + str(s - 4) + '\0'
                tab[s - 4][w] = 'A'
                print(turn)
            elif w <= (len(tab) - 5) and s <= (len(tab) - 5) and tab[s + 1][w + 1] == 'A' and tab[s + 2][w + 2] == 'A' and tab[s + 3][w + 3] == 'A' and tab[s + 4][w + 4] == 0:
                i = i + 1
                turn = str(w + 4) + ',' + str(s + 4) + '\0'
                tab[s + 4][w + 4] = 'A'
                print(turn)

            elif w >= 4 and s >= 4 and tab[s - 1][w - 1] == 'A' and tab[s - 2][w - 2] == 'A' and tab[s - 3][w - 3] == 'A' and tab[s - 4][w - 4] == 0:
                i = i + 1
                turn = str(w - 4) + ',' + str(s - 4) + '\0'
                tab[s - 4][w - 4] = 'A'
                print(turn)

            elif s <= (len(tab) - 5) and w >= 4 and tab[s + 1][w - 1] == 'A' and tab[s + 2][w - 2] == 'A' and tab[s + 3][w - 3] == 'A' and tab[s + 4][w - 4] == 0:
                i = i + 1
                turn = str(w - 4) + ',' + str(s + 4) + '\0'
                tab[s + 4][w - 4] = 'A'
                print(turn)

            elif w <= (len(tab) - 5) and s >= 4 and tab[s - 1][w + 1] == 'A' and tab[s - 2][w + 2] == 'A' and tab[s - 3][w + 3] == 'A' and tab[s - 4][w + 4] == 0:
                i = i + 1
                turn = str(w + 4) + ',' + str(s - 4) + '\0'
                tab[s - 4][w + 4] = 'A'
                print(turn)


        if w == (len(tab) - 1):
            w = 0
            s = s + 1
        w = w + 1
    if i == 0:
        check_if_trou1(tab, y, x)
        #check_if_win(tab, y, x)


def check_if_trou1(tab, y, x):
    i = 0
    nb = ''
    H = 0
    count = 0
    s = 0
    x = 0
    w = 0
    pas = 0
    while s < len(tab):
        if tab[s][w] == 'A' and i == 0:
            if w <= (len(tab) - 5) and i == 0:
                nb = str(tab[s][w + 1]) + str(tab[s][w + 2]) + str(tab[s][w + 3]) + str(tab[s][w + 4])
                count = 0
                x = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'A':
                        H = H + 1
                    if nb[count] == 'H':
                        pas = pas + 1
                    count = count + 1
                if H == 3 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)
                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1


                    w  = w + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
            if s <= (len(tab) - 5) and i == 0:
                nb = str(tab[s + 1][w]) + str(tab[s + 2][w]) + str(tab[s + 3][w]) + str(tab[s + 4][w])
                count = 0
                x = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'A':
                        H = H + 1
                    if nb[count] == 'H':
                        pas = pas + 1
                    count = count + 1
                if H == 3 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)

                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1


                    s = s + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
            if w <= (len(tab) - 5) and s <= (len(tab) - 5) and i == 0:
                nb = str(tab[s + 1][w + 1]) + str(tab[s + 2][w + 2]) + str(tab[s + 3][w + 3]) + str(tab[s + 4][w + 4])
                count = 0
                x = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'A':
                        H = H + 1
                    if nb[count] == 'H':
                        pas = pas + 1
                    count = count + 1
                if H == 3 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)

                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1


                    w = w + x
                    s = s + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
            if w >= 4 and s <= (len(tab) - 5) and i == 0:
                nb = str(tab[s + 1][w - 1]) + str(tab[s + 2][w - 2]) + str(tab[s + 3][w - 3]) + str(tab[s + 4][w - 4])
                count = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'A':
                        H = H + 1
                    if nb[count] == 'H':
                        pas = pas + 1
                    count = count + 1
                if H == 3 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)

                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1

                    #print (x)
                    w = w - x
                    s = s + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
        if w == (len(tab) - 1):
            w = 0
            s = s + 1
        w = w + 1
    if i == 0:
        check_if_win(tab, y, x)

def check_if_3_us_trou(tab, y, x):
    i = 0
    nb = ''
    H = 0
    count = 0
    s = 0
    x = 0
    w = 0
    pas = 0
    while s < len(tab):
        if tab[s][w] == 'A' and i == 0:
            if w <= (len(tab) - 5) and i == 0:
                nb = str(tab[s][w + 1]) + str(tab[s][w + 2]) + str(tab[s][w + 3])
                count = 0
                x = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'A':
                        H = H + 1
                    if nb[count] == 'H':
                        pas = pas + 1
                    count = count + 1
                if H == 2 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)
                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1


                    w  = w + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
            if s <= (len(tab) - 5) and i == 0:
                nb = str(tab[s + 1][w]) + str(tab[s + 2][w]) + str(tab[s + 3][w])
                count = 0
                x = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'A':
                        H = H + 1
                    if nb[count] == 'H':
                        pas = pas + 1
                    count = count + 1
                if H == 2 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)

                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1


                    s = s + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
            if w <= (len(tab) - 5) and s <= (len(tab) - 5) and i == 0:
                nb = str(tab[s + 1][w + 1]) + str(tab[s + 2][w + 2]) + str(tab[s + 3][w + 3])
                count = 0
                x = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'A':
                        H = H + 1
                    if nb[count] == 'H':
                        pas = pas + 1
                    count = count + 1
                if H == 2 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)

                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1


                    w = w + x
                    s = s + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
            if w >= 4 and s <= (len(tab) - 5) and i == 0:
                nb = str(tab[s + 1][w - 1]) + str(tab[s + 2][w - 2]) + str(tab[s + 3][w - 3])
                count = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'A':
                        H = H + 1
                    if nb[count] == 'H':
                        pas = pas + 1
                    count = count + 1
                if H == 2 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)

                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1

                    #print (x)
                    w = w - x
                    s = s + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
        if w == (len(tab) - 1):
            w = 0
            s = s + 1
        w = w + 1
    if i == 0:
        max_fct(tab, y, x)

def check_if_trou(tab, y, x):
    i = 0
    nb = ''
    H = 0
    count = 0
    s = 0
    x = 0
    w = 0
    pas = 0
    while s < len(tab):
        if tab[s][w] == 'H' and i == 0:
            if w <= (len(tab) - 5) and i == 0:
                nb = str(tab[s][w + 1]) + str(tab[s][w + 2]) + str(tab[s][w + 3]) + str(tab[s][w + 4])
                count = 0
                x = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'H':
                        H = H + 1
                    if nb[count] == 'A':
                        pas = pas + 1
                    count = count + 1
                if H == 3 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)
                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1


                    w  = w + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
            if s <= (len(tab) - 5) and i == 0:
                nb = str(tab[s + 1][w]) + str(tab[s + 2][w]) + str(tab[s + 3][w]) + str(tab[s + 4][w])
                count = 0
                x = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'H':
                        H = H + 1
                    if nb[count] == 'A':
                        pas = pas + 1
                    count = count + 1
                if H == 3 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)

                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1


                    s = s + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
            if w <= (len(tab) - 5) and s <= (len(tab) - 5) and i == 0:
                nb = str(tab[s + 1][w + 1]) + str(tab[s + 2][w + 2]) + str(tab[s + 3][w + 3]) + str(tab[s + 4][w + 4])
                count = 0
                x = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'H':
                        H = H + 1
                    if nb[count] == 'A':
                        pas = pas + 1
                    count = count + 1
                if H == 3 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)

                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1


                    w = w + x
                    s = s + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
            if w >= 4 and s <= (len(tab) - 5) and i == 0:
                nb = str(tab[s + 1][w - 1]) + str(tab[s + 2][w - 2]) + str(tab[s + 3][w - 3]) + str(tab[s + 4][w - 4])
                count = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'H':
                        H = H + 1
                    if nb[count] == 'A':
                        pas = pas + 1
                    count = count + 1
                if H == 3 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)

                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1

                    #print (x)
                    w = w - x
                    s = s + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
        if w == (len(tab) - 1):
            w = 0
            s = s + 1
        w = w + 1
    if i == 0:
        check_if_3(tab, y, x)

def check_if_win(tab, y, x):
    i = 0
    s = 0
    w = 0
    while s < len(tab):
        if tab[s][w] == 'H' and i == 0:
            if w <= (len(tab) - 5) and tab[s][w + 1] == 'H' and tab[s][w + 2] == 'H' and tab[s][w + 3] == 'H' and tab[s][w + 4] == 0:
                i = i + 1
                turn = str(w + 4) + ',' + str(s) + '\0'
                tab[s][w + 4] = 'A'
                print(turn)
            elif w >= 4 and tab[s][w - 1] == 'H' and tab[s][w - 2] == 'H' and tab[s][w - 3] == 'H' and tab[s][w - 4] == 0:
                i = i + 1
                turn = str(w - 4) + ',' + str(s) + '\0'
                tab[s][w - 4] = 'A'
                print(turn)
            elif s <= (len(tab) - 5) and tab[s + 1][w] == 'H' and tab[s + 2][w] == 'H' and tab[s + 3][w] == 'H' and tab[s + 4][w] == 0:
                i = i + 1
                turn = str(w) + ',' + str(s + 4) + '\0'
                tab[s + 4][w] = 'A'
                print(turn)
            elif s >= 4 and tab[s - 1][w] == 'H' and tab[s - 2][w] == 'H' and tab[s - 3][w] == 'H' and tab[s - 4][w] == 0:
                i = i + 1
                turn = str(w) + ',' + str(s - 4) + '\0'
                tab[s - 4][w] = 'A'
                print(turn)
            elif w <= (len(tab) - 5) and s <= (len(tab) - 5) and tab[s + 1][w + 1] == 'H' and tab[s + 2][w + 2] == 'H' and tab[s + 3][w + 3] == 'H' and tab[s + 4][w + 4] == 0:
                i = i + 1
                turn = str(w + 4) + ',' + str(s + 4) + '\0'
                tab[s + 4][w + 4] = 'A'
                print(turn)

            elif w >= 4 and s >= 4 and tab[s - 1][w - 1] == 'H' and tab[s - 2][w - 2] == 'H' and tab[s - 3][w - 3] == 'H' and tab[s - 4][w - 4] == 0:
                i = i + 1
                turn = str(w - 4) + ',' + str(s - 4) + '\0'
                tab[s - 4][w - 4] = 'A'
                print(turn)

            elif s <= (len(tab) - 5) and w >= 4 and tab[s + 1][w - 1] == 'H' and tab[s + 2][w - 2] == 'H' and tab[s + 3][w - 3] == 'H' and tab[s + 4][w - 4] == 0:
                i = i + 1
                turn = str(w - 4) + ',' + str(s + 4) + '\0'
                tab[s + 4][w - 4] = 'A'
                print(turn)

            elif w <= (len(tab) - 5) and s >= 4 and tab[s - 1][w + 1] == 'H' and tab[s - 2][w + 2] == 'H' and tab[s - 3][w + 3] == 'H' and tab[s - 4][w + 4] == 0:
                i = i + 1
                turn = str(w + 4) + ',' + str(s - 4) + '\0'
                tab[s - 4][w + 4] = 'A'
                print(turn)


        if w == (len(tab) - 1):
            w = 0
            s = s + 1
        w = w + 1
    if i == 0:
        check_if_trou(tab, y, x)

def check_if_3_trou(tab, y, x):
    i = 0
    nb = ''
    H = 0
    count = 0
    s = 0
    x = 0
    w = 0
    pas = 0
    while s < len(tab):
        if tab[s][w] == 'H' and i == 0:
            if w <= (len(tab) - 5) and i == 0:
                nb = str(tab[s][w + 1]) + str(tab[s][w + 2]) + str(tab[s][w + 3])
                count = 0
                x = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'H':
                        H = H + 1
                    if nb[count] == 'A':
                        pas = pas + 1
                    count = count + 1
                if H == 2 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)
                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1


                    w  = w + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
            if s <= (len(tab) - 5) and i == 0:
                nb = str(tab[s + 1][w]) + str(tab[s + 2][w]) + str(tab[s + 3][w])
                count = 0
                x = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'H':
                        H = H + 1
                    if nb[count] == 'A':
                        pas = pas + 1
                    count = count + 1
                if H == 2 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)

                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1


                    s = s + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
            if w <= (len(tab) - 5) and s <= (len(tab) - 5) and i == 0:
                nb = str(tab[s + 1][w + 1]) + str(tab[s + 2][w + 2]) + str(tab[s + 3][w + 3])
                count = 0
                x = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'H':
                        H = H + 1
                    if nb[count] == 'A':
                        pas = pas + 1
                    count = count + 1
                if H == 2 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)

                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1


                    w = w + x
                    s = s + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
            if w >= 4 and s <= (len(tab) - 5) and i == 0:
                nb = str(tab[s + 1][w - 1]) + str(tab[s + 2][w - 2]) + str(tab[s + 3][w - 3])
                count = 0
                pas = 0
                H = 0
                while count != len(nb):
                    if nb[count] == 'H':
                        H = H + 1
                    if nb[count] == 'A':
                        pas = pas + 1
                    count = count + 1
                if H == 2 and pas == 0:
                    i = i + 1
                    count = 0
                    nb  = str(nb)

                    while count < len(nb):
                        if nb[count] == '0':
                            x = count + 1
                        count = count + 1

                    #print (x)
                    w = w - x
                    s = s + x
                    turn = str(w) + ',' + str(s) + '\0'
                    tab[s][w] = 'A'
                    print(turn)
        if w == (len(tab) - 1):
            w = 0
            s = s + 1
        w = w + 1
    if i == 0:
        check_if_3_us(tab, y, x)

def check_if_3(tab, y, x):
    i = 0
    s = 0
    w = 0
    while s < len(tab):
        if tab[s][w] == 'H' and i == 0:
            if w <= (len(tab) - 5) and tab[s][w + 1] == 'H' and tab[s][w + 2] == 'H' and tab[s][w + 3] == 0 and tab[s][w + 4] != 'A':
                i = i + 1
                turn = str(w + 3) + ',' + str(s) + '\0'
                tab[s][w + 3] = 'A'
                print(turn)
            elif w >= 4 and tab[s][w - 1] == 'H' and tab[s][w - 2] == 'H' and tab[s][w - 3] == 0 and tab[s][w - 4] != 'A':
                i = i + 1
                turn = str(w - 3) + ',' + str(s) + '\0'
                tab[s][w - 3] = 'A'
                print(turn)
            elif s <= (len(tab) - 5) and tab[s + 1][w] == 'H' and tab[s + 2][w] == 'H' and tab[s + 3][w] == 0 and tab[s + 4][w] != 'A':
                i = i + 1
                turn = str(w) + ',' + str(s + 3) + '\0'
                tab[s + 3][w] = 'A'
                print(turn)
            elif s >= 4 and tab[s - 1][w] == 'H' and tab[s - 2][w] == 'H' and tab[s - 3][w] == 0 and tab[s - 4][w] != 'A':
                i = i + 1
                turn = str(w) + ',' + str(s - 3) + '\0'
                tab[s - 3][w] = 'A'
                print(turn)
            elif w <= (len(tab) - 5) and s <= (len(tab) - 5) and tab[s + 1][w + 1] == 'H' and tab[s + 2][w + 2] == 'H' and tab[s + 3][w + 3] == 0 and tab[s + 4][w + 4] != 'A':
                i = i + 1
                turn = str(w + 3) + ',' + str(s + 3) + '\0'
                tab[s + 3][w + 3] = 'A'
                print(turn)

            elif w >= 4 and s >= 4 and tab[s - 1][w - 1] == 'H' and tab[s - 2][w - 2] == 'H' and tab[s - 3][w - 3] == 0 and tab[s - 4][w - 4] != 'A':
                i = i + 1
                turn = str(w - 3) + ',' + str(s - 3) + '\0'
                tab[s - 3][w - 3] = 'A'
                print(turn)

            elif s <= (len(tab) - 5) and w >= 4 and tab[s + 1][w - 1] == 'H' and tab[s + 2][w - 2] == 'H' and tab[s + 3][w - 3] == 0 and tab[s + 4][w - 4] != 'A':
                i = i + 1
                turn = str(w - 3) + ',' + str(s + 3) + '\0'
                tab[s + 3][w - 3] = 'A'
                print(turn)

            elif w <= (len(tab) - 5) and s >= 4 and tab[s - 1][w + 1] == 'H' and tab[s - 2][w + 2] == 'H' and tab[s - 3][w + 3] == 0 and tab[s - 4][w + 4] != 'A':
                i = i + 1
                turn = str(w + 3) + ',' + str(s - 3) + '\0'
                tab[s - 3][w + 3] = 'A'
                print(turn)


        if w == (len(tab) - 1):
            w = 0
            s = s + 1
        w = w + 1
    if i == 0:
        check_if_3_trou(tab, y, x)

def check_if_3_us (tab, y, x):
    i = 0
    s = 0
    w = 0
    while s < len(tab):
        if tab[s][w] == 'A' and i == 0:
            if w <= (len(tab) - 5) and tab[s][w + 1] == 'A' and tab[s][w + 2] == 'A' and tab[s][w + 3] == 0 and tab[s][w + 4] != 'H':
                i = i + 1
                turn = str(w + 3) + ',' + str(s) + '\0'
                tab[s][w + 3] = 'A'
                print(turn)
            elif w >= 4 and tab[s][w - 1] == 'A' and tab[s][w - 2] == 'A' and tab[s][w - 3] == 0 and tab[s][w - 4] != 'H':
                i = i + 1
                turn = str(w - 3) + ',' + str(s) + '\0'
                tab[s][w - 3] = 'A'
                print(turn)
            elif s <= (len(tab) - 5) and tab[s + 1][w] == 'A' and tab[s + 2][w] == 'A' and tab[s + 3][w] == 0 and tab[s + 4][w] != 'H':
                i = i + 1
                turn = str(w) + ',' + str(s + 3) + '\0'
                tab[s + 3][w] = 'A'
                print(turn)
            elif s >= 4 and tab[s - 1][w] == 'A' and tab[s - 2][w] == 'A' and tab[s - 3][w] == 0 and tab[s - 4][w] != 'H':
                i = i + 1
                turn = str(w) + ',' + str(s - 3) + '\0'
                tab[s - 3][w] = 'A'
                print(turn)
            elif w <= (len(tab) - 5) and s <= (len(tab) - 5) and tab[s + 1][w + 1] == 'A' and tab[s + 2][w + 2] == 'A' and tab[s + 3][w + 3] == 0 and tab[s + 4][w + 4] != 'H':
                i = i + 1
                turn = str(w + 3) + ',' + str(s + 3) + '\0'
                tab[s + 3][w + 3] = 'A'
                print(turn)

            elif w >= 4 and s >= 4 and tab[s - 1][w - 1] == 'A' and tab[s - 2][w - 2] == 'A' and tab[s - 3][w - 3] == 0 and tab[s - 4][w - 4] != 'H':
                i = i + 1
                turn = str(w - 3) + ',' + str(s - 3) + '\0'
                tab[s - 3][w - 3] = 'A'
                print(turn)

            elif s <= (len(tab) - 5) and w >= 4 and tab[s + 1][w - 1] == 'A' and tab[s + 2][w - 2] == 'A' and tab[s + 3][w - 3] == 0 and tab[s + 4][w - 4] != 'H':
                i = i + 1
                turn = str(w - 3) + ',' + str(s + 3) + '\0'
                tab[s + 3][w - 3] = 'A'
                print(turn)

            elif w <= (len(tab) - 5) and s >= 4 and tab[s - 1][w + 1] == 'A' and tab[s - 2][w + 2] == 'A' and tab[s - 3][w + 3] == 0 and tab[s - 4][w + 4] != 'H':
                i = i + 1
                turn = str(w + 3) + ',' + str(s - 3) + '\0'
                tab[s - 3][w + 3] = 'A'
                print(turn)


        if w == (len(tab) - 1):
            w = 0
            s = s + 1
        w = w + 1
    if i == 0:
        check_if_3_us_trou(tab, y, x)

def put_pion(tab, s, w):

    if (w != (len(tab) - 1) and w != 0 and tab[s][w + 1] == 0):
        tab[s][w + 1] = 'A'
        w = w + 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif (w != 0 and w != (len(tab) - 1) and tab[s][w - 1] == 0):
        tab[s][w - 1] = 'A'
        w = w - 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif (s != 0 and s != (len(tab) - 1) and tab[s + 1][w] == 0) :
        tab[s + 1][w] = 'A'
        s = s + 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif (s != 0 and s != (len(tab) - 1) and tab[s - 1][w] == 0):
        tab[s - 1][w] = 'A'
        s = s - 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif (w != 0 and s != 0 and w != (len(tab) - 1) and s != (len(tab) - 1) and tab[s - 1][w - 1] == 0):
        tab[s - 1][w - 1] = 'A'
        s = s - 1
        w = w - 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif (s != 0 and s != (len(tab) - 1) and w != 0 and w != (len(tab) - 1) and tab[s - 1][w + 1] == 0):
        tab[s - 1][w + 1] = 'A'
        s = s - 1
        w = w + 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif (s != (len(tab) - 1) and s != 0 and w != (len(tab) - 1) and w != 0 and tab[s + 1][w + 1] == 0):
        tab[s + 1][w + 1] = 'A'
        s = s + 1
        w = w + 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif ( w != 0 and w != (len(tab) - 1) and s != (len(tab) - 1) and s != 0 and tab[s + 1][w - 1] == 0):
        tab[s + 1][w - 1] = 'A'
        s = s + 1
        w = w - 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    else:
        a = randint(0, l)
        b = randint(0, l)
        while tab[a][b] != 0:
            a = randint(0, l)
            b = randint(0, l)
        tab[a][b] = 'A'
        turn = str(b) + ',' + str(a) + '\0'
        print (turn)

def optimization_play(tab, l):

    a = 0
    b = 0
    i = 0

    while a != l:
        if tab[a][b] == 'A':
            i = i + 1
        if b == l:
            b = 0
            a = a + 1
        b = b + 1
    if i != 0:
        a = 0
        b = 0
        while a != l:
            if tab[a][b] == 'A':
                put_pion(tab, a, b)
                break
            if b == l:
                b = 0
                a = a + 1
            b = b + 1
    else:
        a = randint(0, l)
        b = randint(0, l)
        while tab[a][b] != 0:
            a = randint(0, l)
            b = randint(0, l)
        tab[a][b] = 'A'
        turn = str(b) + ',' + str(a) + '\0'
        print (turn)


def max_fct(tab, s, w):
    if (w != (len(tab) - 1) and w != 0 and tab[s][w - 1] == 'H' and tab[s][w + 1] == 0):
        tab[s][w + 1] = 'A'
        w = w + 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif (w != 0 and w != (len(tab) - 1) and tab[s][w + 1] == 'H' and tab[s][w - 1] == 0):
        tab[s][w - 1] = 'A'
        w = w - 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif (s != 0 and s != (len(tab) - 1) and tab[s - 1][w] == 'H' and tab[s + 1][w] == 0) :
        tab[s + 1][w] = 'A'
        s = s + 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif (s != 0 and s != (len(tab) - 1) and tab[s + 1][w] == 'H' and tab[s - 1][w] == 0):
        tab[s - 1][w] = 'A'
        s = s - 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif (w != 0 and s != 0 and w != (len(tab) - 1) and s != (len(tab) - 1) and tab[s + 1][w + 1] == 'H' and tab[s - 1][w - 1] == 0):
        tab[s - 1][w - 1] = 'A'
        s = s - 1
        w = w - 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif (s != 0 and s != (len(tab) - 1) and w != 0 and w != (len(tab) - 1) and tab[s + 1][w - 1] == 'H' and tab[s - 1][w + 1] == 0):
        tab[s - 1][w + 1] = 'A'
        s = s - 1
        w = w + 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif (s != (len(tab) - 1) and s != 0 and w != (len(tab) - 1) and w != 0 and tab[s - 1][w - 1] == 'H' and tab[s + 1][w + 1] == 0):
        tab[s + 1][w + 1] = 'A'
        s = s + 1
        w = w + 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    elif ( w != 0 and w != (len(tab) - 1) and s != (len(tab) - 1) and s != 0 and tab[s - 1][w + 1] == 'H' and tab[s + 1][w - 1] == 0):
        tab[s + 1][w - 1] = 'A'
        s = s + 1
        w = w - 1
        turn = str(w) + ',' + str(s) + '\0'
        print (turn)
    else:
        optimization_play(tab, l)
        #s = 0
        #w = 0
        #while tab[s][w] != 0:
         #   S = randint(0, (len(tab) - 1))
         #   w = randint(0, (len(tab) - 1))
        #tab[s][w] = 'A'
        #turn = str(s) + ',' + str(w) + '\0'
        #print (turn)

def turn(tab, line, l):
    xy = line[1].split(',')
    tab[int(xy[1])][int(xy[0])] = 'H'
    check_if_loose(tab, int(xy[1]), int(xy[0]))
    #tab_printer(tab)
    #check_if_trou(tab, 0, 0)
    #max_fct(tab, int(xy[1]), int(xy[0]))
    #tab_printer(tab)

    # min_fct(tab, int(xy[1]), int(xy[0]))
    # random_play(tab, l, tab)


while True:
        inp = input()
        if inp.split():
            line = inp.split()
            if line[0] == "START":
                if int(line[1]) > 5:
                    l = int(line[1])
                    l = l - 1
                    tab = [[0 for r in range(l + 1)] for c in range(l + 1)]
                    print ("OK")
                else:
                    print ("ERROR message - unsupported size or other error")
            elif line[0] == "BEGIN":
                begin(tab, l)
            elif line[0] == "INFO":
                #info(tab, l)
                p = "INFO"
            elif line[0] == "BOARD":
                board(tab, l, inp, line)
                max_fct(tab, 0, 0)
            elif line[0] == "TURN":
                turn(tab, line, l)
                #tab_printer(tab)
            elif line[0] == "RESTART":
                tab = [[0 for r in range(l + 1)] for c in range(l + 1)]
                print ("OK")
            elif line[0] == "END":
                exit (0)
            else:
                print ("UNKNOWN COMMAND " + line[0])
            # s = 0
            # while s < l + 1:
            #     print (tab[s])
            #     s = s + 1
        else:
            print ("UNKNOWN COMMAND")
