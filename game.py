import pygame

pygame.init()
win = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Guk & Khodosov prod.")

x = 5
y = 655
widht = 19
hight = 29
speed = 5
isJmp = False
jumpRange = 10

lest = False
right = False
animcount = 0

walkRight = [pygame.image.load('runner1.png'),
             pygame.image.load('runner2.png'),
             pygame.image.load('runner3.png'),
             pygame.image.load('runner4.png'),
             pygame.image.load('runner5.png'),
             pygame.image.load('runner6.png'),
             pygame.image.load('runner7.png'),
             pygame.image.load('runner8.png')]

# walkLeft=[pygame.image.load(''),pygame.image.load(''),pygame.image.load(''),
#         pygame.image.load(''),pygame.image.load(''),pygame.image.load('')]

playerstand = pygame.image.load('runner.png')


def drawWindow():
    # win.blit()
    global animcount

    if animcount + 1 >= 35:
        animcount = 0
    #    if left:
    #       win.blit(walkleft[animcount//5])
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 255, 0), (x, y, widht, hight))
    pygame.display.update()


run = True
while run:
    pygame.time.delay(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 1280 - widht - 5:
        x += speed
        left = False
        right = True

    else:
        left = False
        right = False
        animcount = 0

    if not (isJmp):

        if keys[pygame.K_SPACE]:
            isJmp = True
    else:
        if jumpRange >= -10:
            if jumpRange < 0:
                y += (jumpRange ** 2) / 2
            else:
                y -= (jumpRange ** 2) / 2
            jumpRange -= 1
        else:
            isJmp = False
            jumpRange = 10

    drawWindow()

pygame.quit()
