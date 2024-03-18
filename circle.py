from setting import *
import math
class Circlegen:
    def __init__(self,tileAmount,tileSize,boxColor,barColor):
        self.tileAmount = tileAmount
        self.tileSize = tileSize
        self.boxColor = boxColor
        self.barColor = barColor
        self.barSpeed = (360 / self.tileAmount) / 5
        self.angle = 0
        self.bar = (WIDTH / 2) - self.tileSize / 2
        self.grid = self.createGrid()
        self.barPoint = self.getBarPoint()


        self.circlePos = []

    def createGrid(self):
        grid = []
        for r in range(self.tileAmount):
            row = []
            for c in range(self.tileAmount):
                row.append(0)
            grid.append(row)
        return grid

    def getBarPoint(self):
        angle = self.angle
        angle = math.radians(angle)
        x = math.cos(angle) * self.bar
        y = math.sin(angle) * self.bar

        x += WIDTH / 2
        y += HEIGHT / 2

        return (x,y)

    def makeCircleBox(self):
        box = (int(self.barPoint[0] // self.tileSize),int(self.barPoint[1] // self.tileSize))
        if 0 <= box[0] < len(self.grid) and 0 <= box[1] < len(self.grid):
            if self.grid[box[1]][box[0]] == 0:
                self.grid[box[1]][box[0]] = 1

    def displayLines(self):
        for i in range(self.tileAmount + 1):
            pygame.draw.line(screen,"#2d3436",(0,i * self.tileSize),(WIDTH,i * self.tileSize))
            pygame.draw.line(screen, "#2d3436", (i * self.tileSize, 0), (i * self.tileSize, HEIGHT))

    def displayGrid(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] == 1:
                    pygame.draw.rect(screen,self.boxColor,(c * self.tileSize,r * self.tileSize,self.tileSize,self.tileSize))

    def displayBar(self):
        pygame.draw.circle(screen,self.barColor,(WIDTH/2,HEIGHT/2),self.tileSize / 2)
        pygame.draw.line(screen,self.barColor,(WIDTH/2,HEIGHT/2),(self.barPoint),5)

    def update(self):
        self.barPoint = self.getBarPoint()
        if self.angle < 360:
            self.angle += self.barSpeed
        self.makeCircleBox()

    def display(self):
        self.update()
        self.displayGrid()
        self.displayLines()
        self.displayBar()


circle = Circlegen(TILEAMOUNT,TILESIZE,"#e74c3c","#3498db")
