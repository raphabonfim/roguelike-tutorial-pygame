import pygame, sys
from input_handler import EventHandler
from actions import EscapeAction, MovementAction
from entity import Entity

# game_constants

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
TILE_SIZE = 10
FPS = 30
TILEMAP = pygame.image.load("assets/dejavu10x10_gs_tc.png")  # .convert_alpha()

# glyphs
PLAYER_GLYPH = pygame.Rect(1, 10, 10, 10)  # position of the glyph in the tilemap
NPC_GLYPH = pygame.Rect(1, 30, 10, 10)  # position of the NPC
# helpers
handler = EventHandler()


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
    player = Entity(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), "@", (255, 255, 255))
    npc = Entity(int(SCREEN_WIDTH / 2 - 10), int(SCREEN_HEIGHT / 2), "@", (255, 255, 0))
    entities = {npc, player}

    running = True
    while running:

        # 1. event handling
        action = handler.handle_events()

        # 2. player input
        if action:
            if isinstance(action, EscapeAction):
                running = False
            elif isinstance(action, MovementAction):
                player.move((action.dx * TILE_SIZE), (action.dy * TILE_SIZE))

        # 3. update world
        # 4. draw
        screen.fill((0, 0, 0))
        screen.blit(TILEMAP, (player.x, player.y), PLAYER_GLYPH)
        screen.blit(
            TILEMAP,
            (
                npc.x,
                npc.y,
            ),
            NPC_GLYPH,
        )
        pygame.display.flip()
        # pygame.display.update()  # update specific regions
        clock.tick(FPS)


# this means that we will only run main() if we explicitly run the script (e.g. via python main.py)
if __name__ == "__main__":
    main()
