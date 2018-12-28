import pygame as pg

# --- constants --- (UPPER_CASE names)

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# --- functions --- (lower_case names)

def message(text, delay=5000, foreground=WHITE, background=BLACK):

    image = font.render(text, True, foreground)
    rect = image.get_rect()
    rect.center = screen.get_rect().center

    screen.fill(background)
    screen.blit(image, rect)
    pg.display.flip()

    current_time = pg.time.get_ticks()
    exit_time = current_time + delay

    clock = pg.time.Clock()
    running = True

    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        current_time = pg.time.get_ticks()

        if current_time >= exit_time:
            running = False

        clock.tick(5)

# --- main --- (lower_case names)

pg.init()

screen = pg.display.set_mode((800, 600))
screen_rect = screen.get_rect()

font = pg.font.Font(None, 40)

message("Wait 2 seconds or press ESC", 2000, BLACK, RED)
message("You Died!", 2000)
message("Good Bye!", 2000, BLACK, GREEN)

pg.quit()
quit()
