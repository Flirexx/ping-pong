from pygame import *
from file_class import GameSprite, Rocket, Ball
font.init()
x = 700
y = 500
win = display.set_mode((x, y))
rocket2 = Rocket(win, 5, 'media/rocket.png', 600, 180, 30, 100)
win.fill((122, 77, 129))
rocket = Rocket(win, 5, 'media/rocket.png', 50, 180, 30, 100)
ball = Ball(win, 1, 'media/ball.png', 350, 250, 60, 60)
font1 = font.Font(None, 35)
lose = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))
game = True
ok = True
clock = time.Clock()
while game:
  clock.tick(60)
  for e in event.get():
    if e.type == QUIT:
      game = False
  if ok:
    rocket.move()
    rocket2.move_2()
    win.fill((122, 77, 129))
    win.blit(rocket.image, (rocket.rect.x, rocket.rect.y))
    win.blit(rocket2.image, (rocket2.rect.x, rocket2.rect.y))
    win.blit(ball.image, (ball.rect.x, ball.rect.y))
    ball.move_ball()
    if sprite.collide_rect(rocket, ball) or sprite.collide_rect(rocket2, ball):
      ball.speed_x *= -1
    if ball.rect.x < 0:
      win.blit(lose, (250, 250))
      ok = False
    if ball.rect.x > 640:
      win.blit(lose2, (250, 250))
      ok = False
    
    
    
  
   


  display.update()
