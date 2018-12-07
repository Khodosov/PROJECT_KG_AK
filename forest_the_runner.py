import pygame
from levels import l1, l2, l3, l4, l5, l6, l7, l8, l9, Platform  # li (1<=i<=9)
#  - это список платформ - уровень, из файла levels.py.
#  Platform - класс платформ
from players import Player  # Player - класс игроков

pygame.init()
win = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Guk & Khodosov prod.")
# ============================================================================
bg = pygame.image.load('win.jpg')
logo = pygame.image.load('new_logo.jpg')
lvl_p_win = pygame.image.load('histranger.jpg')
player2 = ('find1.png')
player1 = ('geo.png')
pl1win = pygame.image.load('1win.jpg')
pl2win = pygame.image.load('2win.jpg')
limit = ('lim.png')  # Картинка для платформы
x1 = 5
y1 = 655
up1 = False  # Переменная, отвечающаяя на вопрос, находится ли игрок1 в прыжке
x2 = 5
y2 = 655
up2 = False  # Переменная, отвечающаяя на вопрос, находится ли игрок2 в прыжке
# След. две переменные запихиваем в класс Player
# (соотв-но они теперь обладают всеми свойствами класса)
pl2 = Player(x2, y2, player2)
pl1 = Player(x1, y1, player1)
# ============================================================================
left1 = left2 = right1 = right2 = False  # переменные, отвечающие, движется
#                                               ли игрок вправо/влево

# Intro ======================================================================
pygame.mixer.music.load('opening.mp3')
pygame.mixer.music.play(-1)
skip = 0
while skip < 450:  # 450
    win.blit(logo, (0, 0))
    pygame.display.update()
    skip += 1
skip = 0
# Чудесная композиция ========================================================
pygame.mixer.music.load('Pskov.mp3')
pygame.mixer.music.play(-1)
# ============================================================================
sprite_group = pygame.sprite.Group()  # переменная (группа), в которой
# содержатся все элементы класса Sprite (и игроки, и платформы)
# ============================================================================
# Добавление в группу каждого игрока:
sprite_group.add(pl1)
sprite_group.add(pl2)
platforms = []  # Список всех платформ в конкретном уровне
# lev = l9 .  l9 выбрано для примера.
# Саша, напиши код так, чтобы в зависимости от нажатой кнопки (1, 2, ... 9)
# выбирался нужный список (уровень - l1, l2,... l9)
# Level pick =================================================================

def drawWindow_0():
    win.blit(lvl_p_win, (0, 0))
    pygame.display.update()


run1 = True
while run1:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run1 = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        lev = l1
        break
    elif keys[pygame.K_2]:
        lev = l2
        break
    elif keys[pygame.K_3]:
        lev = l3
        break
    elif keys[pygame.K_4]:
        lev = 4
        break
    elif keys[pygame.K_5]:
        lev = l5
        break
    elif keys[pygame.K_6]:
        lev = l6
        break
    elif keys[pygame.K_7]:
        lev = l7
        break
    elif keys[pygame.K_8]:
        lev = l8
        break
    elif keys[pygame.K_9]:
        lev = l9
        break

    drawWindow_0()

# ============================================================================
# Координаты платформ:
x = 0
y = 0
# ============================================================================
# Отображение уровня. Нельзя засовывать в цикл (ломается)
# ============================================================================

for i, j in enumerate(lev):  # движение по столбцам
    for k, l in enumerate(j):  # движение по строке
        if l == '-':
            pl = Platform(x, y)  # переменная, отвечающая за расположение
            # в координатах каждой новой платформы
            sprite_group.add(pl)  # добавление в группу новой платформы
            platforms.append(
                pl)  # добавление в список платформ новой платформы
        x += 128  # переход к след. элементу строки, но теперь в координатах
    y += 72  # переход к след. столбцу, но теперь в координатах
    x = 0  # обнуление х, так как теперь просматривается следующая строка

# ============================================================================

timer = pygame.time.Clock()
if 1 == 1:  # здесь должен быть выбор уровня (Саня)
    run1 = True
    run2 = True
    while run1 or run2:
        pygame.time.delay(5)
        win.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False
                run2 = False
            if event.type == pygame.KEYDOWN:  # проверка, происходит ли
                #  НАжатие кнопки (в данный момент)
                if event.key == pygame.K_LEFT:
                    left1 = True
                if event.key == pygame.K_RIGHT:
                    right1 = True
                if event.key == pygame.K_UP:
                    up1 = True
                if event.key == pygame.K_a:
                    left2 = True
                if event.key == pygame.K_d:
                    right2 = True
                if event.key == pygame.K_w:
                    up2 = True
            elif event.type == pygame.KEYUP:  # проверка, произошло ли
                # ОТжатие кнопки (в данный момент)
                if event.key == pygame.K_LEFT:
                    left1 = False
                if event.key == pygame.K_RIGHT:
                    right1 = False
                if event.key == pygame.K_UP:
                    up1 = False
                if event.key == pygame.K_a:
                    left2 = False
                if event.key == pygame.K_d:
                    right2 = False
                if event.key == pygame.K_w:
                    up2 = False
        pl1.update(left1, right1, up1, platforms)  # метод обноления
        #                                           в классе Player
        pl2.update(left2, right2, up2, platforms)  # ^^^^^
        sprite_group.draw(win)  # отрисовка ВСЕХ элементов группы
        #                            (и платформ, и игроков)
        pygame.display.flip()
        timer.tick(60)

pygame.quit()
