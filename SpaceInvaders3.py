import pygame
import random
import sys

pygame.init()
saat = pygame.time.Clock()

ekran_gen = 750
ekran_yuk = 600
ekran = pygame.display.set_mode((ekran_gen, ekran_yuk))
pygame.display.set_caption("Space Invaders")

pilot_yuzey = pygame.image.load("spaceresimler/space-invaders.png")
pilot_yuzey = pygame.transform.scale(pilot_yuzey, (75, 75))
pilot_dikdortgen = pilot_yuzey.get_rect(topleft=(337.5, 525))

uzayli_yuzey = pygame.image.load("spaceresimler/ufo (1).png")
uzayli_yuzey = pygame.transform.scale(uzayli_yuzey, (75, 75))

uzayli_yuzey2 = pygame.image.load("spaceresimler/ufo (4).png")
uzayli_yuzey2 = pygame.transform.scale(uzayli_yuzey2, (75, 75))

uzayli_yuzey3 = pygame.image.load("spaceresimler/ufo (3).png")
uzayli_yuzey3 = pygame.transform.scale(uzayli_yuzey3, (75, 75))

mermiyuzey = pygame.image.load("spaceresimler/bullet.png")
mermiyuzey = pygame.transform.scale(mermiyuzey, (20, 20))
mermi_dikdortgen = mermiyuzey.get_rect(topleft=(305, 800))

patlamayuzey = pygame.image.load("spaceresimler/explosion.png")
patlamayuzey = pygame.transform.scale(patlamayuzey, (40, 40))
patlama_dikdortgen = patlamayuzey.get_rect(topleft=(365, 800))

aralik = 20
uzayli_dikdortgen = []
uzayli2_dikdortgen = []
uzayli3_dikdortgen = []

# uzaylı mermi
uzaylımermi_dikdortgen = []
uzaylımermiyuzey = pygame.image.load("spaceresimler/bomb.png")
uzaylımermiyuzey = pygame.transform.scale(uzaylımermiyuzey, (30, 30))




for i in range(6):
    uzayli_dikdortgen.append(uzayli_yuzey.get_rect(topleft=(aralik, 50)))
    aralik += 120
aralik = 20
for i in range(6):
    uzayli2_dikdortgen.append(uzayli_yuzey2.get_rect(topleft=(aralik, 150)))
    aralik += 120
aralik = 20
for i in range(6):
    uzayli3_dikdortgen.append(uzayli_yuzey3.get_rect(topleft=(aralik, 250)))
    aralik += 120
pilotxhiz, pilotyhiz = 0, 0
uzaylıxhiz = 0
uzaylıxhiz2 = 0
uzaylıxhiz3 = 0
mermiyhiz = 0

uzaylimermihiz1 = 3
uzaylimermihiz2 = 3
uzaylimermihiz3 = 3
uzaylıyaratikkonumları = []
can = 3


# Loop Aşaması Çizdirme



while True:

    if can <= 0:
        can = 0

        pilotxhiz, pilotyhiz = 0, 0
        uzaylıxhiz = 0
        uzaylıxhiz2 = 0
        uzaylıxhiz3 = 0
        mermiyhiz = 0

        uzaylimermihiz1 = 0
        uzaylimermihiz2 = 0
        uzaylimermihiz3 = 0

    # kullanıcı girişini kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pilotyhiz += -5

            elif event.key == pygame.K_DOWN:
                pilotyhiz += 5

            elif event.key == pygame.K_LEFT:
                pilotxhiz += -5


            elif event.key == pygame.K_RIGHT:
                pilotxhiz += 5
            elif event.key == pygame.K_SPACE:
                mermiyhiz = 0
                mermi_dikdortgen.x = pilot_dikdortgen.x + 27.5
                mermi_dikdortgen.y = pilot_dikdortgen.y + 10
                mermiyhiz += -5




        elif event.type == pygame.KEYUP:
            pilotxhiz = 0
            pilotyhiz = 0

    pilot_dikdortgen.x += pilotxhiz
    pilot_dikdortgen.y += pilotyhiz
    mermi_dikdortgen.y += mermiyhiz

    if uzayli_dikdortgen[0].x <= 20:
        uzaylıxhiz += 0.1
    elif uzayli_dikdortgen[0].x > 50:
        uzaylıxhiz += -0.1
    if uzayli2_dikdortgen[0].x <= 25:
        uzaylıxhiz2 += 0.1
    elif uzayli2_dikdortgen[0].x > 60:
        uzaylıxhiz2 += -0.1
    if uzayli3_dikdortgen[0].x <= 30:
        uzaylıxhiz3 += 0.1
    elif uzayli3_dikdortgen[0].x > 50:
        uzaylıxhiz3 += -0.1

    for i in range(5):
        uzayli_dikdortgen[i].x += uzaylıxhiz
        if mermi_dikdortgen.colliderect(uzayli_dikdortgen[i]):
            patlama_dikdortgen.x = uzayli_dikdortgen[i].x + 20
            patlama_dikdortgen.y = uzayli_dikdortgen[i].y + 10
            mermi_dikdortgen.y = -200
            uzayli_dikdortgen[i].y = -600

    for i in range(5):
        uzayli2_dikdortgen[i].x += uzaylıxhiz2
        if mermi_dikdortgen.colliderect(uzayli2_dikdortgen[i]):
            patlama_dikdortgen.x = uzayli2_dikdortgen[i].x + 20
            patlama_dikdortgen.y = uzayli2_dikdortgen[i].y + 10
            mermi_dikdortgen.y = -200
            uzayli2_dikdortgen[i].y = -600
    for i in range(5):
        uzayli3_dikdortgen[i].x += uzaylıxhiz3
        if mermi_dikdortgen.colliderect(uzayli3_dikdortgen[i]):
            patlama_dikdortgen.x = uzayli3_dikdortgen[i].x + 20
            patlama_dikdortgen.y = uzayli3_dikdortgen[i].y + 10
            mermi_dikdortgen.y = -200
            uzayli3_dikdortgen[i].y = -600

    x0 = uzayli_dikdortgen[0].x
    y0 = uzayli_dikdortgen[0].y
    x1 = uzayli_dikdortgen[1].x
    y1 = uzayli_dikdortgen[1].y
    x2 = uzayli_dikdortgen[2].x
    y2 = uzayli_dikdortgen[2].y
    x3 = uzayli_dikdortgen[3].x
    y3 = uzayli_dikdortgen[3].y
    x4 = uzayli_dikdortgen[4].x
    y4 = uzayli_dikdortgen[4].y
    x5 = uzayli_dikdortgen[5].x
    y5 = uzayli_dikdortgen[5].y
    x6 = uzayli2_dikdortgen[0].x
    y6 = uzayli2_dikdortgen[0].y
    x7 = uzayli2_dikdortgen[1].x
    y7 = uzayli2_dikdortgen[1].y
    x8 = uzayli2_dikdortgen[2].x
    y8 = uzayli2_dikdortgen[2].y
    x9 = uzayli2_dikdortgen[3].x
    y9 = uzayli2_dikdortgen[3].y
    x10 = uzayli2_dikdortgen[4].x
    y10 = uzayli2_dikdortgen[4].y
    x11 = uzayli2_dikdortgen[5].x
    y11 = uzayli2_dikdortgen[5].y
    x12 = uzayli3_dikdortgen[0].x
    y12 = uzayli3_dikdortgen[0].y
    x13 = uzayli3_dikdortgen[1].x
    y13 = uzayli3_dikdortgen[1].y
    x14 = uzayli3_dikdortgen[2].x
    y14 = uzayli3_dikdortgen[2].y
    x15 = uzayli3_dikdortgen[3].x
    y15 = uzayli3_dikdortgen[3].y
    x16 = uzayli3_dikdortgen[4].x
    y16 = uzayli3_dikdortgen[4].y
    x17 = uzayli3_dikdortgen[5].x
    y17 = uzayli3_dikdortgen[5].y

    if len(uzaylımermi_dikdortgen) < 4:
        for i in range(4-len(uzaylımermi_dikdortgen)):
            sayi = random.randint(0, 17)
            if sayi == 0 and y0 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x0, y0)))
            if sayi == 1 and y1 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x1, y1)))
            if sayi == 2 and y2 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x2, y2)))
            if sayi == 3 and y3 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x3, y3)))
            if sayi == 4 and y4 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x4, y4)))
            if sayi == 5 and y5 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x5, y5)))
            if sayi == 6 and y6 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x6, y6)))
            if sayi == 7 and y7 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x7, y7)))
            if sayi == 8 and y8 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x8, y8)))
            if sayi == 9 and y9 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x9, y9)))
            if sayi == 10 and y10 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x10, y10)))
            if sayi == 11 and y11 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x11, y11)))
            if sayi == 12 and y12 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x12, y12)))
            if sayi == 13 and y13 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x13, y13)))
            if sayi == 14 and y14 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x14, y14)))
            if sayi == 15 and y15 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x15, y15)))
            if sayi == 16 and y16 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x16, y16)))
            if sayi == 17 and y17 > 0:
                uzaylımermi_dikdortgen.append(uzaylımermiyuzey.get_rect(topleft=(x17, y17)))
            if y0 < 0 and y1 < 0 and y2 < 0 and y3 < 0 and y4 < 0 and y5 < 0 and y6 < 0 and y7 < 0 and y8 < 0 and y9 < 0 and y10 < 0 and y11 < 0 and y12 < 0 and y13 < 0 and y14 < 0 and y15 < 0 and y16 < 0 and y17 < 0:
                can = 0

    uzaylımermi_dikdortgen[0].y += uzaylimermihiz1
    if uzaylımermi_dikdortgen[0].y > 620:
        uzaylımermi_dikdortgen.pop(0)
    uzaylımermi_dikdortgen[1].y += uzaylimermihiz2
    if uzaylımermi_dikdortgen[1].y > 620:
        uzaylımermi_dikdortgen.pop(1)

    for i in range(3):
        if pilot_dikdortgen.colliderect(uzaylımermi_dikdortgen[i]):
            uzaylımermi_dikdortgen.pop(i)
            patlama_dikdortgen.x = pilot_dikdortgen.x + 20
            patlama_dikdortgen.y = pilot_dikdortgen.y + 10
            can = can - 1

    # çizdirme  KOD EKSikmiş, uğurun attığının içinden silinmiş, aynısı değildi, kesiyorum bağlantıyı

    ekran.fill("black")

    for uzaylimermi in uzaylımermi_dikdortgen:
        ekran.blit(uzaylımermiyuzey, uzaylimermi)

    ekran.blit(pilot_yuzey, pilot_dikdortgen)
    ekran.blit(patlamayuzey, patlama_dikdortgen)
    ekran.blit(mermiyuzey, mermi_dikdortgen)

    for uzayli in uzayli_dikdortgen:
        ekran.blit(uzayli_yuzey, uzayli)
    for uzayli in uzayli2_dikdortgen:
        ekran.blit(uzayli_yuzey2, uzayli)
    for uzayli in uzayli3_dikdortgen:
        ekran.blit(uzayli_yuzey3, uzayli)

    font = pygame.font.SysFont(None, 24)  # skor ekranı için
    mesaj = "Can : " + str()
    img = font.render(mesaj, True, "white")
    ekran.blit(img, (20, 20))

    if can <= 0:
        can = 0
        font = pygame.font.SysFont(None, 100)  # skor ekranı için
        mesaj = "Game Over"
        img = font.render(mesaj, True, "white")
        ekran.blit(img, (150, 200))

    pygame.display.flip()
    saat.tick(60)
