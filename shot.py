from circleshape import CircleShape
import constants
import pygame

class Shot(CircleShape):

    containers = []

    def __init__(self, pos, vel):
        super().__init__(pos.x, pos.y, constants.SHOT_RADIUS)
        self.velocity = vel
        for container in self.containers:
            container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)