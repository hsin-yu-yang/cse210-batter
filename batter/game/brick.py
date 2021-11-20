from game.actor import Actor
from game.point import Point
from game import constants

class Brick(Actor):
    """A code template for the brick actor. The responsibility of 
    this class of objects is to create an actor that is specifically a brick.
    
    Stereotype:
        actor
    """
    def __init__(self):
        super().__init__()
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self.set_width(constants.BRICK_WIDTH)
        self.set_height(constants.BRICK_HEIGHT)
        self.set_image(constants.IMAGE_BRICK)
    
    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Args:
            self (Actor): an instance of Actor.
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position

    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            self (Actor): An instance of Actor.
            position (Point): The given position.
        """
        self._position = position

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Args:
            self (Actor): an instance of Actor.
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            self (Actor): An instance of Actor.
            position (Point): The given velocity.
        """
        self._velocity = velocity
    
    def has_text(self):
        return self._text != ""

    def has_image(self):
        return self._image != ""
    