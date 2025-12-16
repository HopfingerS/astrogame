import pygame
import constants
from circleshape import CircleShape

class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, constants.SHOT_RADIUS)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, width=constants.LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    