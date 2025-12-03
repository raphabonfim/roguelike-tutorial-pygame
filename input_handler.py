import pygame.event

from actions import Action, EscapeAction, MovementAction


class EventHandler:
    def handle_events(self):
        # handle QUIT clicking on X, ctrl+q, ctrl+w
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                return EscapeAction()

            # handle MOVEMENT
            if event.type == pygame.KEYDOWN:
                dx, dy = 0, 0

                if event.key == pygame.K_UP:
                    dy = -1
                elif event.key == pygame.K_DOWN:
                    dy = 1
                elif event.key == pygame.K_LEFT:
                    dx = -1
                elif event.key == pygame.K_RIGHT:
                    dx = 1

                # if any movement key was pressed, return action
                if dx != 0 or dy != 0:
                    return MovementAction(dx, dy)
