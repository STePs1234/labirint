#создай игру "Лабиринт"!
from  pygame import *
win = display.set_mode((700,500))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'),(700,500))
game=True

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(60,60))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def show(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x  >5:
            self.rect.x  -= self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x  < 650:
            self.rect.x += self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 615:
            self.direction = 'left'
        if self.direction =='left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color=(color_1,color_2,color_3)
        self.width=wall_width
        self.height=wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        draw.rect(win,self.color,(self.rect.x, self.rect.y, self.width, self.height))
clock = time.Clock()
fps = 60
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
player=Player('hero.png',20,430,5)
enemy=Enemy('cyborg.png',620,280,2)
treasure=GameSprite('treasure.png',620,430,0)
w1 = Wall(154, 205, 50, 110, 20 , 450, 10)
w2 = Wall(154, 205, 50, 180, 350, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)
w4 = Wall(154, 205, 50, 450, 100, 10, 380)
finish=False
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        win.blit(background,(0,0))
        player.update()
        enemy.update()
        player.show()
        enemy.show()
        treasure.show()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
    display.update()
    clock.tick(fps)
