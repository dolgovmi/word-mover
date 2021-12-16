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
        self.coins = 0

    def print(self):
        print("---")
        for id in self.items:
            print(id)
            self.items[id].print()

    def is_movable(self, name):
        if name == 'wall':
            return False
        return True

    def is_crossable(self, id):
        item = self.items[id]
        if item.t == '1':
            return False
        return True

    def is_collectable(self, id):
        item = self.items[id]
        if item.t == '3':
            return True
        return False

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

    def get_items(self, x, y):
        result = {}
        for id in self.items:
            item = self.items[id]
            if x == item.x and y == item.y:
                result[id] = item
        return result

    def get_player_id(self):
        for id in self.items:
            item = self.items[id]
            if item.t == '2':
                return id



    def move(self, id, direction):
        item = self.items[id]
        x = item.x
        y = item.y
        if direction == 'up':
            x -= 1
            if x < 0:
                x = 0
        if direction == 'down':
            x += 1
            if x > 9:
                x = 9
        if direction == 'left':
            y -= 1
            if y < 0:
                y = 0
        if direction == 'right':
            y += 1
            if y > 9:
                y = 9
        next_items = self.get_items(x, y)
        for next_item_id in next_items:
            if not self.is_crossable(next_item_id):
                return False
            if self.is_collectable(next_item_id):
                del self.items[next_item_id]
                self.coins += 1
        item.x = x
        item.y = y
        self.items[id] = item
        return True

    def get_coins(self):
        return self.coins




class Item(object):

    def __init__(self, x, y, t, text):
        self.x = x
        self.y = y
        self.t = t
        name = ""
        if t == "1":
            name = 'wall'
        if t == "2":
            name = 'player'
        if t == "3":
            name = 'coin'
        if t == "4":
            name = 'door'
        if t == "5":
            name = 'a'
        if t == "6":
            name = 'is'
        if t == "7":
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
            item = Item(x, y, cell, '')
            items.add(id, item)
            id += 1
        y += 1
    x += 1


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
my_font = pygame.font.SysFont("impact", 40)
text = my_font.render("", True, THECOLORS["red"])


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
    score_text = my_font.render("Собрано призов: " + str(items.coins), True, THECOLORS["blue"])
    screen.blit(score_text, [400, 10])
    return (ik, jk)

screen.fill(THECOLORS["white"])
run = True
id = items.get_player_id()
while run == True:

    is_game_changed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                is_game_changed = items.move(id, 'up')
            if event.key == pygame.K_DOWN:
                is_game_changed = items.move(id, 'down')
            if event.key == pygame.K_LEFT:
                is_game_changed = items.move(id, 'left')
            if event.key == pygame.K_RIGHT:
                is_game_changed = items.move(id, 'right')
        if is_game_changed:
            screen.fill(THECOLORS["white"])
            map_list = items.map()
            ik, jk = draw_maze(map_list, nx, ny, dx, dy, ik, jk, remember)
            pygame.display.update()
    pygame.display.update()

pygame.time.delay(1000)
screen = pygame.display.set_mode([400, 600])
