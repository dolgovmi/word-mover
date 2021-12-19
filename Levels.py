import pygame, pickle
pygame.init()
from pygame.color import THECOLORS
def select():
    window = [660, 800]
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption("Word Mover")
    background = pygame.Surface(screen.get_size())
    x = 100
    y = [60, 210, 360, 510, 660, 60, 210, 360, 510, 660]
    width = 200
    height = 80
    menu_list = ["Уровень 1", 'Уровень 2',
                 "Уровень 3", 'Уровень 4',
                 "Уровень 5", 'Уровень 6',
                 "Уровень 7", 'Уровень 8',
                 "Уровень 9", 'Уровень 10']
    my_font = pygame.font.SysFont("arial", 35)
    run = True
    j = 11
    x2 = x + 250
    while run:
        background.fill(THECOLORS["black"])
        for i in range(5):
            pygame.draw.rect(background, THECOLORS["darkgray"], [x, y[i], width, height])
            pygame.draw.rect(background, THECOLORS["black"], [x, y[i], width, height], 4, 20)
            text = my_font.render(menu_list[i], True, THECOLORS["white"])
            background.blit(text, [x + 30, y[i] + 30])
        for i in range(5, 10):
            pygame.draw.rect(background, THECOLORS["darkgray"], [x2, y[i], width, height])
            pygame.draw.rect(background, THECOLORS["black"], [x2, y[i], width, height], 4, 20)
            text = my_font.render(menu_list[i], True, THECOLORS["white"])
            background.blit(text, [x2 + 30, y[i] + 30])
        text = my_font.render("Выберите уровень", True, THECOLORS["red"])
        background.blit(text, [200, 10])
        screen.blit(background, [0, 0])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import menu
                menu.menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                for j in range(5):
                    if ((xm > x) and (xm < x + width) and (ym > y[j]) and (ym < y[j] + height)):
                        break
                else:
                    for j in range(5, 10):
                        if ((xm > x2) and (xm < x2 + width) and (ym > y[j]) and (ym < y[j] + height)):
                            break
                        else:
                            j = 11

                if (j == 0):
                    pickle_file = open('Level.txt', 'w')
                    Level = '1'
                    pickle_file.write(Level)
                    pickle_file.close()
                    import Sokoban
                    Sokoban.game()
                elif (j == 1):
                    pickle_file = open('Level.txt', 'w')
                    Level = '2'
                    pickle_file.write(Level)
                    pickle_file.close()
                    import Sokoban
                    Sokoban.game()
                elif (j == 2):
                    pickle_file = open('Level.txt', 'w')
                    Level = '3'
                    pickle_file.write(Level)
                    pickle_file.close()
                    import Sokoban
                    Sokoban.game()
                elif (j == 3):
                    pickle_file = open('Level.txt', 'w')
                    Level = '4'
                    pickle_file.write(Level)
                    pickle_file.close()
                    import Sokoban
                    Sokoban.game()
                elif (j == 4):
                    pickle_file = open('Level.txt', 'w')
                    Level = '5'
                    pickle_file.write(Level)
                    pickle_file.close()
                    import Sokoban
                    Sokoban.game()
                elif (j == 5):
                    pickle_file = open('Level.txt', 'w')
                    Level = '6'
                    pickle_file.write(Level)
                    pickle_file.close()
                    import Sokoban
                    Sokoban.game()
                elif (j == 6):
                    pickle_file = open('Level.txt', 'w')
                    Level = '7'
                    pickle_file.write(Level)
                    pickle_file.close()
                    import Sokoban
                    Sokoban.game()
                elif (j == 7):
                    pickle_file = open('Level.txt', 'w')
                    Level = '8'
                    pickle_file.write(Level)
                    pickle_file.close()
                    import Sokoban
                    Sokoban.game()
                elif (j == 8):
                    pickle_file = open('Level.txt', 'w')
                    Level = '9'
                    pickle_file.write(Level)
                    pickle_file.close()
                    import Sokoban
                    Sokoban.game()
                elif (j == 9):
                    pickle_file = open('Level.txt', 'w')
                    Level = '10'
                    pickle_file.write(Level)
                    pickle_file.close()
                    import Sokoban
                    Sokoban.game()



