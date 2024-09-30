import pygame

from components.button import Button
from helpers.helpers import handle_quit, cart_to_iso, draw_tile
from classes.map import Map
from settings import *


def play(SCREEN, player):
    map_data = Map.map_data
    map_width = len(map_data[0])
    map_height = len(map_data)

    screen_center_x = WIDTH // 2
    screen_center_y = HEIGHT // 2

    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(60) / 1000
        player.game.dt = dt

        SCREEN.fill((128, 128, 128))

        player_iso_x, player_iso_y = cart_to_iso(player.x, player.y)
        camera_x_offset = screen_center_x - player_iso_x
        camera_y_offset = screen_center_y - player_iso_y

        for y, row in enumerate(map_data):
            for x, symbol in enumerate(row):
                color = COLORS.get(symbol, (255, 255, 255))
                draw_tile(SCREEN, x, y, color,
                          camera_x_offset, camera_y_offset)

        player.draw(SCREEN, camera_x_offset, camera_y_offset)

        player.handle_movement(map_width, map_height, map_data)
        player.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                handle_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "MENU"

        pygame.display.update()
        clock.tick(60)
