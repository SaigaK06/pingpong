from pygame import *
from random import *

window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('fon.png'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, size_1, size_2):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_1, size_2))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_1 = size_1
        self.size_2 = size_2

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 345:
            self.rect.y += self.speed
    
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 345:
            self.rect.y += self.speed
        
ball = GameSprite('ball.png', 4, 320, 220, 50, 50)
player_1 = Player('platforma.png', 4, 5, 10, 50, 150)
player_2 = Player('platforma.png', 4, 645, 340, 50, 150)

game = True
finish = False
clock = time.Clock()
vx = 3
vy = 3

font.init()
font1 = font.SysFont('Arial', 40)
win_1 = font1.render('ВЫИГРАЛ ИГРОК №1 :)', True, (0, 215, 0))
win_2 = font1.render('ВЫИГРАЛ ИГРОК №2 :)', True, (0, 215, 0))

while game:
    for e in event.get(): 
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(background, (0, 0))
        ball.reset()
        ball.rect.x += vx 
        ball.rect.y -= vy
        player_1.reset()
        player_2.reset()
        player_1.update_left()
        player_2.update_right()

        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            vx = vx * (-1)


        if ball.rect.y < 0 or ball.rect.y > 450:
            vy = vy * (-1)

        if ball.rect.x < 1:
            finish = True
            window.blit(win_2, (170, 200))

        if ball.rect.x > 650:
            finish = True
            window.blit(win_1, (170, 200))

    display.update()
    clock.tick(60)