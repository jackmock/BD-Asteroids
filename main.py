import pygame, constants
from player import Player

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

    Player.containers = [updatable, drawable]

    player_obj = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.PLAYER_RADIUS)
    updatable.add(player_obj)
    drawable.add(player_obj)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        for sprite in drawable:
            sprite.draw(screen)

        for item in updatable:
            item.update(dt)          
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

