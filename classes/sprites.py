import pygame
from settings import *
from helpers.helpers import draw_tile


class GameEntity(pygame.sprite.Sprite):
    def __init__(self, x, y, count=0):
        self.x = x
        self.y = y
        self.count = count

    def get_position(self):
        return (self.x, self.y)


def lerp(start, end, t):
    return start + (end - start) * t


class Player(GameEntity):
    PLAYER_SPEED = 10

    def __init__(self, x, y, health, game):
        super().__init__(x, y)
        self.health = health
        self.inventory = []
        self.vx = 0
        self.vy = 0
        self.game = game

    def update(self):
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.stop()

    def set_velocity(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def stop(self):
        self.vx = 0
        self.vy = 0

    def handle_movement(self, map_width, map_height, map_data):
        vx, vy = 0, 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            vx -= self.PLAYER_SPEED
        if keys[pygame.K_d]:
            vx += self.PLAYER_SPEED
        if keys[pygame.K_w]:
            vy -= self.PLAYER_SPEED
        if keys[pygame.K_s]:
            vy += self.PLAYER_SPEED
        if vx != 0 and vy != 0:
            vx *= 0.7071
            vy *= 0.7071

        if 0 <= self.x + vx * self.game.dt < map_width and 0 <= self.y + vy * self.game.dt < map_height:
            if map_data[int(self.y + vy * self.game.dt)][int(self.x + vx * self.game.dt)] not in ['1', 'X']:
                self.set_velocity(vx, vy)

    def draw(self, SCREEN, camera_x_offset, camera_y_offset):
        draw_tile(SCREEN, self.x, self.y,
                  COLORS['P'], camera_x_offset, camera_y_offset)


class Enemy(GameEntity):
    total_count = 0

    def __init__(self, x, y, count, strength):
        super().__init__(x, y, count)
        self.strength = strength
        self.alive = True
        self.speed = 1
        Enemy.total_count += 1

    def move(self, new_x, new_y):
        self.x = new_x * self.speed
        self.y = new_y * self.speed
        print(f"Enemy moved to ({self.x}, {self.y})")

    def attack(self, player):
        if self.alive:
            player.take_damage(self.strength)

    def take_damage(self, amount):
        if amount >= self.strength:
            self.alive = False
            print("Enemy defeated")

    @classmethod
    def get_total_count(cls):
        return cls.total_count


class Collectible(GameEntity):
    total_count = 0

    def __init__(self, x, y, count):
        super().__init__(x, y, count)
        self.collected = False
        Collectible.total_count += 1

    def collect(self):
        self.collected = True
        print(f"Collectible collected!")

    @classmethod
    def get_total_count(cls):
        return cls.total_count


class Exit(GameEntity):
    def __init__(self, x, y, is_open=False):
        super().__init__(x, y)
        self.is_open = is_open

    def open_exit(self):
        self.is_open = True
        print("Exit is now open!")

    def close_exit(self):
        self.is_open = False
        print("Exit is now closed!")

    def check_reached(self, player):
        if self.is_open and self.get_position() == player.get_position():
            print("Player reached the exit! You win!")
