import pygame
import time
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
font = pygame.font.Font(pygame.font.get_default_font(), 36)

GRID_SIZE = 50
BORDER_SIZE = 20

grid = [[0 for _ in range(9)] for _ in range(9)]
locked = [[False for _ in range(9)] for _ in range(9)]
possible_lists = [[None for _ in range(9)] for _ in range(9)]

selected = [0, 0]

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
    l = [[False for i in range(9)] for _ in range(9)]
    for y in range(9):
        for x in range(9):
            if g[y][x] != 0:
                l[y][x] = True

    return l

def check_grid(g):
    # check rows
    for i in range(9):
        for n in g[i]:
            if g[i].count(n)>1:
                if n != 0:
                    return False

    # check cols
    for i in range(9):
        a = []
        for j in range(9):
            a.append(g[j][i])

        for n in a:
            if a.count(n)>1:
                if n != 0:
                    return False

    # check boxes
    for i in range(9):
        x = (i % 3) * 3
        y = int(i / 3) * 3
        a = []
        for x_ in range(3):
            for y_ in range(3):
                #print([y + y_, x + x_])
                a.append(g[y + y_][x + x_])

        for n in a:
            if a.count(n)>1:
                if n != 0:
                    return False
    return True


def possible_moves(g, x, y):
    a = []

    for i in range(1, 10):
        g[y][x] = i
        if check_grid(g):
            a.append(i)

    return a


def next_cell():
    # try to move right
    if selected[1] != 8:
        selected[1] += 1
        return
    # otherwise next row
    if selected[0] != 8:
        selected[0] += 1
        selected[1] = 0


def last_cell():
    # try to move right
    if selected[1] != 0:
        selected[1] -= 1
        return
    # otherwise next row
    if selected[0] != 0:
        selected[0] -= 1
        selected[1] = 8


def draw_grid():
    screen.fill((120, 120, 120))

    x = selected[1] * GRID_SIZE + BORDER_SIZE
    y = selected[0] * GRID_SIZE + BORDER_SIZE
    
    pygame.draw.rect(screen, (255, 255, 120), (x, y, GRID_SIZE, GRID_SIZE))
    c = (0, 0, 0)
    p0 = GRID_SIZE * 0 + BORDER_SIZE
    p1 = GRID_SIZE * 3 + BORDER_SIZE
    p2 = GRID_SIZE * 6 + BORDER_SIZE
    p3 = GRID_SIZE * 9 + BORDER_SIZE
    # horizontal lines
    pygame.draw.line(screen, c, (p0, p0), (p3, p0), 5)
    pygame.draw.line(screen, c, (p0, p1), (p3, p1), 5)
    pygame.draw.line(screen, c, (p0, p2), (p3, p2), 5)
    pygame.draw.line(screen, c, (p0, p3), (p3, p3), 5)
    # vertical lines
    pygame.draw.line(screen, c, (p0, p0), (p0, p3), 5)
    pygame.draw.line(screen, c, (p1, p0), (p1, p3), 5)
    pygame.draw.line(screen, c, (p2, p0), (p2, p3), 5)
    pygame.draw.line(screen, c, (p3, p0), (p3, p3), 5)


    if check_grid(grid):
        c = (0, 0, 0)
    else:
        c = (255, 0, 0)

    for y in range(9):
        for x in range(9):
            if grid[y][x] != 0:
                if locked[y][x]:
                    text_surface = font.render(str(grid[y][x]), True, (0, 0, 255))
                else:
                    text_surface = font.render(str(grid[y][x]), True, c)
                x_ = (x + 0.5) * GRID_SIZE + BORDER_SIZE - text_surface.get_rect().width / 2
                y_ = (y + 0.5) * GRID_SIZE + BORDER_SIZE - text_surface.get_rect().height / 2
                
                screen.blit(text_surface, (x_, y_))

    pygame.display.flip()



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
                else:
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


    if solving:
        while locked[selected[0]][selected[1]]:
            next_cell()

        l = possible_lists[selected[0]][selected[1]]
        if l == None:
            l = possible_moves(grid, selected[1], selected[0])

        if len(l) != 0:
            choice = random.choice(l)
            l.remove(choice)
            possible_lists[selected[0]][selected[1]] = l
            
            #time.sleep(0.1)
            grid[selected[0]][selected[1]] = choice
            next_cell()
        else:
            grid[selected[0]][selected[1]] = 0
            possible_lists[selected[0]][selected[1]] = None
            last_cell()
            while locked[selected[0]][selected[1]]:
                last_cell()
            
    draw_grid()
    

pygame.quit()
