import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    running = True
    
    clock = pygame.time.Clock()
    dt = 0 # time in seconds since last frame
    
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        
        clock.tick(60)
        
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
