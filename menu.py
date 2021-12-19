import pygame

pygame.init()
from pygame.color import THECOLORS


def menu():
    window = [400, 600]
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption("Word Mover")
    background = pygame.Surface(screen.get_size())
    x = 100
    y = [60, 210, 360, 510]
    width = 200
    height = 80
    menu_list = ["Играть", "Помощь", "", "Выход"]
    my_font = pygame.font.SysFont("arial", 40)
    run = True
    j = 5
    while run:
        background.fill(THECOLORS["black"])
        for i in range(4):
            pygame.draw.rect(background, THECOLORS["darkgray"], [x, y[i], width, height])
            pygame.draw.rect(background, THECOLORS["black"], [x, y[i], width, height], 4, 20)
            text = my_font.render(menu_list[i], True, THECOLORS["white"])
            background.blit(text, [x + 30, y[i] + 30])

        text = my_font.render("Word Mover", True, THECOLORS["red"])
        background.blit(text, [110, 10])
        screen.blit(background, [0, 0])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                for j in range(4):

                    if (xm > x) and (xm < x + width) and (ym > y[j]) and (ym < y[j] + height):
                        break
                    else:
                        j = 5

                if j == 0:
                    import Levels
                    Levels.select()
                elif j == 1:
                    import help
                    help.help()
                elif j == 2:
                    print("")
                elif j == 3:
                    run = False

    quit()


menu()
