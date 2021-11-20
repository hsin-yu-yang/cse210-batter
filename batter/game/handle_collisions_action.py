import random
from game import constants
from game.action import Action
from game.physics_service import PhysicsService
from game.point import Point
from game.actor import Actor
from game.audio_service import AudioService

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def execute(self, cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        audio_service = AudioService()
        ball = cast["balls"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["bricks"]
        value = PhysicsService()
        experiment = value.is_collision(ball, paddle)
        if experiment == True:
            new_vel = Point(ball._velocity._x, -1 * ball._velocity._y)
            ball.set_velocity(new_vel)
            audio_service.play_sound(constants.SOUND_BOUNCE)
        value_2 = PhysicsService()
        for brick in bricks:
            touch = value_2.is_collision(ball, brick)
            if touch == True:
                new_vel = Point(ball._velocity._x, -1 * ball._velocity._y)
                ball.set_velocity(new_vel)
                audio_service.play_sound(constants.SOUND_BOUNCE)
                bricks.remove(brick)
