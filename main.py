import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN, K_q
import constants
from tetris import Tetris
from grid import Grid
import time


# setup pygame window
WIN = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")


# main game function
def main():
    # font setup
    pygame.font.init()
    myfont = pygame.font.SysFont("Comic Sans MS",30)

    # setup game grid, blocks and game clock
    grid = Grid(WIN)
    tetris = Tetris(WIN,grid)
    clock = pygame.time.Clock()

    # fill the game area white, and the rest of the screen gray
    WIN.fill(constants.GRAY)
    WIN.fill(constants.WHITE,(constants.LEFT,constants.TOP,constants.GAME_WIDTH,constants.GAME_HEIGHT))

    # draw text for score, level, number of lines and high score
    score_surface = myfont.render("Score : 0",False,(constants.WHITE))
    WIN.blit(score_surface,(500,100))

    level_surface = myfont.render("Level : 0",False,(constants.WHITE))
    WIN.blit(level_surface,(500,200))

    lines_surface = myfont.render("Lines : 0",False,(constants.WHITE))
    WIN.blit(lines_surface,(500,300))

    hs = grid.game.high_score
    hs_surface = myfont.render(f"High Score : {hs}",False,(constants.WHITE))
    WIN.blit(hs_surface,(500,400))

    # main game loop
    while True:
        time.sleep(constants.DELAY)
        clock.tick(constants.FPS)
        pygame.display.update()
        # event checking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if tetris.can_rotate():
                        tetris.rotate()
                elif event.key == K_LEFT:
                    if tetris.can_move_left():
                        tetris.move_left()
                elif event.key == K_RIGHT:
                    if tetris.can_move_right():
                        tetris.move_right()
                elif event.key == K_DOWN:
                    if tetris.can_move_down():
                        tetris.move_down()
                elif event.key == K_q:
                    grid.game.update_leaderboard()
                    main_menu()


        # move down once on each loop, if we cannot move down we create a new Tetris shape at the top of the screen
        if tetris.can_move_down():
            tetris.move_down()
        else:
            tetris = Tetris(WIN,grid)

        # check for filled lines
        grid.check_lines()

        # check if game_over
        if grid.check_game_over():
            main_menu()


def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WIN.fill(constants.GRAY)
        title_label = title_font.render("To begin click the mouse or hit SPACE ", 1, (255,255,255))
        WIN.blit(title_label, (constants.SCREEN_WIDTH/2 - title_label.get_width()/2, 350) )
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    main()

    pygame.quit()


main_menu()

    