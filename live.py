import random
import pygame
from pygame.locals import *


class GameOfLife:
    def __init__(self, width = 1000, height = 1000, cell_size = 20, speed = 2):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)

        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.speed = speed

        self.cels=[]

    def draw_grid(self):
        for x in range(self.cell_width):
            pygame.draw.line(self.screen, pygame.Color('black'), (x*self.cell_size, 0), (x*self.cell_size, self.height))
        for y in range(self.cell_height):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y*self.cell_size), (self.width, y*self.cell_size))

    def cell_list(self, randomize=False):
        if randomize:
            cels = [[random.randint(0, 1) * 1 for x in range (self.cell_width)] * 1 for y in range (self.cell_height)]
        else:
            cels = [[0 * 1 for x in range (self.cell_width)] * 1 for y in range (self.cell_height)]
        return cels

    def cell_count(self, cels):
        nextcels = [[0 * 1 for x in range (self.cell_width)] * 1 for y in range (self.cell_height)]
        for x in range (self.cell_width):
            for y in range (self.cell_height):
                n = 0
                m = 0
                for a in range(x-1, x+1):
                    for b in range(y-1, y+1):
                        if a == x and b == y:
                            pass
                        else:
                            if cels[a][b] == 1:
                                m = m + 1
                try:
                    n1 = cels[x-1][y-1]
                except IndexError:
                    n1 = 0
                try:
                    n2 = cels[x-1][y]
                except IndexError:
                    n2 = 0
                try:
                    n3 = cels[x-1][y+1]
                except IndexError:
                    n3 = 0
                try:
                    n4 = cels[x][y-1]
                except IndexError:
                    n4 = 0
                try:
                    n5 = cels[x][y+1]
                except IndexError:
                    n5 = 0
                try:
                    n6 = cels[x+1][y-1]
                except IndexError:
                    n6 = 0
                try:
                    n7 = cels[x+1][y]
                except IndexError:
                    n7 = 0
                try:    
                    n8 = cels[x+1][y+1]
                except IndexError:
                    n8 = 0
                n = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                #print(n, m)
                if (cels[x][y] == 1 and n > 3) or (cels[x][y] == 1 and n < 2):
                    nextcels[x][y] = 0
                elif cels[x][y] == 0 and n == 3:
                    nextcels[x][y] = 1
                else:
                    nextcels[x][y] = cels[x][y]
        return nextcels



    def draw_cell_list (self, cels):
        for x in range (self.cell_width):
            for y in range (self.cell_height):
                if cels[x][y] == 0:
                    pygame.draw.rect(self.screen, pygame.Color('white'), ((x)*self.cell_size,(y)*self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('green'), ((x)*self.cell_size,(y)*self.cell_size, self.cell_size, self.cell_size))

    def cell_click (self, pos):
        self.cels[pos[0]//self.cell_size][pos[1]//self.cell_size] = 1
  
    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        self.cels = self.cell_list(True)
        running = True
        while running:
            self.cels = self.cell_count(self.cels)
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.cell_click(pos)
            self.draw_cell_list(self.cels)
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

if __name__ == '__main__':
    game = GameOfLife()
    game.run()