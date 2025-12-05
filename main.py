import pygame, sys

from input_handler import EventHandler
from actions import EscapeAction, MovementAction
from entity import Entity
from engine import Engine

# game_constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
FPS = 30
TILEMAP = pygame.image.load("assets/dejavu10x10_gs_tc.png")  # .convert_alpha()

# glyphs and sprites
sprite_dict = {"player": pygame.Rect(1, 10, 10, 10), "npc": pygame.Rect(1, 30, 10, 10)}


# game loop
def main():
    # initialization: pygame, game screen, game title
    pygame.init()
    # enable repeating key presses - 500ms delay, 50ms interval
    pygame.key.set_repeat(500, 50)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Yet Another Roguelike Tutorial (Now in pygame!)")
    clock = pygame.time.Clock()

    # player instantiate
    player = Entity(
        int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), sprite_dict["player"], None
    )
    npc = Entity(
        int(SCREEN_WIDTH / 2 - 10), int(SCREEN_HEIGHT / 2), sprite_dict["npc"], None
    )

    entities = {npc, player}
    event_handler = EventHandler()
    engine = Engine(entities, event_handler, player)

    running = True
    while running:

        # 1. event handling & player input
        engine.handle_events()

        # 2. update world & draw
        engine.render(screen, TILEMAP)
        clock.tick(FPS)


# this means that we will only run main() if we explicitly run the script (e.g. via python main.py)
if __name__ == "__main__":
    main()
