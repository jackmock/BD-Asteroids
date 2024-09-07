import pygame, constants, random
from circleshape import CircleShape

class Asteroid(CircleShape):
    
    containers = []

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)  # This will be set by AsteroidField

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_vel_1 = self.velocity.rotate(random_angle)
            new_vel_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

            x, y = self.position.x, self.position.y

            new_ast_1 = Asteroid(x, y, new_radius)
            new_ast_2 = Asteroid(x, y, new_radius)
            new_ast_1.velocity = new_vel_1 * constants.ASTEROID_SCALER
            new_ast_2.velocity = new_vel_2 * constants.ASTEROID_SCALER
