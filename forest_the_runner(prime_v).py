# ============================================================================
# ============================================================================
# ================================ AK_KG =====================================
# ========================== FOREST THE RUNNER ===============================
# ============================================================================
# ============================================================================
# ============================================================================
import pygame
from levels import l1, l2, l3, l4, l5, l6, l7, l8, l9, l0, Platform, \
    Prize  # li (1<=i<=9)
#  - это список платформ - уровень, из файла levels.py.
#  Platform - класс платформ
from players import Player  # Player - класс игроков

pygame.init()
win = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Guk & Khodosov prod.")
# ============================================================================
endgame = pygame.image.load('endgame.jpg')  # да это отсылка
prize = ('prize.png')
pari = pygame.image.load('pari.jpg')
plat = ('pl.png')
bg = pygame.image.load('win.jpg')
logo = pygame.image.load('new_logo.jpg')
lvl_p_win = pygame.image.load('histranger.jpg')
lvl_p_win1 = pygame.image.load('lvl_p.jpg')
tutor = pygame.image.load('tutor.jpg')
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
# Tutor ======================================================================
while skip < 250:  # 450
    win.blit(tutor, (0, 0))
    pygame.display.update()
    skip += 1
skip = 0
game_exe = True

# ============================================================================
sprite_group = pygame.sprite.Group()  # переменная (группа), в которой
# содержатся все элементы класса Sprite (и игроки, и платформы)
# ============================================================================
# Добавление в группу каждого игрока:
sprite_group.add(pl1)
sprite_group.add(pl2)
platforms = []  # Список всех платформ в конкретном уровне
prizes = []  # Список всех призов (финишей)


# Level pick =================================================================
while game_exe:
    def drawWindow_0():
        win.blit(lvl_p_win1, (0, 0))
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
            lev = l4
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
        elif keys[pygame.K_0]:
            lev = l0
            break

        drawWindow_0()

    # ============================================================================
    # Координаты платформ:
    x = 0
    y = 0


    # easter agg =================================================================
    def sanya_wins():
        win.blit(pari, (0, 0))
        pygame.display.update()


    # ============================================================================
    # Отображение уровня. Нельзя засовывать в цикл (ломается)
    # ============================================================================

    for i, j in enumerate(lev):  # движение по столбцам
        for k, l in enumerate(j):  # движение по строке
            if l == '-':
                pl = Platform(x, y,
                              plat)  # переменная, отвечающая за расположение
                # в координатах каждой новой платформы
                sprite_group.add(pl)  # добавление в группу новой платформы
                platforms.append(
                    pl)  # добавление в список платформ новой платформы
            if l == '.':
                pr = Prize(x, y, prize)
                sprite_group.add(pr)
                prizes.append(
                    pr)
            x += 128  # переход к след. элементу строки, но теперь в координатах
        y += 72  # переход к след. столбцу, но теперь в координатах
        x = 0  # обнуление х, так как теперь просматривается следующая строка

    # ============================================================================

    timer = pygame.time.Clock()
    if 1 == 1:
        run1 = True
        run2 = True
        while run1 or run2:
            pygame.time.delay(5)
            win.blit(bg, (0, 0))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_m]:
                while skip < 250:  # 450
                    win.blit(pari, (0, 0))
                    pygame.display.update()
                    skip += 1
                    pl1.isFinish = True
            if pl1.isFinish is True:
                break
            if pl2.isFinish is True:
                break

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
            pl1.update(left1, right1, up1, platforms,
                       prizes)  # метод обноления
            #                                           в классе Player
            pl2.update(left2, right2, up2, platforms, prizes)  # ^^^^^
            sprite_group.draw(win)  # отрисовка ВСЕХ элементов группы
            #                            (и платформ, и игроков)
            pygame.display.flip()
            timer.tick(60)
    if pl1.isFinish is True:
        while skip < 250:
            win.blit(pl2win, (0, 0))
            pygame.display.update()
            skip += 1
        skip = 0
        game_exe = False
    if pl2.isFinish is True:
        while skip < 250:
            win.blit(pl1win, (0, 0))
            pygame.display.update()
            skip += 1
        skip = 0
        game_exe = False


def drawWindow():
    win.blit(endgame, (0, 0))
    pygame.display.update()


run1 = True
while run1:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run1 = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    elif keys[pygame.K_y]:
        game_exe = True
        break
    game_exe = True
    drawWindow()
game_exe = True
pygame.quit()
