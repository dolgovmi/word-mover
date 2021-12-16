import pygame

pygame.init()
from pygame.color import THECOLORS

window = [940, 780]
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Лабиринт")
screen.fill(THECOLORS["white"])
hero = pygame.image.load("player.png")
prize = pygame.image.load("prize.png")
door = pygame.image.load("door.png")
wall = pygame.image.load("wall.png")
road = pygame.image.load("road.png")
C_A = pygame.image.load("A.jpg")
t_is = pygame.image.load('is.jpg')
you = pygame.image.load('you.jpg')


class Items(object):

    def __init__(self):
        self.items = {}

    def print(self):
        print("---")
        for id in self.items:
            print(id)
            self.items[id].print()

    def is_movable(self, name):
        if name == 'wall':
            return False
        return True

    def is_crossable(self, name):
        if name == 'wall':
            return False
        return True

    def add(self, id, item):
        self.items[id] = item

    def map(self):
        map_list = [0] * 10
        for i in range(10):
            map_list[i] = [0] * 10
        for id in self.items:
            item = self.items[id]
            map_list[item.x][item.y] = int(item.t)
        return map_list


class Item(object):

    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t
        name = ""
        if cell == "1":
            name = 'wall'
        if cell == "2":
            name = 'player'
        if cell == "3":
            name = 'coin'
        if cell == "4":
            name = 'door'
        if cell == "5":
            name = 'a'
        if cell == "6":
            name = 'is'
        if cell == "7":
            name = 'you'
        self.name = name

    def print(self):
        print(self.x, self.y, self.name)


map_file = open("map.txt", "r")
items = Items()

lines = map_file.readlines()

id = 0
x = 0
for line in lines:
    y = 0
    cells = line.split()
    for cell in cells:
        if cell != "0":
            item = Item(x, y, cell)
            items.add(id, item)
            id += 1
        y += 1
    x += 1
map_list = items.map()

# id = 1
# for item in list:
#    print(item)


# for i in range(10):
#   s = map_file.readline()
#  list = s.split()
# for j in range(10):
#    if __name__ == "0":
#       car = item(, 5, 4)
#      print(car.color)
map_file.close()

ik = 0
jk = 0
remember = 0
nx = 100
ny = 100
dx = 64
dy = 64
my_font = pygame.font.SysFont("impact", 24)
text = my_font.render("", True, THECOLORS["red"])

print(map_list)


def draw_maze(map_list, nx, ny, dx, dy, ik, jk, remember):
    for i in range(10):
        for j in range(10):
            x = nx + dx * j
            y = ny + dy * i
            if map_list[i][j] == 0:
                screen.blit(road, [x, y])
            elif map_list[i][j] == 1:
                screen.blit(road, [x, y])
                screen.blit(wall, [x, y])
            elif map_list[i][j] == 2:
                screen.blit(road, [x, y])
                screen.blit(hero, [x, y])
                ik = i
                jk = j
            elif map_list[i][j] == 3:
                screen.blit(prize, [x, y])
            elif map_list[i][j] == 4:
                screen.blit(door, [x, y])
            elif map_list[i][j] == 5:
                screen.blit(C_A, [x, y])
            elif map_list[i][j] == 6:
                screen.blit(t_is, [x, y])
            elif map_list[i][j] == 7:
                screen.blit(you, [x, y])
    return (ik, jk)


run = True
while run == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            screen.fill(THECOLORS["white"])
            ik, jk = draw_maze(map_list, nx, ny, dx, dy, ik, jk, remember)
            pygame.display.update()
    pygame.display.update()

pygame.time.delay(1000)
screen = pygame.display.set_mode([400, 600])
