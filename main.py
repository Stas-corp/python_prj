import pygame as pg
import player
import blocks
pg.init()

DISPLAY = WIN_WIDTH, WIN_HEIGHT = 800, 800
BG_COLOR = (123, 45, 222)

def main():
    screen = pg.display.set_mode(DISPLAY)
    pg.display.set_caption('SUPER MARIVO')
    bg = pg.Surface(DISPLAY)
    bg.fill(BG_COLOR)
    clock = pg.time.Clock()

    Level = [
        '-------------------------',
        '-                       -',
        '- -----                 -',
        '-                       -',
        '-                       -',
        '-       -               -',
        '-                       -',
        '-                       -',
        '-           -----       -',
        '-                       -',
        '-                       -',
        '-                   -   -',
        '-    -                  -',
        '-                       -',
        '-                       -',
        '-        ---            -',
        '-                       -',
        '-                       -',
        '-           --          -',
        '-                       -',
        '-                       -',
        '-       ---             -',
        '-                       -',
        '-                       -',
        '-------------------------']

    hero = player.Player(50,50)
    entities = pg.sprite.Group()
    platforms = []
    entities.add(hero)

    left = right = up = False
    Game = True

    while Game:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                Game = False

            if e.type == pg.KEYDOWN:
                if e.key == pg.K_d:
                    right = True
                if e.key == pg.K_a:
                    left = True
                if e.key == pg.K_w:
                    up = True
            
            if e.type == pg.KEYUP:
                if e.key == pg.K_d:
                    right = False
                if e.key == pg.K_a:
                    left = False
                if e.key == pg.K_w:
                    up = False

        screen.blit(bg, (0,0))
        hero.update(screen, left, right, up)
        entities.draw(screen)

        x=y=0
        for row in Level:
            for symbol in row:
                if symbol == '-':
                    pf = blocks.Platform(x,y)
                    entities.add(pf)
                    platforms.append(pf)
                x += blocks.BL_WIDTH
            y += blocks.BL_HEIGHT
            x = 0
        pg.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()