from game.actor import Actor
from game.point import Point
from game import constants

class Ball(Actor):
    """A code template for the ball actor. The responsibility of 
    this class of objects is to create an actor that is specifically a ball.
    
    Stereotype:
        actor
    """
    def __init__(self):
        '''
        initializes the class and assigns attributes to the actor.
        '''
        super().__init__()
        self.set_velocity(Point(constants.BALL_DX, constants.BALL_DY))
        self.set_width(constants.BALL_WIDTH)
        self.set_height(constants.BALL_HEIGHT)
        self.set_image(constants.IMAGE_BALL)

    def bounce_horizontal(self):
        '''
        Handles the logic which makes the ball bounce on the X-axis.
        '''
        velocity = self.get_velocity()
        dx = velocity.get_x()
        dy = velocity.get_y()
        return self.set_velocity(Point(-dx, dy))

    def bounce_vertical(self):
        '''
        handles the logic which makes the ball bounce on the Y-axis.
        '''
        velocity = self.get_velocity()
        dx = velocity.get_x()
        dy = velocity.get_y()
        return self.set_velocity(Point(dx, -dy))