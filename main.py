from pygame import *
from random import randint
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
        
        
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        elif keys[K_RIGHT] and self.rect.x < win_width - 85:
            self.rect.x += self.speed
    def file(self):
        pass
        
img_back = "galaxy.jpg"
img_hero = "rocket.png"
img_enemy = "ufo.png"
img_bullet = "bullet.png"
img_asteroid = "asteroid.png"
    
win_width = 700
win_height = 500
display.set_caption("Shooter")
mw = display.set_mode((win_width, win_width))
background = transform.scale(image.load(img_back), (win_width, win_height))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
file_sound = mixer.Sound('fire.ogg')

player = Player("rocket.png", 5, 250, win_height-100, 80, 100 )

game=True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False      
        mw.blit(background, (0,0))
        player.reset()
        player.update()
        display.update()
        
