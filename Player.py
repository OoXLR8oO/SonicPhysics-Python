import pygame as pg
from pygame.math import Vector2


class Player:
    def __init__(self, x, y, radius):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.radius = radius
        self.width = radius * 2
        
        self.x_acceleration = 0.25
        self.y_acceleration = 1
        
        self.max_speed = 10
        self.stopping_friction = 1
        
        self.is_jumping = False
        self.jump_key_down = False
        self.jump_power = -17
        self.max_jump_count = 1
        self.jump_count = 0

        self.on_ground = False
        self.is_rectangle = False  # Flag to determine the player shape

        # Create surfaces for the shapes
        self.circle_surface = pg.Surface((self.width, self.width), pg.SRCALPHA)
        self.circle_surface.fill((0, 0, 0, 0))  # Fill with transparent color
        pg.draw.circle(self.circle_surface, (0, 0, 255), (self.radius, self.radius), self.radius)

        self.rect_height = 150
        self.rect_surface = pg.Surface((self.width, self.rect_height), pg.SRCALPHA)
        self.rect_surface.fill((0, 0, 0, 0))  # Fill with transparent color
        self.rect = pg.draw.rect(self.rect_surface, (0, 0, 255), (0, 0, self.width, self.rect_height))

    def draw(self, screen):
        if self.is_rectangle:
            rect_pos = (self.position.x - self.width / 2, self.position.y - self.rect_height / 2)
            rect_size = (self.width, self.rect_height)
            pg.draw.rect(screen, (0, 0, 255), rect_pos + rect_size)
        else:
            circle_center = (self.position.x, self.position.y)
            pg.draw.circle(screen, (0, 0, 255), circle_center, self.radius)
