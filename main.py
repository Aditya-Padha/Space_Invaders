import pygame
import pygame.draw
pygame.init()

window_height = 600
window_width = 800
rows = 3
cols = 10

clock = pygame.time.Clock()

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders")

background = pygame.image.load("Images/background.jpg")

invaders_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
playerBullet_group = pygame.sprite.Group()
InvaderBullet_group = pygame.sprite.Group()


class Invader(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/spaceInvaders.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1

        if self.move_counter > 75:
            self.move_direction *= -1
            self.move_counter *= -1


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/user.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        speed = 3
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed

        if key[pygame.K_RIGHT] and self.rect.right < window_width:
            self.rect.x += speed


def create_invaders():
    for row in range(rows):
        for col in range(cols):
            invader = Invader(100 + col * 65, 80 + row * 50)
            invaders_group.add(invader)


create_invaders()

player = Player(int(window_width/2), window_height - 100)
player_group.add(player)
game = True

while game:
    clock.tick(60)
    screen.blit(background, (0, 0))

    invaders_group.update()
    player_group.update()

    invaders_group.draw(screen)
    player_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.update()

pygame.quit()
