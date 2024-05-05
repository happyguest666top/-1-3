from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("stock-vector-vector-cartoon-illustration-of-background-morning-jungle-bright-jungle-with-ferns-and-flowers-for-536303545.jpg"), (win_width, win_height))
game = True
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 3:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < win_width - 70:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.image = Surface((self.wall_width, self.wall_height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
happy1 = Wall(154, 205, 50, 0, 0, 800, 10)
happy2 = Wall(154, 205, 50, 0, 10, 10, 600)
happy3 = Wall(154, 205, 50, 690, 10, 10, 500)
happy4 = Wall(154, 205, 50, 200, 490, 500, 10)
happy5 = Wall(154, 205, 50, 200, 115, 10, 380)
happy6 = Wall(154, 205, 50, 500, 25, 10, 175)
happy7 = Wall(154, 205, 50, 400, 325, 75, 10)
happy8 = Wall(154, 205, 50, 400, 400, 200, 10)
player = Player("images-6jdu4LOkj-transformed.png", 50, win_height - 80, 4)
monster = Enemy("Ð_ÐµÐ·_Ð½Ð°Ð·Ð²Ð°Ð½Ð¸Ñ_-igcIeoAat-transformed.png", win_width - 80, 280, 3)
goal = GameSprite('images.jpg', 440, 420, 0)
mixer.init()
mixer.music.load("bdd6ff5ec5a8e214 (1).mp3")
mixer.music.play()
font.init()
font1 = font.Font(None, 70)
win = font1.render("YOU WIN!", True, (255, 215, 0))
lose = font1.render("YOU LOSE!", True, (255, 0, 0))
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        player.update()
        monster.update()
        goal.reset()
        player.reset()
        monster.reset()
        happy1.draw_wall()
        happy2.draw_wall()
        happy3.draw_wall()
        happy4.draw_wall()
        happy5.draw_wall()
        happy6.draw_wall()
        happy7.draw_wall()
        happy8.draw_wall()
        if sprite.collide_rect(player, goal):
            finish = True
            window.blit(win, (200, 200))
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, happy1) or sprite.collide_rect(player, happy2) or sprite.collide_rect(player, happy3) or sprite.collide_rect(player, happy4) or sprite.collide_rect(player, happy5) or sprite.collide_rect(player, happy6) or sprite.collide_rect(player, happy7):
            finish = True
            window.blit(lose, (200, 200))
    else:
        time.delay(3000)
        finish = False
        player = Player("images-6jdu4LOkj-transformed.png", 5, win_height-80, 4)
    display.update()
    clock.tick(FPS)
