import sys
import pygame
import constants as c
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {c.SCREEN_WIDTH}")
    print(f"Screen height: {c.SCREEN_HEIGHT}")

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    setattr(Asteroid, "containers", (asteroids, updatable, drawable))
    setattr(Shot, "containers", (shots, updatable, drawable))
    setattr(AsteroidField, "containers", updatable)
    asteroidfield = AsteroidField()
    
    setattr(Player, "containers", (updatable, drawable))
    
    player = Player(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("GAME OVER MAN!")
                sys.exit()

            for shot in shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
