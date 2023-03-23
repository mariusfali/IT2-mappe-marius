# Example file showing a basic pygame "game loop"
import pygame as pg
from hinder import Hinder
from spiller import Spiller
from random import randint

# pygame setup
pg.init()
#screen = pygame.display.set_mode((1280, 720))
bredde = 500
hoyde = 500
screen = pg.display.set_mode((bredde, hoyde))
clock = pg.time.Clock()
running = True
frame = 0
previous_frame = 0
hindre = []
points = 0
lives = 3

spiller = Spiller(200, 450, 0.1, 100, 30)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    mousepos = pg.mouse.get_pos()
    if lives > 0:

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        font = pg.font.SysFont('Corbel', 23, True) 
        poeng_tekst = font.render(f"Score: {points}", True, (255, 255, 255))
        screen.blit(poeng_tekst, (20, 20))

        lives_tekst = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(lives_tekst, (400, 20))

        
        frame += 0.01

        if previous_frame + 1 == int(frame):
            previous_frame = previous_frame + 1
            nytt_hinder = Hinder(randint(20,445), 25, 1, 35, 35)
            hindre.append(nytt_hinder)
            #print("check")

        #print(frame)
        for i in hindre:
            pg.draw.rect(screen, "green", (i.x, i.y, i.bredde, i.hoyde))
            i.y += i.fart 
            if i.y + i.bredde == spiller.y and ((i.x >= spiller.x and i.x <= spiller.x + spiller.bredde) or (i.x + i.bredde >= spiller.x and i.x + i.bredde <= spiller.x + spiller.bredde)):
                hindre.remove(i)
                points += 1
            if i.y >= bredde + i.hoyde:
                hindre.remove(i)
                lives -= 1



        #pg.draw.circle(screen, "red", (spiller.x, spiller.y), 40)
        pg.draw.rect(screen, "red", (spiller.x,spiller.y,spiller.bredde,spiller.hoyde))

        keys = pg.key.get_pressed()
        #if keys[pg.K_UP]:
        #    spiller.y -= 10
        #if keys[pg.K_DOWN]:
        #    spiller.y += 10
        if keys[pg.K_LEFT]:
            if spiller.x <= 10:
                pass
            else:
                spiller.x -= 10 
        if keys[pg.K_RIGHT]:
            if spiller.x >= 390:
                pass
            else:
                spiller.x += 10 
    else:
        screen.fill("purple")
        font = pg.font.SysFont('Corbel', 23, True) 
        death_tekst = font.render(f"Game Over", True, (255, 255, 255))
        screen.blit(death_tekst, (200, 230))
        play_tekst = font.render(f"Try again", True, (255, 255, 255))
        screen.blit(play_tekst, (200, 400))

        for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if 200 <= mousepos[0] <= 300 and 400 <= mousepos[1] <= 450:
                        lives = 3
                        print("du trykket")


    # LAG SPILLET DIT HER:

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()