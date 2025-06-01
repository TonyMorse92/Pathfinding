# First pass. Just doing 1D rule 1 to start off (should just alternate each generation)
# Just going to start off with 10x10 board with cell a_15 initialized black

import pygame
import sys
import time #DEBUGGING


start_pos = [0,0]
target_pos = [8,0]


black = (0,0,0)
white = (255,255,255)
grey = (128,128,128)
red = (255,0,0)
rows = 400
columns = 400
cell_size = 40
state = [0,0,0,0,0,1,0,0,0,0] # 1 black
gen_num = 0

def main():
    global screen, clock, gen_num, state
    pygame.init()
    screen = pygame.display.set_mode((rows,columns))
    clock = pygame.time.Clock()
    screen.fill(white)

    draw_grid()

    pygame.display.update()
    time.sleep(1)
    start_cell = pygame.Rect(start_pos[0]*cell_size, start_pos[1]*cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, black, start_cell)
    target_cell = pygame.Rect(target_pos[0]*cell_size, target_pos[1]*cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, grey, target_cell)
    pygame.display.update()

    time.sleep(2)


    target_hit = False

    num_moves = 0
    while not target_hit:
        num_moves += 1
        pygame.draw.rect(screen, red, start_cell)
        start_cell = pygame.Rect(num_moves*cell_size, start_pos[1]*cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, black, start_cell)
        pygame.display.update()
        time.sleep(1)
        if num_moves == 8:
            target_hit = True


def draw_grid():
    for col in range(columns):
        for row in range(rows):
            grid = pygame.Rect(row*cell_size, col*cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, grey, grid, 1)

main()
