import os 
import time 

# Defines the height and width of the canvas, tracks the movement of the terminalscribe class
class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height 
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

# Sets the position of dots on the canvas
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

# Clears the terminal to start the animation 
    def clear(self):
        os.system('cls' if os.name == 'NT' else 'clear')

# Prints lines to the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))


# Defines the placement of dots on the "canvas"
class TerminalScribe: 
    def __init__(self,canvas):
        self.canvas = canvas
        self.pos = [0,0]
        self.mark = '*'
        self.trail = '.'

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos 
        self.canvas.setPos(self.pos, self.mark)
        self.canvas.print()

canv = Canvas(20,20)
scribe = TerminalScribe(canv)

for i in range(0,10):
    for j in range(0,10):
        scribe.draw((i,j))