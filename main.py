import pygame, sys
from input_handler import EventHandler
from actions import EscapeAction, MovementAction

# game_constants

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
TILE_SIZE = 10
FPS = 30
TILEMAP = pygame.image.load("assets/dejavu10x10_gs_tc.png")  # .convert_alpha()

# glyphs
PLAYER_GLYPH = pygame.Rect(1, 10, 10, 10)  # position of the glyph in the tilemap

# helpers
handler = EventHandler()


# game loop
def main():
    # initialization: pygame, game screen, game title
    pygame.init()
    pygame.key.set_repeat(
        500, 50
    )  # enable repeating key presses - 500ms delay, 50ms interval
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Yet Another Roguelike Tutorial (Now in pygame!)")
    clock = pygame.time.Clock()
    player_x, player_y = int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)

    direction = "right"
    running = True
    while running:

        # 1. event handling
        action = handler.handle_events()

        # 2. player input
        if action:
            if isinstance(action, EscapeAction):
                running = False
            elif isinstance(action, MovementAction):
                player_x += action.dx * TILE_SIZE
                player_y += action.dy * TILE_SIZE

        # 3. update world
        # 4. draw
        screen.fill((0, 0, 0))
        screen.blit(TILEMAP, (player_x, player_y), PLAYER_GLYPH)
        pygame.display.flip()
        # pygame.display.update()  # update specific regions
        clock.tick(FPS)


# this means that we will only run main() if we explicitly run the script (e.g. via python main.py)
if __name__ == "__main__":
    main()
