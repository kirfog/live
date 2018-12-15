import pygame
import numpy

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

        self.cells=[]

    def draw_grid(self):
        for x in range(self.cell_width):
            pygame.draw.line(self.screen, pygame.Color('black'), (x*self.cell_size, 0), (x*self.cell_size, self.height))
        for y in range(self.cell_height):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y*self.cell_size), (self.width, y*self.cell_size))

    def cell_list(self, randomize=False):
        if randomize:
            cells = numpy.random.randint(2, size=(self.cell_width, self.cell_height))
        else:
            cells = numpy.random.randint(1, size=(self.cell_width, self.cell_height))
        return cells   

    def tern(self, cells):
        z=len(cells)
        nextcells = numpy.random.randint(1, size=(z, z))
        a = numpy.random.randint(1, size=(z+2, z+2))
        b = numpy.random.randint(1, size=(z+2, z+2))

        for x in range(0, z):
            for y in range(0, z):
                a[x+1,y+1] = cells[x,y]

        for x in range(1, z+1):
            for y in range(1, z+1):
                c = 0
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        if not (i == x and j == y):
                            c = c + a[i,j]
                if a[x, y] == 0 and c == 3:
                    b[x, y] = 1
                elif(a[x,y] == 1 and c > 3) or (a[x,y] == 1 and c < 2):
                    b[x, y] = 0
                else:
                    b[x, y] = a[x, y]

        for x in range(0, z):
            for y in range(0, z):
                nextcells[x,y] = b[x+1,y+1]

        return(nextcells)

    def draw_cell_list (self, cells):
        for x in range (self.cell_width):
            for y in range (self.cell_height):
                if cells[x][y] == 0:
                    pygame.draw.rect(self.screen, pygame.Color('white'), ((x)*self.cell_size,(y)*self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('green'), ((x)*self.cell_size,(y)*self.cell_size, self.cell_size, self.cell_size))

    def cell_click (self, pos):
        self.cells[pos[0]//self.cell_size][pos[1]//self.cell_size] = 1
  
    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        self.cells = self.cell_list(True)
        running = True
        while running:
            self.cells = self.tern(self.cells)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.cell_click(pos)
            self.draw_cell_list(self.cells)
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

if __name__ == '__main__':
    game = GameOfLife()
    game.run()