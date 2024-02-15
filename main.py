import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
font = pygame.font.Font(pygame.font.get_default_font(), 36)

GRID_SIZE = 50
BORDER_SIZE = 20

grid = [[0 for i in range(9)] for _ in range(9)]



selected = [0, 0]

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x = int((pos[0] - BORDER_SIZE) / GRID_SIZE)
            y = int((pos[1] - BORDER_SIZE) / GRID_SIZE)
            if 0 < x < 10 and 0 < y < 10:
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

    for y in range(9):
        for x in range(9):
            text_surface = font.render(str(grid[y][x]), True, (0, 0, 0))
            screen.blit(text_surface, (x * GRID_SIZE + BORDER_SIZE, y * GRID_SIZE + BORDER_SIZE))

    pygame.display.flip()


pygame.quit()
