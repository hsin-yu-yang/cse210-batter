
   
from game.action import Action
from game import constants

class ControlActorsAction(Action):
    """Handles controlling the speed of the paddle. The responsibility of 
    this class of objects is to control the direction and speed of the paddle.
    
    Stereotype:
        Controller
    Attributes:
        input_service: a class which handles the inputs from the user and converts it to data for the program.
    """
    def __init__(self, input_service):
        '''
        receives input service and converts it into a variable useable to the class.
        '''
        self._input_service = input_service

    def execute(self, cast):
        '''
        handles updating the paddle from the cast with its velocity and input from the user.
        attributes:
            cast: a dictionary which stores all actors in play. 
        '''
        direction = self._input_service.get_direction()
        paddle = cast["paddle"][0]
        paddle.set_velocity(direction.scale(constants.PADDLE_SPEED))

    