import pygame
import sys
import os
from settings import *


def handle_quit():
    pygame.quit()
    sys.exit()


def get_font(size, font='assets/font.ttf'):
    base_path = os.path.dirname(os.path.dirname(__file__))
    font_path = os.path.join(base_path, font)

    return pygame.font.Font(font_path, size)


def cart_to_iso(x, y):
    iso_x = (x - y) * TILE_WIDTH // 2
    iso_y = (x + y) * TILE_HEIGHT // 2
    return iso_x, iso_y


def draw_tile(SCREEN, x, y, color, x_offset, y_offset):
    iso_x, iso_y = cart_to_iso(x, y)
    points = [
        (iso_x + x_offset, iso_y + y_offset),
        (iso_x + TILE_WIDTH // 2 + x_offset, iso_y + TILE_HEIGHT // 2 + y_offset),
        (iso_x + x_offset, iso_y + TILE_HEIGHT + y_offset),
        (iso_x - TILE_WIDTH // 2 + x_offset, iso_y + TILE_HEIGHT // 2 + y_offset)
    ]
    pygame.draw.polygon(SCREEN, color, points)
