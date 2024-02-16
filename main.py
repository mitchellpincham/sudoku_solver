import pygame
import time
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
font = pygame.font.Font(pygame.font.get_default_font(), 36)

# constants
GRID_SIZE = 50
BORDER_SIZE = 20

# grid and information about the grid, could use oop but why.
grid = [[0 for _ in range(9)] for _ in range(9)]
locked = [[False for _ in range(9)] for _ in range(9)]
possible_lists = [[None for _ in range(9)] for _ in range(9)]

# the cell that is selected by the user
selected = [0, 0]

# an example sudoku
def load_example():
    return [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]


def lock_grid(g):
    """
        returns a 2d array with a true where there is a number, and false where there is none
    """
    l = [[False for i in range(9)] for _ in range(9)]
    for y in range(9):
        for x in range(9):
            if g[y][x] != 0:
                l[y][x] = True

    return l

def check_grid(g):
    """
        this returns false if there are any errors in the sudoku grid
        eg. the same number is repeated in a row
    """
    # check rows
    for row in range(9):
        for num in g[row]:
            # if a number is repeated
            if g[row].count(num) > 1:
                if num != 0:
                    return False

    # check cols
    for col in range(9):
        arr = []
        for row in range(9):
            arr.append(g[row][col])

        for num in arr:
            if arr.count(num) > 1:
                if num != 0:
                    return False

    # check boxes
    for box in range(9):
        # get the coordinates in the top left cell of block
        x = (box % 3) * 3
        y = int(box / 3) * 3

        # add each cell of box to an array
        arr = []
        for x_ in range(3):
            for y_ in range(3):
                arr.append(g[y + y_][x + x_])

        for num in arr:
            if arr.count(num) > 1:
                if num != 0:
                    return False
    return True


def possible_moves(g, x, y):
    """
        returns an array of possible numbers that could go in a cordinate (x, y) in the grid g.
    """
    a = [] 
    for i in range(1, 10):
        # check each number and use the check grid function to see if it works
        g[y][x] = i
        if check_grid(g):
            a.append(i)

    return a


def next_cell():
    """
        moves the selected square to the right, or to the next row
    """
    # try to move right
    if selected[1] != 8:
        selected[1] += 1
        return
    # otherwise next row
    if selected[0] != 8:
        selected[0] += 1
        selected[1] = 0


def last_cell():
    """
        moves the selected square to the left, or to the last row
    """
    # try to move right
    if selected[1] != 0:
        selected[1] -= 1
        return
    # otherwise next row
    if selected[0] != 0:
        selected[0] -= 1
        selected[1] = 8


def draw_grid():
    """
        This function does all of the drawing to the screen, in the order
            - fill the screen with grey
            - draw rectangle on selected square
            - draw the lines to make out the boxes
            - draw the numbers
    """
    screen.fill((120, 120, 120))

    # draw selected square
    x = selected[1] * GRID_SIZE + BORDER_SIZE
    y = selected[0] * GRID_SIZE + BORDER_SIZE
    pygame.draw.rect(screen, (255, 255, 120), (x, y, GRID_SIZE, GRID_SIZE))
    
    c = (0, 0, 0)
    p = [GRID_SIZE * n * 3 + BORDER_SIZE for n in range(4)]  # p = [GRID_SIZE * 0 + BORDER_SIZE, GRID_SIZE * 3 + BORDER_SIZE, GRID_SIZE * 6 + BORDER_SIZE, GRID_SIZE * 9 + BORDER_SIZE]
    
    # horizontal lines
    for i in range(4):
        pygame.draw.line(screen, c, (p[0], p[i]), (p[3], p[i]), 5)
    # vertical lines
    for i in range(4):
        pygame.draw.line(screen, c, (p[i], p[0]), (p[i], p[3]), 5)

    # if its wrong, then draw the numbers red
    if check_grid(grid):
        c = (0, 0, 0)
    else:
        c = (255, 0, 0)

    # now draw all the numbers
    for y in range(9):
        for x in range(9):
            # if there is a number in the cell
            if grid[y][x] != 0:
                # if it is a locked then make the number blue and load the surface
                if locked[y][x]:
                    text_surface = font.render(str(grid[y][x]), True, (0, 0, 255))
                else:
                    text_surface = font.render(str(grid[y][x]), True, c)
                # draw the number, making sure to centre it and draw it in the middle of the square
                x_ = (x + 0.5) * GRID_SIZE + BORDER_SIZE - text_surface.get_rect().width / 2
                y_ = (y + 0.5) * GRID_SIZE + BORDER_SIZE - text_surface.get_rect().height / 2
                
                screen.blit(text_surface, (x_, y_))

    # end of the function, now render
    pygame.display.flip()



# keeps state of the game
running = True
solving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x = int((pos[0] - BORDER_SIZE) / GRID_SIZE)
            y = int((pos[1] - BORDER_SIZE) / GRID_SIZE)
            if 0 <= x <= 9 and 0 <= y <= 9:
                selected = [y, x]

        elif event.type == pygame.KEYDOWN:
            if not solving:
                if not locked[selected[0]][selected[1]]:
                    if event.key == pygame.K_1:
                        grid[selected[0]][selected[1]] = 1
                        next_cell()
                    elif event.key == pygame.K_2:
                        grid[selected[0]][selected[1]] = 2
                        next_cell()
                    elif event.key == pygame.K_3:
                        grid[selected[0]][selected[1]] = 3
                        next_cell()
                    elif event.key == pygame.K_4:
                        grid[selected[0]][selected[1]] = 4
                        next_cell()
                    elif event.key == pygame.K_5:
                        grid[selected[0]][selected[1]] = 5
                        next_cell()
                    elif event.key == pygame.K_6:
                        grid[selected[0]][selected[1]] = 6
                        next_cell()
                    elif event.key == pygame.K_7:
                        grid[selected[0]][selected[1]] = 7
                        next_cell()
                    elif event.key == pygame.K_8:
                        grid[selected[0]][selected[1]] = 8
                        next_cell()
                    elif event.key == pygame.K_9:
                        grid[selected[0]][selected[1]] = 9
                        next_cell()
                    elif event.key in [pygame.K_0, pygame.K_BACKSPACE]:
                        grid[selected[0]][selected[1]] = 0
                        next_cell()
                    
                if event.key in [pygame.K_w, pygame.K_UP]:
                    if selected[0] != 0:
                        selected[0] -= 1
                elif event.key in [pygame.K_a, pygame.K_LEFT]:
                    last_cell()
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    if selected[0] != 8:
                        selected[0] += 1
                elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                    next_cell()

                elif event.key == pygame.K_l:
                    grid = load_example()
                    locked = lock_grid(grid)
                elif event.key == pygame.K_c:
                    print(check_grid(grid))
                elif event.key in [pygame.K_q, pygame.K_RETURN]:
                    locked = lock_grid(grid)
                    selected = [0, 0]
                    solving = True
    
    # if it is solving then make one move per frame
    if solving:
        # move the selected cell forwards until it reaches an empty cell
        while locked[selected[0]][selected[1]]:
            next_cell()
            # if its the last cell
            if selected == [8, 8]:
                print("done")
                solving = False
                break

        l = possible_lists[selected[0]][selected[1]]
        if l == None:
            l = possible_moves(grid, selected[1], selected[0])

        if len(l) != 0:
            choice = random.choice(l)
            l.remove(choice)
            possible_lists[selected[0]][selected[1]] = l
            
            #time.sleep(0.1)
            grid[selected[0]][selected[1]] = choice
            
            if selected == [8, 8]:
                print("done")
                solving = False
                
            next_cell()
        else:
            grid[selected[0]][selected[1]] = 0
            possible_lists[selected[0]][selected[1]] = None
            last_cell()
            while locked[selected[0]][selected[1]]:
                last_cell()

    
            
    draw_grid()
    

pygame.quit()
