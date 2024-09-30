import pygame
from screens.menu import menu
from screens.play import play
from screens.options import options
from settings import *

pygame.init()


class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Balthazar's Temple")
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.player = None
        self.states = {
            "MENU": self.menu,
            "PLAY": self.play,
            "OPTIONS": self.options,
        }
        self.current_state = "MENU"

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.states[self.current_state]()

    def menu(self):
        self.player = menu(self.screen, self)
        if self.player:
            self.current_state = "PLAY"

    def play(self):
        self.current_state = play(self.screen, self.player)

    def options(self):
        self.current_state = options(self.screen)


if __name__ == "__main__":
    game = GameController()
    game.run()
