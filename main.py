# WSU 2022 Hackathon
# Adam Hagengruber

import pygame
import sys

# Initialize sprite class:
class Sprite(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
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
    player = Sprite([40,50])
    jump = False

    # Set move values:
    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    player.vx = 5
    player.vy = 5

    previousx = player.rect.x
    previousy = player.rect.y
    wall = Sprite([100,60])

    wall_group = pygame.sprite.Group()
    wall_group.add(wall)

    player_group = pygame.sprite.Group()
    player_group.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        # Get keyboard input from user:
        key = pygame.key.get_pressed()

        # Move logic:
        if key[pygame.K_LEFT]:
            player.rect.x -= 1
        if key[pygame.K_RIGHT]:
            player.rect.x += 1
        #if key[pygame.K_UP]:
        #    player.rect.y -= 1
        #if key[pygame.K_DOWN]:
        #   player.rect.y += 1

        # Jump logic:
        if jump == False and key[pygame.K_SPACE]:
            jump = True

        if jump == True:
            player.rect.y -= player.vy
            player.vy -= 1
            if player.vy < -5:
                jump = False
                player.vy = 5

        # Hit logic:
        hit = pygame.sprite.spritecollide(player, wall_group, False)
        if hit:
            player.image.fill((255,255,255))
            player.rect.x = previousx
            player.rect.y = previousy
        else:
            if player.image.fill != (255,0,255):
                player.image.fill((255,0,255))
            previousx = player.rect.x
            previousy = player.rect.y

        # Delay:
        pygame.time.delay(50)
        player_group.draw(screen)
        wall_group.draw(screen)
        pygame.display.update()
        clock.tick(fps)
        screen.fill(bg)

    pygame.quit()
    sys.exit

# Call main:
main()