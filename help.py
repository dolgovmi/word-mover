import pygame
pygame.init()
from pygame.color import THECOLORS
def help():
    run = True
    x = 20
    y = 10
    window = [600, 600]
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption('Помощь')
    background = pygame.Surface(screen.get_size())
    background.fill(THECOLORS["black"])
    help_file = open('help.txt', 'r', encoding='utf-8')
    mylist = help_file.readlines()
    myfont = pygame.font.SysFont('arial', 20)
    help_file.close()
    for i in range(len(mylist)):
        s = mylist[i]
        s = s.rstrip()
        text = myfont.render(s, True, THECOLORS['green'])
        background.blit(text, [x, y])
        y += 20
    text = myfont.render('Нажмите любую клавишу', True, THECOLORS['green'])
    background.blit(text, [x, y+50])
    screen.blit(background, [0, 0])
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                run = False
        pygame.display.update()
    screen = pygame.display.set_mode([400, 600])