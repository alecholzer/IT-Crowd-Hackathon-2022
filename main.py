# WSU 2022 Hackathon
# Adam Hagengruber

import pygame
import sys

# Initialize sprite class:
class Sprite(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.center = pos

# Initialize ground class:
class Ground(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([300,20])
        self.image.fill((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.center = pos

# Main function:
def main():
    # Initialize pygame:
    pygame.init()
    clock = pygame.time.Clock()
    fps = 50
    bg = [0,0,0]
    size = [300,300]
    screen = pygame.display.set_mode(size)

    #Logic variables:
    jump = False
    gravity = 1
    onGround = False

    # Player initialization:
    player = Sprite([40,250])
    player_group = pygame.sprite.Group()
    player_group.add(player)
    previousx = player.rect.x
    previousy = player.rect.y
    player.vy = 5
    player.vx = 5

    # Wall initialization:
    wall = Sprite([100,60])
    wall_group = pygame.sprite.Group()
    wall_group.add(wall)

    # Ground initialization:
    ground = Ground([150,290])
    ground_group = pygame.sprite.Group()
    ground_group.add(ground)

    while True:
        # Set loop end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        # Get keyboard input:
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.rect.x -= 1
        if key[pygame.K_RIGHT]:
            player.rect.x += 1

        # Gravity logic:
        if onGround == False:
            player.rect.y += 1

        # Jump logic:
        if jump == False and key[pygame.K_SPACE]:
            jump = True

        if jump == True:
            player.rect.y -= player.vy
            player.vy -= 1
            onGround = True
            if player.vy < -5:
                jump = False
                player.vy = 5

        # Hit commands:
        hitGround = pygame.sprite.spritecollide(player, ground_group, False)
        hitWall = pygame.sprite.spritecollide(player, wall_group, False)

        # Check ground:
        if hitGround:
            onGround = True
        else:
            onGround = False

        # Check wall:
        if hitWall:
            player.rect.x = previousx
            player.rect.y = previousy
        else:
            previousx = player.rect.x
            previousy = player.rect.y

        # Output to display:
        screen.fill(bg)
        player_group.draw(screen)
        wall_group.draw(screen)
        pygame.display.update()
        clock.tick(fps)

    # Exit game:
    pygame.quit()
    sys.exit

main()