from pygame.sprite import Sprite, collide_rect
import pygame

speed = 8 
JumpRange = 10

gravity = 0.5

class Player(Sprite): #класс Player наследует методы класса Sprite и является дочерним классом по отн. к нему
    def __init__(self, x, y, player): #координаты и персонаж
        Sprite.__init__(self)
        self.image = pygame.image.load(player)#отображение героя
        self.xvel = 0 #скорость по х
        self.yvel = 0 #скорость по y
        self.rect = self.image.get_rect() #выделение прямоугольной области для героя
        self.rect.x = x # соответствующаяя координата, rect добавлен, для того чтобы игрок "воспринимался" программой как прямоугольник
        self.rect.y = y
        self.onGround = False #находится ли игрок на земле (на поверхности)
        self.isFinish = False

    def update(self, left, right, up, platforms, prizes): #метод обновления положения игрока
        if left: # движется ли влево
            self.xvel = -speed #скорость "отрицательна", т.к. координаты уменьшаются
        if right:
            self.xvel = speed
        if not(left or right):
            self.xvel = 0

        if up:
            if self.onGround:
                self.yvel = -JumpRange #если игрок на земле и собирается прыгнуть, то координаты по y вычитаются

        if not self.onGround:
            self.yvel += gravity #если игрок в воздухе и уже прыгнул, то он падает - координаты прибавляются по y

        self.onGround = False
        self.rect.x += self.xvel #перемещение по х
        self.collide(self.xvel, 0, platforms)#выполнение проверки на столкновение с платформой по х
        self.prize(self.xvel, 0, prizes)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)#выполнение проверки на столкновение с платформой по y
        self.prize(0, self.yvel, prizes)

    def collide(self, xvel, yvel, platforms): #метод проверяющий на столкновение игрока с платформой^^^
        for pl in platforms: #проходимся по всему списку платформ
            if collide_rect(self, pl):
                if xvel > 0:
                    self.rect.right = pl.rect.left # если произошло столкновение и скорость по х была +, то игрок столкнулся с левой стенкой платформы =>
                    #=> выполняется спец. метод столкновения с лев. стенкой объекта
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top # если произошло столкновение и скорость по y была +, то игрок столкнулся с верхней стенкой платформы =>
                    #=> выполняется спец. метод столкновения с верх. стенкой объекта и =>
                    self.onGround = True #=> игрок на земле (на поверхности)
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                    self.yvel = 0
    def prize (self, xvel, yvel, prizes):
        for pr in prizes: #проходимся по всему списку платформ
            if collide_rect(self, pr):
                if xvel > 0:
                    self.rect.right = pr.rect.left # если произошло столкновение и скорость по х была +, то игрок столкнулся с левой стенкой платформы =>
                    #=> выполняется спец. метод столкновения с лев. стенкой объекта
                if xvel < 0:
                    self.rect.left = pr.rect.right
                if yvel > 0:
                    self.rect.bottom = pr.rect.top # если произошло столкновение и скорость по y была +, то игрок столкнулся с верхней стенкой платформы =>
                    #=> выполняется спец. метод столкновения с верх. стенкой объекта и =>
                    self.onGround = True #=> игрок на земле (на поверхности)
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = pr.rect.bottom
                    self.yvel = 0
                self.isFinish = True
