import pygame
from settings import *
from helpers.helpers import cart_to_iso
import math


class GameEntity(pygame.sprite.Sprite):
    def __init__(self, x, y, count=0):
        self.x = x
        self.y = y
        self.count = count

    def get_position(self):
        return (self.x, self.y)


class Player(GameEntity):
    PLAYER_SPEED = 10
    idle_sprites = {
        'E': pygame.image.load('assets/sprites/player/warrior_armed_idle/E/warrior_armed_idle_E_0.0_0.png'),
        'N': pygame.image.load('assets/sprites/player/warrior_armed_idle/N/warrior_armed_idle_N_90.0_0.png'),
        'NE': pygame.image.load('assets/sprites/player/warrior_armed_idle/NE/warrior_armed_idle_NE_45.0_0.png'),
        'NEE': pygame.image.load('assets/sprites/player/warrior_armed_idle/NEE/warrior_armed_idle_NEE_22.5_0.png'),
        'NNE': pygame.image.load('assets/sprites/player/warrior_armed_idle/NNE/warrior_armed_idle_NNE_67.5_0.png'),
        'NNW': pygame.image.load('assets/sprites/player/warrior_armed_idle/NNW/warrior_armed_idle_NNW_112.5_0.png'),
        'NW': pygame.image.load('assets/sprites/player/warrior_armed_idle/NW/warrior_armed_idle_NW_135.0_0.png'),
        'NWW': pygame.image.load('assets/sprites/player/warrior_armed_idle/NWW/warrior_armed_idle_NWW_157.5_0.png'),
        'S': pygame.image.load('assets/sprites/player/warrior_armed_idle/S/warrior_armed_idle_S_270.0_0.png'),
        'SE': pygame.image.load('assets/sprites/player/warrior_armed_idle/SE/warrior_armed_idle_SE_315.0_0.png'),
        'SEE': pygame.image.load('assets/sprites/player/warrior_armed_idle/SEE/warrior_armed_idle_SEE_337.5_0.png'),
        'SSE': pygame.image.load('assets/sprites/player/warrior_armed_idle/SSE/warrior_armed_idle_SSE_292.5_0.png'),
        'SSW': pygame.image.load('assets/sprites/player/warrior_armed_idle/SSW/warrior_armed_idle_SSW_247.5_0.png'),
        'SW': pygame.image.load('assets/sprites/player/warrior_armed_idle/SW/warrior_armed_idle_SW_225.0_0.png'),
        'SWW': pygame.image.load('assets/sprites/player/warrior_armed_idle/SWW/warrior_armed_idle_SWW_202.5_0.png'),
        'W': pygame.image.load('assets/sprites/player/warrior_armed_idle/W/warrior_armed_idle_W_180.0_0.png'),
    }
    walking_sprites = {
        'E': [pygame.image.load('assets/sprites/player/warrior_armed_walk/E/warrior_armed_walk_E_0.0_0.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/E/warrior_armed_walk_E_0.0_1.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/E/warrior_armed_walk_E_0.0_2.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/E/warrior_armed_walk_E_0.0_3.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/E/warrior_armed_walk_E_0.0_4.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/E/warrior_armed_walk_E_0.0_5.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/E/warrior_armed_walk_E_0.0_6.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/E/warrior_armed_walk_E_0.0_7.png')
              ],
        'N': [pygame.image.load('assets/sprites/player/warrior_armed_walk/N/warrior_armed_walk_N_90.0_0.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/N/warrior_armed_walk_N_90.0_1.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/N/warrior_armed_walk_N_90.0_2.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/N/warrior_armed_walk_N_90.0_3.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/N/warrior_armed_walk_N_90.0_4.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/N/warrior_armed_walk_N_90.0_5.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/N/warrior_armed_walk_N_90.0_6.png'),
              pygame.image.load(
                  'assets/sprites/player/warrior_armed_walk/N/warrior_armed_walk_N_90.0_7.png'),
              ],
        'NE': [pygame.image.load('assets/sprites/player/warrior_armed_walk/NE/warrior_armed_walk_NE_45.0_0.png'),
               pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NE/warrior_armed_walk_NE_45.0_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NE/warrior_armed_walk_NE_45.0_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NE/warrior_armed_walk_NE_45.0_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NE/warrior_armed_walk_NE_45.0_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NE/warrior_armed_walk_NE_45.0_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NE/warrior_armed_walk_NE_45.0_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NE/warrior_armed_walk_NE_45.0_7.png'),
        ],
        'NEE': [pygame.image.load('assets/sprites/player/warrior_armed_walk/NEE/warrior_armed_walk_NEE_22.5_0.png'),
                pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NEE/warrior_armed_walk_NEE_22.5_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NEE/warrior_armed_walk_NEE_22.5_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NEE/warrior_armed_walk_NEE_22.5_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NEE/warrior_armed_walk_NEE_22.5_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NEE/warrior_armed_walk_NEE_22.5_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NEE/warrior_armed_walk_NEE_22.5_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NEE/warrior_armed_walk_NEE_22.5_7.png'),
        ],
        'NNE': [pygame.image.load('assets/sprites/player/warrior_armed_walk/NNE/warrior_armed_walk_NNE_67.5_0.png'),
                pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNE/warrior_armed_walk_NNE_67.5_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNE/warrior_armed_walk_NNE_67.5_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNE/warrior_armed_walk_NNE_67.5_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNE/warrior_armed_walk_NNE_67.5_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNE/warrior_armed_walk_NNE_67.5_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNE/warrior_armed_walk_NNE_67.5_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNE/warrior_armed_walk_NNE_67.5_7.png'),
        ],
        'NNW': [pygame.image.load('assets/sprites/player/warrior_armed_walk/NNW/warrior_armed_walk_NNW_112.5_0.png'),
                pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNW/warrior_armed_walk_NNW_112.5_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNW/warrior_armed_walk_NNW_112.5_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNW/warrior_armed_walk_NNW_112.5_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNW/warrior_armed_walk_NNW_112.5_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNW/warrior_armed_walk_NNW_112.5_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNW/warrior_armed_walk_NNW_112.5_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NNW/warrior_armed_walk_NNW_112.5_7.png'),
        ],
        'NW': [pygame.image.load('assets/sprites/player/warrior_armed_walk/NW/warrior_armed_walk_NW_135.0_0.png'),
               pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NW/warrior_armed_walk_NW_135.0_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NW/warrior_armed_walk_NW_135.0_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NW/warrior_armed_walk_NW_135.0_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NW/warrior_armed_walk_NW_135.0_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NW/warrior_armed_walk_NW_135.0_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NW/warrior_armed_walk_NW_135.0_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NW/warrior_armed_walk_NW_135.0_7.png'),
        ],
        'NWW': [pygame.image.load('assets/sprites/player/warrior_armed_walk/NWW/warrior_armed_walk_NWW_157.5_0.png'),
                pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NWW/warrior_armed_walk_NWW_157.5_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NWW/warrior_armed_walk_NWW_157.5_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NWW/warrior_armed_walk_NWW_157.5_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NWW/warrior_armed_walk_NWW_157.5_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NWW/warrior_armed_walk_NWW_157.5_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NWW/warrior_armed_walk_NWW_157.5_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/NWW/warrior_armed_walk_NWW_157.5_7.png'),
        ],
        'S': [pygame.image.load('assets/sprites/player/warrior_armed_walk/S/warrior_armed_walk_S_270.0_0.png'),
              pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/S/warrior_armed_walk_S_270.0_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/S/warrior_armed_walk_S_270.0_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/S/warrior_armed_walk_S_270.0_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/S/warrior_armed_walk_S_270.0_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/S/warrior_armed_walk_S_270.0_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/S/warrior_armed_walk_S_270.0_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/S/warrior_armed_walk_S_270.0_7.png'),
        ],
        'SE': [pygame.image.load('assets/sprites/player/warrior_armed_walk/SE/warrior_armed_walk_SE_315.0_0.png'),
               pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SE/warrior_armed_walk_SE_315.0_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SE/warrior_armed_walk_SE_315.0_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SE/warrior_armed_walk_SE_315.0_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SE/warrior_armed_walk_SE_315.0_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SE/warrior_armed_walk_SE_315.0_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SE/warrior_armed_walk_SE_315.0_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SE/warrior_armed_walk_SE_315.0_7.png'),
        ],
        'SEE': [pygame.image.load('assets/sprites/player/warrior_armed_walk/SEE/warrior_armed_walk_SEE_337.5_0.png'),
                pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SEE/warrior_armed_walk_SEE_337.5_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SEE/warrior_armed_walk_SEE_337.5_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SEE/warrior_armed_walk_SEE_337.5_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SEE/warrior_armed_walk_SEE_337.5_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SEE/warrior_armed_walk_SEE_337.5_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SEE/warrior_armed_walk_SEE_337.5_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SEE/warrior_armed_walk_SEE_337.5_7.png'),
        ],
        'SSE': [pygame.image.load('assets/sprites/player/warrior_armed_walk/SSE/warrior_armed_walk_SSE_292.5_0.png'),
                pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSE/warrior_armed_walk_SSE_292.5_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSE/warrior_armed_walk_SSE_292.5_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSE/warrior_armed_walk_SSE_292.5_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSE/warrior_armed_walk_SSE_292.5_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSE/warrior_armed_walk_SSE_292.5_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSE/warrior_armed_walk_SSE_292.5_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSE/warrior_armed_walk_SSE_292.5_7.png'),
        ],
        'SSW': [pygame.image.load('assets/sprites/player/warrior_armed_walk/SSW/warrior_armed_walk_SSW_247.5_0.png'),
                pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSW/warrior_armed_walk_SSW_247.5_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSW/warrior_armed_walk_SSW_247.5_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSW/warrior_armed_walk_SSW_247.5_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSW/warrior_armed_walk_SSW_247.5_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSW/warrior_armed_walk_SSW_247.5_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSW/warrior_armed_walk_SSW_247.5_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SSW/warrior_armed_walk_SSW_247.5_7.png'),
        ],
        'SW': [pygame.image.load('assets/sprites/player/warrior_armed_walk/SW/warrior_armed_walk_SW_225.0_0.png'),
               pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SW/warrior_armed_walk_SW_225.0_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SW/warrior_armed_walk_SW_225.0_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SW/warrior_armed_walk_SW_225.0_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SW/warrior_armed_walk_SW_225.0_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SW/warrior_armed_walk_SW_225.0_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SW/warrior_armed_walk_SW_225.0_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SW/warrior_armed_walk_SW_225.0_7.png'),
        ],
        'SWW': [pygame.image.load('assets/sprites/player/warrior_armed_walk/SWW/warrior_armed_walk_SWW_202.5_0.png'),
                pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SWW/warrior_armed_walk_SWW_202.5_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SWW/warrior_armed_walk_SWW_202.5_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SWW/warrior_armed_walk_SWW_202.5_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SWW/warrior_armed_walk_SWW_202.5_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SWW/warrior_armed_walk_SWW_202.5_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SWW/warrior_armed_walk_SWW_202.5_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/SWW/warrior_armed_walk_SWW_202.5_7.png'),
        ],
        'W': [pygame.image.load('assets/sprites/player/warrior_armed_walk/W/warrior_armed_walk_W_180.0_0.png'),
              pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/W/warrior_armed_walk_W_180.0_1.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/W/warrior_armed_walk_W_180.0_2.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/W/warrior_armed_walk_W_180.0_3.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/W/warrior_armed_walk_W_180.0_4.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/W/warrior_armed_walk_W_180.0_5.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/W/warrior_armed_walk_W_180.0_6.png'),
            pygame.image.load(
            'assets/sprites/player/warrior_armed_walk/W/warrior_armed_walk_W_180.0_7.png'),
        ],
    }

    def __init__(self, x, y, health, game):
        super().__init__(x, y)
        self.health = health
        self.inventory = []
        self.vx = 0
        self.vy = 0
        self.game = game
        self.player_width, self.player_height = 0.5, 0.5

        self.current_sprite = Player.idle_sprites['SE']

    def update_sprite_direction(self, mouse_x, mouse_y, camera_x_offset, camera_y_offset):
        adjusted_mouse_x = mouse_x - camera_x_offset
        adjusted_mouse_y = mouse_y - camera_y_offset

        player_iso_x, player_iso_y = cart_to_iso(self.x, self.y)

        dx = adjusted_mouse_x - player_iso_x
        dy = adjusted_mouse_y - player_iso_y

        angle = -math.degrees(math.atan2(dy, dx))

        if angle < 0:
            angle += 360

        if 337.5 <= angle or angle < 22.5:
            self.current_sprite = self.idle_sprites['E']
        elif 22.5 <= angle < 45:
            self.current_sprite = self.idle_sprites['NEE']
        elif 45 <= angle < 67.5:
            self.current_sprite = self.idle_sprites['NE']
        elif 67.5 <= angle < 90:
            self.current_sprite = self.idle_sprites['NNE']
        elif 90 <= angle < 112.5:
            self.current_sprite = self.idle_sprites['N']
        elif 112.5 <= angle < 135:
            self.current_sprite = self.idle_sprites['NNW']
        elif 135 <= angle < 157.5:
            self.current_sprite = self.idle_sprites['NW']
        elif 157.5 <= angle < 180:
            self.current_sprite = self.idle_sprites['NWW']
        elif 180 <= angle < 202.5:
            self.current_sprite = self.idle_sprites['W']
        elif 202.5 <= angle < 225:
            self.current_sprite = self.idle_sprites['SWW']
        elif 225 <= angle < 247.5:
            self.current_sprite = self.idle_sprites['SW']
        elif 247.5 <= angle < 270:
            self.current_sprite = self.idle_sprites['SSW']
        elif 270 <= angle < 292.5:
            self.current_sprite = self.idle_sprites['S']
        elif 292.5 <= angle < 315:
            self.current_sprite = self.idle_sprites['SSE']

    def draw(self, SCREEN, camera_x_offset, camera_y_offset):
        sprite_x, sprite_y = cart_to_iso(self.x, self.y)
        sprite_x -= self.current_sprite.get_width() // 2
        sprite_y -= self.current_sprite.get_height() // 2
        SCREEN.blit(self.current_sprite, (sprite_x +
                    camera_x_offset, sprite_y + camera_y_offset))

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

    def handle_movement(self, map_data):
        keys = pygame.key.get_pressed()
        vx = (-self.PLAYER_SPEED if keys[pygame.K_a] else 0) + \
            (self.PLAYER_SPEED if keys[pygame.K_d] else 0)
        vy = (-self.PLAYER_SPEED if keys[pygame.K_w] else 0) + \
            (self.PLAYER_SPEED if keys[pygame.K_s] else 0)

        if vx or vy:
            if vx != 0 and vy != 0:
                vx *= 0.7071
                vy *= 0.7071
            next_x, next_y = self.x + vx * self.game.dt, self.y + vy * self.game.dt
            if self.can_move(next_x, next_y, map_data):
                self.set_velocity(vx, vy)

    def can_move(self, next_x, next_y, map_data):
        return (
            self.detect_collision(map_data, next_x, next_y) and
            self.detect_collision(map_data, next_x + self.player_width, next_y) and
            self.detect_collision(map_data, next_x, next_y + self.player_height) and
            self.detect_collision(
                map_data, next_x + self.player_width, next_y + self.player_height)
        )

    def detect_collision(self, map_data, x, y):
        map_x, map_y = int(x), int(y)
        if 0 <= map_x < len(map_data[0]) and 0 <= map_y < len(map_data):
            return map_data[map_y][map_x] not in ['1', 'X']
        return False


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
