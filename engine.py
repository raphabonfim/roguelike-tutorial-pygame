import pygame
from actions import EscapeAction, MovementAction
from entity import Entity
from input_handler import EventHandler


class Engine:
    def __init__(
        self, entities: set[Entity], event_handler: EventHandler, player: Entity
    ):
        self.entities = entities
        self.event_handler = event_handler
        self.player = player

    def handle_events(self):
        for event in pygame.event.get():

            action = self.event_handler()

            if action is None:
                continue

            if isinstance(action, MovementAction):
                self.player.move(action.dx, action.dy)

            elif isinstance(action, EscapeAction):
                raise SystemExit()

    def render(self, surface):
        self.surface = surface
        for entity in self.entities:
            surface.blit(entity.x, entity.y, entity.char, entity.color)
            pygame.display.flip()
            surface.fill(0, 0, 0)
