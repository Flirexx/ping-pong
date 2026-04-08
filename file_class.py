from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, window, speed, name_image, x, y, w, h):
        super().__init__()
        self.window = window
        self.speed = speed
        self.image = transform.scale(image.load(name_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Rocket(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0: #нажата ли клавиша
            self.rect.y -= self.speed #смена координат
        
            

        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
            
    def move_2(self):
        keys = key.get_pressed()
        if keys[K_r] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_f] and self.rect.y < 400:
            self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self, window, speed, name_image, x, y, w, h):
        super().__init__(window, speed, name_image, x, y, w, h)
        self.speed_x = 3
        self.speed_y = 3
    def move_ball(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y >= 440:
            self.speed_y *= -1
            self.rect.y += self.speed_y
            
        if self.rect.y <= 0:
            self.speed_y *= -1
            self.rect.y += self.speed_y
