from Player import *
from Ground import *

class GameMode:
    def __init__(self, player, ground):
        self.player = player
        self.ground = ground

    def check_collision(self, ground):
        player_rect = self.player.rect.copy()  # Create a copy of self.player.rect
        player_rect.move_ip(self.player.position.x - self.player.width / 2, self.player.position.y - self.player.rect_height / 2)  # Move the rect to player's current position
        return player_rect.colliderect(ground.rect)  # Perform collision detection

    def check_movement(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            if self.player.velocity.x >= 0:
                self.player.velocity.x -= self.player.x_acceleration * 2  # Increased acceleration when changing direction
            else:
                self.player.velocity.x -= self.player.x_acceleration
        elif keys[pg.K_d]:
            if self.player.velocity.x <= 0:
                self.player.velocity.x += self.player.x_acceleration * 2  # Increased acceleration when changing direction
            else:
                self.player.velocity.x += self.player.x_acceleration
        elif self.player.on_ground:
            # Apply friction to gradually slow down the player's horizontal movement (when not moving on the ground)
            if self.player.velocity.x > 0:
                self.player.velocity.x = max(0, self.player.velocity.x - (self.player.stopping_friction * 0.8))
            elif self.player.velocity.x < 0:
                self.player.velocity.x = min(0, self.player.velocity.x + (self.player.stopping_friction * 0.8))
            else:
                self.player.x_acceleration = 0.25  # Reset acceleration when not moving

        # Adjust the maximum speed based on boost key
        if keys[pg.K_w] and (self.player.velocity.x > 0 or self.player.velocity.x < 0):
            self.player.max_speed = 20
        else:
            self.player.max_speed = 10

        # Limit the player's velocity to the maximum speed
        self.player.velocity.x = max(-self.player.max_speed, min(self.player.max_speed, self.player.velocity.x))

        if keys[pg.K_SPACE] and not self.player.jump_key_down:
            self.player.jump_key_down = True
            if not self.player.is_jumping:
                self.player.is_jumping = True
                self.player.velocity.y = self.player.jump_power  # Adjust the jump height as needed
                self.player.jump_count += 1
            elif self.player.is_jumping and self.player.jump_count < self.player.max_jump_count:
                self.player.velocity.y = self.player.jump_power  # Adjust the double jump height as needed
                self.player.jump_count += 1
        elif not keys[pg.K_SPACE]:
            self.player.jump_key_down = False

        self.player.position += self.player.velocity
            
    def check_border_constraints(self, width, height):
        # Clamp the player's x position within the screen boundaries
        self.player.position.x = max(self.player.radius, min(self.player.position.x, width - self.player.radius))

        # Clamp the player's y position within the screen boundaries
        self.player.position.y = max(self.player.radius, min(self.player.position.y, height - self.player.radius))

        if self.player.position.y >= height - self.player.radius:
            self.player.is_jumping = False
            self.player.jump_count = 0

        # Check collision with the ground
        self.player.on_ground = self.check_collision(self.ground)
        
    def update_physics(self):
        # if self.player.on_ground:
        #     self.player.velocity.y = 0
            
        self.player.position += self.player.velocity
        
        if self.player.is_jumping:
            self.player.velocity.y += self.player.y_acceleration  # Adjust the gravity value as needed
            
        # Check the x velocity range to determine the player shape
        if abs(self.player.velocity.x) <= 10 and self.player.on_ground:
            self.player.is_rectangle = True
        else:
            self.player.is_rectangle = False