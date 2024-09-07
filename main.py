import pygame, constants, sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
#from circleshape import CircleShape

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = [updatable, drawable]
    Asteroid.containers = [asteroids, updatable, drawable]
    AsteroidField.containers = [updatable]
    Shot.containers = [updatable, drawable, shots]
    
    asteroidField_obj = AsteroidField()
    player_obj = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.PLAYER_RADIUS)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        for sprite in drawable:
            sprite.draw(screen)

        for item in updatable:
            item.update(dt)
            for asteroid in asteroids:
                if player_obj.check_collision(asteroid):
                    print("Game over!")
                    pygame.quit()
                    sys.exit()
                for bullet in shots:
                    if asteroid.check_collision(bullet):
                        asteroid.kill()
                        bullet.kill()
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

