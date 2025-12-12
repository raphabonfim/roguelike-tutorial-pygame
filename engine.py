import pygame
from constants import *

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handler import EventHandler


class Engine:
    def __init__(self, entities, event_handler: EventHandler, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.player = player

    def handle_events(self):
        action = self.event_handler.handle_events()

        if action is None:
            return

        if isinstance(action, MovementAction):
            self.player.move(action.dx * TILE_SIZE, action.dy * TILE_SIZE)

        if isinstance(action, EscapeAction):
            pygame.quit()
            raise SystemExit

    def render(self, surface, tilemap):
        surface.fill((0, 0, 0))

        for entity in self.entities:
            surface.blit(tilemap, (entity.x, entity.y), entity.sprite)

        pygame.display.flip()
