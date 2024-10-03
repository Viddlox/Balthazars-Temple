import pygame

from helpers.helpers import handle_quit, cart_to_iso, draw_tile
from classes.map import Map
from settings import *


def play(SCREEN, player):
    map_data = Map.map_data

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

        mouse_coords = pygame.mouse.get_pos()
        player.update_sprite_direction(mouse_coords[0], mouse_coords[1], camera_x_offset, camera_y_offset)

        visible_tiles_x = (WIDTH // TILE_WIDTH) + 4
        visible_tiles_y = (HEIGHT // TILE_HEIGHT) + 4

        player_map_x, player_map_y = int(player.x), int(player.y)
        for y in range(player_map_y - visible_tiles_y // 2, player_map_y + visible_tiles_y // 2):
            for x in range(player_map_x - visible_tiles_x // 2, player_map_x + visible_tiles_x // 2):
                if 0 <= y < len(map_data) and 0 <= x < len(map_data[0]):
                    symbol = map_data[y][x]
                    color = COLORS.get(symbol, (255, 255, 255))
                    draw_tile(SCREEN, x, y, color,
                            camera_x_offset, camera_y_offset)

        player.draw(SCREEN, camera_x_offset, camera_y_offset)

        player.handle_movement(map_data)
        player.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                handle_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "MENU"

        pygame.display.update()
        clock.tick(60)
