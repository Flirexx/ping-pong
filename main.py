from pygame import *
x = 700
y = 500
win = display.set_mode((x, y))
win.fill((122, 77, 129))
display.update()
game = True
while game:
  for e in event.get():
    if e.type == QUIT:
      game = False
