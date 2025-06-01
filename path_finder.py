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
    time.sleep(3)

def draw_grid():
    for col in range(columns):
        for row in range(rows):
            grid = pygame.Rect(row*cell_size, col*cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, grey, grid, 1)

def draw_state():
    global gen_num
    #print(f"state[5] should be 1. It is {state[5]}")
    #print(f"The state is: {state}")
    #print(f"Length of state: {len(state)}")
    for i in range(len(state)):
        #print(f"is 1?:{state[i]} --> {state[i] == 1}")
        if state[i] == 1:
            #print(f"i: {i}")
            # This will be drawing the colors for the current generation
            generation = pygame.Rect(i*cell_size,gen_num*cell_size,cell_size,cell_size)

            pygame.draw.rect(screen, black, generation, 0)

def update_state():
    global state
    # This will be updating creating the new generation based on the rule of the last generation
    # As noted at top, initially this will just be for rule 1, but will eventually modify to make rules selectable
    new_state = [0]*len(state)

    # Always flip the endpoints
    new_state[0] = (state[0]+1) % 2
    new_state[len(state)-1] = (state[len(state)-1]+1) % 2

    for i in range(1,len(state)-1):
        # Only way for a bit to flip in RULE 1 is if they are all 0
        if(state[i-1] + state[i] + state[i+1] == 0):
            new_state[i] = 1

    #print(f"State: {state}")
    #print(f"Newstate: {new_state}")
    state = new_state

main()
