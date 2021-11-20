from game.actor import Actor
from game import constants
from game.point import Point

class Paddle(Actor):
    """A code template for the paddle actor. The responsibility of 
    this class of objects is to create an actor that is specifically a paddle.
    
    Stereotype:
        actor
    """
    def __init__(self):
        super().__init__()
        # self.set_position(Point(400, 555))
        self.set_velocity(Point(0, 0))
        self.set_width(constants.PADDLE_WIDTH)
        self.set_height(constants.PADDLE_HEIGHT)
        self.set_image(constants.IMAGE_PADDLE)