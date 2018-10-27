import pygame

pygame.init()
win = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Guk & Khodosov prod.")


x=50
y=50
widht=40
hight=60
speed=10

run=True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=speed
    if keys[pygame.K_RIGHT]:
        x+=speed
    if keys[pygame.K_UP]:
        y-=speed
    if keys[pygame.K_DOWN]:
        y+=speed

    pygame.draw.rect(win,(0,255, 0), (x, y, widht, hight))
    pygame.display.update()

pygame.quit()