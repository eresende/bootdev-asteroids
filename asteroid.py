import pygame
import random

import constants as c
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= c.ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        vect1 = self.velocity.rotate(random_angle)
        vect2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - c.ASTEROID_MIN_RADIUS
      
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vect1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vect2 * 1.2
