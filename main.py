from pygame import *
from file_class import GameSprite, Rocket
x = 700
y = 500
win = display.set_mode((x, y))
rocket2 = Rocket(win, 5, 'media/rocket.png', 600, 180, 30, 100)
win.fill((122, 77, 129))
rocket = Rocket(win, 5, 'media/rocket.png', 50, 180, 30, 100)
game = True
clock = time.Clock()
while game:
  clock.tick(60)
  for e in event.get():
    if e.type == QUIT:
      game = False
  
  rocket.move()
  rocket2.move_2()
  win.fill((122, 77, 129))
  win.blit(rocket.image, (rocket.rect.x, rocket.rect.y))
  win.blit(rocket2.image, (rocket2.rect.x, rocket2.rect.y))
  
   


  display.update()
