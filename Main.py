import sys
import pygame as pg
from pygame.locals import *

from Player import *
from Ground import *
from GameMode import *

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 720

player_x = 1240
player_y = 680
player_radius = 40

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

# Set the window name
pg.display.set_caption("My Game Window") # Replace "My Game Window" with your desired window namew

player = Player(player_x, player_y, player_radius)
ground = Ground(0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20, (0, 255, 0))

game_mode = GameMode(player, ground)

pg.init()

while True:
    screen.fill("black") # Fill the display with a solid color
    # Draw the ground
    ground.draw(screen)

    # Render the graphics here
    player.draw(screen)

    # Code for Player Movement
    game_mode.check_movement()
    
    # Check collision with the ground
    if game_mode.check_collision(ground):
        player.on_ground = True
    else:
        player.on_ground = False

    # Update Player Physics
    game_mode.update_physics()

    # Code for Border Constraints
    game_mode.check_border_constraints(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Process player inputs.    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            # Escape Window to Quit
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

    pg.display.flip()  # Refresh on-screen display
    clock.tick(60)     # Wait until the next frame (at 60 FPS)