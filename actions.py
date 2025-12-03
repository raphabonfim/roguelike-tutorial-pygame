class Action:
    pass


class EscapeAction(Action):
    pass


"""We do not need any data here. 
The class EscapeAction acts like a signal 
(think Godot signals. It just have to exist 
to bridge the KEYDOWN in input_handler.py 
and the pygame.QUIT in main.py)"""


class MovementAction(Action):
    def __init__(self, dx, dy):
        super().__init__()

        self.dx = dx
        self.dy = dy
