import pygame
pygame.init()
from pygame.color import THECOLORS
def game():
    window = [940,780]
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption("Лабиринт")
    screen.fill(THECOLORS["white"])
    hero=pygame.image.load("player.png")
    prize=pygame.image.load("prize.png")
    door=pygame.image.load("door.png")
    wall=pygame.image.load("wall.png")
    road=pygame.image.load("road.png")
    C_A=pygame.image.load("A.jpg")
    t_is=pygame.image.load('is.jpg')
    you=pygame.image.load('you.jpg')
    remember = 1
    nx = 100
    ny = 100
    dx = 64
    dy = 64
    score = 0
    prize_count = 7
    time = 300
    win = False
    up = down = left = right = False
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    my_font = pygame.font.SysFont("impact", 24)
    text = my_font.render("",True,THECOLORS["red"])
    map_list = [0]*10
    print(map_list)
    for i in range(10):
        map_list[i] = [0]*10
        print(map_list[i])
    map_file = open("map.txt", "r")
    for i in range(10):
        s = map_file.readline()
        list = s.split()
        for j in range(10):
            map_list[i][j] = int(list[j])
            print(map_list[i][j], end=" ")
        print()
    map_file.close()


    stop = [0]
    push = [5, 6, 7]

    def draw_maze(map_list,nx, ny, dx, dy, ik, jk, text, remember):
        for i in range(10):
            for j in range(10):
                x = nx + dx*j
                y = ny + dy*i
                if map_list[i][j] == 0:
                    screen.blit(road, [x, y])
                    screen.blit(wall, [x,y])
                elif map_list[i][j] == 1:
                    screen.blit(road, [x,y])
                elif map_list[i][j] == 2:
                    if remember == 3:
                        screen.blit(prize, [x,y])
                    screen.blit(road, [x,y])
                    screen.blit(hero, [x,y])
                    ik = i
                    jk = j
                elif map_list[i][j] == 3:
                    screen.blit(prize, [x,y])
                elif map_list[i][j] == 4:
                    screen.blit(door, [x,y])
                elif map_list[i][j] == 5:
                    screen.blit(C_A, [x,y])
                elif map_list[i][j] == 6:
                    screen.blit(t_is, [x,y])
                elif map_list[i][j] == 7:
                    screen.blit(you, [x,y])

        score_text = my_font.render("Собрано призов: " + str(score), True, THECOLORS["blue"])
        time_text = my_font.render("Оставшееся время: " + str(time)+ " c.", True, THECOLORS["blue"])
        screen.blit(score_text, [400, 10])
        screen.blit(time_text,[400,40])
        screen.blit(text, [400,70])
        pygame.display.update()
        return (ik, jk)
    def analysis_key(ik,jk,i,j, up, down, left, right):
        if event.key == pygame.K_UP:
            up = True
            down = left = right = False
            if(ik > 0):
                i = ik - 1
        elif event.key == pygame.K_DOWN:
            down = True
            up = left = right = False
            if (ik < 9):
                i=ik+1
        elif event.key == pygame.K_LEFT:
            left = True
            up = down = right = False
            if (jk > 0):
                j = jk -1
        elif event.key == pygame.K_RIGHT:
            right = True
            up = left = down = False
            if (jk < 9):
                j = jk+1
        return (i,j, up, down, left, right)
    def move_maze(map_list, ik, jk, i, j, score, text, win, remember, up, down, left, right):
        if (map_list[i][j] == 0):
            i=ik
            j=jk
        elif (map_list[i][j]==1):
            map_list[i][j] = 2
            map_list[ik][jk] = remember
            remember = 1
            ik = i
            jk = j
        elif (map_list[i][j]==3):
            map_list[i][j] = 2
            map_list[ik][jk] = remember
            remember = 3
            ik = i
            jk = j
            score+=1
        elif (map_list[i][j] == 4):
            if (score < prize_count):
                text = my_font.render("Собраны не все призы!", True, THECOLORS["red"])
            else:
                map_list[i][j] = 2
                map_list[ik][jk] = 1
                ik = i
                jk = j
                win = True
                text = my_font.render("Ура победа!", True, THECOLORS["red"])
        elif (map_list[i][j] == 5):

            map_list[i][j] = 2
            map_list[ik][jk] = remember
            remember = 1
            ik = i
            jk = j
            if up == True:
                #if (map_list[i-1][j] in push):

                if (map_list[i-1][j] != 0):
                    map_list[i-1][j] = 5
                else:
                    i += 1
                    map_list[i][j] = 2
                    map_list[i - 1][j] = 5




        elif (map_list[i][j] == 6):
            map_list[i][j] = 2

        elif (map_list[i][j] == 7):
            map_list[i][j] = 2

        return map_list, ik, jk, i, j, score, text, win, remember

    ik = 0
    jk = 0
    i = ik
    j = jk
    run = True
    ik, jk = draw_maze(map_list,nx, ny, dx, dy, ik, jk,text, win, remember)

    while run == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                i,j, up, down, left, right = analysis_key(ik, jk, i, j, up, down, left, right)
                map_list, ik, jk, i, j, score, text, win, remember = move_maze(map_list, ik, jk, i, j, score, text, win, remember, up, down, left, right)
            elif event.type == pygame.USEREVENT:
                time = time-1
        if time == 0:
            text = my_font.render("Время вышло!", True, THECOLORS["red"])
            run = False
        if win == True:
            text = my_font.render("Ура победа!", True, THECOLORS["red"])
            run = False

        screen.fill(THECOLORS["white"])
        ik, jk = draw_maze(map_list, nx, ny, dx, dy, ik, jk, text, win, remember)
        pygame.display.update()
    pygame.time.delay(1000)
    screen = pygame.display.set_mode([400, 600])
