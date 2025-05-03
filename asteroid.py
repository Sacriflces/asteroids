import pygame
from circleshape import CircleShape
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        child_angle = random.uniform(20, 50)
        child_1_direction = self.velocity.rotate(child_angle)
        child_2_direction = self.velocity.rotate(-child_angle)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child_1 = Asteroid(self.position[0], self.position[1], child_radius)
        child_2 = Asteroid(self.position[0], self.position[1], child_radius)
        child_1.velocity = child_1_direction
        child_2.velocity = child_2_direction


        