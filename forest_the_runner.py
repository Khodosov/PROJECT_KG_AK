import pygame

pygame.init()

win = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Guk & Khodosov prod.")

bg = pygame.image.load('win.jpg')

# переменные-характеристики "персонажей"

logo = pygame.image.load('logo.jpg')

player2 = pygame.image.load('find1.png')
player1 = pygame.image.load('geo.png')

pl1win = pygame.image.load('1win.jpg')
pl2win = pygame.image.load('2win.jpg')

x1 = 5
y1 = 655
widht1 = 40
hight1 = 40
speed1 = 5
isJmp1 = False
jumpRange1 = 8
left1 = False
right1 = False

x2 = 5
y2 = 655
widht2 = 40
hight2 = 40
speed2 = 5
isJmp2 = False
jumpRange2 = 8
left2 = False
right2 = False

# тут должен быть лого

# нужно отрисовывать окно, например, 5 секунд

# while
#    pygame.mixer.music.load('opening.mp3')
#    pygame.mixer.music.play(0)
#    win.blit(logo, (0, 0))

pygame.mixer.music.load('Pskov.mp3')
pygame.mixer.music.play(-1)


# функция, которая рисует окно


def drawWindow():
    win.blit(bg, (0, 0))
    win.blit(player1, (x1, y1))
    win.blit(player2, (x2, y2))
    # win.fill((0, 0, 0)
    # pygame.draw.rect(win, (0, 0, 255), (x2, y2, widht2, hight2))
    # pygame.draw.rect(win, (0, 255, 0), (x1, y1, widht1, hight1))
    pygame.display.update()

keys = pygame.key.get_pressed()


# Сделать таймеры, в том числе для лого



if keys[pygame.K_1]:
    run1 = True
    run2 = True
    while run1 or run2:
        pygame.time.delay(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False
                run2 = False

        if keys[pygame.K_LEFT] and x1 > 5:
            x1 -= speed1
            left1 = True
            right1 = False

        elif keys[pygame.K_RIGHT] and x1 < 1280 - widht1 - 5:
            x1 += speed1
            left1 = False
            right1 = True

        if keys[pygame.K_a] and x2 > 5:
            x2 -= speed2
            left2 = True
            right2 = False

        if keys[pygame.K_d] and x2 < 1280 - widht2 - 5:
            x2 += speed2
            left2 = False
            right2 = True

        else:
            left1 = False
            right1 = False
            left2 = False
            right2 = False
        if not (isJmp1):

            if keys[pygame.K_UP]:
                isJmp1 = True

        else:
            if jumpRange1 >= -8:
                if jumpRange1 < 0:
                    y1 += (jumpRange1 ** 2) / 2
                else:
                    y1 -= (jumpRange1 ** 2) / 2
                jumpRange1 -= 1
            else:
                isJmp1 = False
                jumpRange1 = 8

        if not (isJmp2):

            if keys[pygame.K_w]:
                isJmp2 = True
        else:
            if jumpRange2 >= -8:
                if jumpRange2 < 0:
                    y2 += (jumpRange2 ** 2) / 2
                else:
                    y2 -= (jumpRange2 ** 2) / 2
                jumpRange2 -= 1
            else:
                isJmp2 = False
                jumpRange2 = 8
        #    if x1 == 1280 - widht1 - 0 or x2 == 1280 - widht1 - 0:
        #        break
        drawWindow()

# if x1 == 1280 - widht1 - 0:
#    win.blit(pl1win, (0, 0))
# if x1 == 1280 - widht1 - 0:
#    win.blit(pl2win, (0, 0))


pygame.quit()
