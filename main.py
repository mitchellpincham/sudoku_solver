import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
font = pygame.font.Font(pygame.font.get_default_font(), 36)

GRID_SIZE = 50
BORDER_SIZE = 20

grid = [[0 for i in range(9)] for _ in range(9)]

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
                text_surface = font.render(str(grid[y][x]), True, c)
                x_ = (x + 0.5) * GRID_SIZE + BORDER_SIZE - text_surface.get_rect().width / 2
                y_ = (y + 0.5) * GRID_SIZE + BORDER_SIZE - text_surface.get_rect().height / 2
                
                screen.blit(text_surface, (x_, y_))

    pygame.display.flip()



running = True

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
            
            if event.key == pygame.K_1:
                grid[selected[0]][selected[1]] = 1
            elif event.key == pygame.K_2:
                grid[selected[0]][selected[1]] = 2
            elif event.key == pygame.K_3:
                grid[selected[0]][selected[1]] = 3
            elif event.key == pygame.K_4:
                grid[selected[0]][selected[1]] = 4
            elif event.key == pygame.K_5:
                grid[selected[0]][selected[1]] = 5
            elif event.key == pygame.K_6:
                grid[selected[0]][selected[1]] = 6
            elif event.key == pygame.K_7:
                grid[selected[0]][selected[1]] = 7
            elif event.key == pygame.K_8:
                grid[selected[0]][selected[1]] = 8
            elif event.key == pygame.K_9:
                grid[selected[0]][selected[1]] = 9
                
            elif event.key in [pygame.K_w, pygame.K_UP]:
                if selected[0] != 0:
                    selected[0] -= 1
            elif event.key in [pygame.K_a, pygame.K_LEFT]:
                if selected[1] != 0:
                    selected[1] -= 1
            elif event.key in [pygame.K_s, pygame.K_DOWN]:
                if selected[0] != 8:
                    selected[0] += 1
            elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                if selected[1] != 8:
                    selected[1] += 1

            elif event.key == pygame.K_l:
                grid = load_example()
            elif event.key == pygame.K_c:
                print(check_grid(grid))

          
          
    draw_grid()
    


pygame.quit()
