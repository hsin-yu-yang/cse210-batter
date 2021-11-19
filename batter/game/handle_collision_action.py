import sys
import random
from game import actor, constants 
from game.point import Point
from game.move_actors_action import MoveActorsAction


from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    


    def execute(self, cast):
        """Executes the action using the given actors.
        - Bounces off bat
        - Bounces off walls
        - Bounces off (and removes) bricks
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle = cast["paddle"] # there's only one
        ball = cast["ball"][0] # there's only one

        # Check surroundings

        # - Border
        # - - Top
        if ball.get_position().get_y() == 1:
            ball.set_y_velocity(1)
        # - - Bottom
        elif ball.get_position().get_y() == 19:
            ball.set_y_velocity(-1)
            sys.exit()
        # - - Left
        if ball.get_position().get_x() == 1:
            ball.set_x_velocity(1)
        # - - Right
        elif ball.get_position().get_x() == 79:
            ball.set_x_velocity(-1)
        
        # - Objects
        # - - Bricks
        removed = False
        for brick in cast['brick']:
            point = brick.get_position()
            # Check direction
            # - Center
            if point.add(Point(0, 0)).equals(ball.get_position()):
                ball.reverse_velocity()
                cast['brick'].remove(brick)
                
                removed = True
                return
        if not removed:
            for brick in cast['brick']:
                point = brick.get_position()
                # - Up
                if ball.get_velocity().get_y() == -1:
                    if point.add(Point(0, 1)).equals(ball.get_position()):
                        if not removed:
                            cast['brick'].remove(brick)
                            
                            removed = True
                        ball.set_y_velocity(1)
                # - Down
                else:
                    if point.add(Point(0, -1)).equals(ball.get_position()):
                        if not removed:
                            cast['brick'].remove(brick)
                            
                            removed = True
                        ball.set_y_velocity(-1)
                # - Left
                if ball.get_velocity().get_x() == -1:
                    if point.add(Point(1, 0)).equals(ball.get_position()):
                        if not removed:
                            cast['brick'].remove(brick)
                            
                            removed = True
                        ball.set_x_velocity(1)
                # - Right
                else:
                    if point.add(Point(-1, 0)).equals(ball.get_position()):
                        if not removed:
                            cast['brick'].remove(brick)
                            
                            removed = True
                        ball.set_x_velocity(-1)
        # - - Paddle
        for paddle in cast["paddle"]:
            point = paddle.get_position()
            # Check direction
            # - Down
            if ball.get_velocity().get_y() == 1:
                if point.add(Point(0, -1)).equals(ball.get_position()):
                    ball.set_y_velocity(-1)
            # - Left
            if ball.get_velocity().get_x() == -1:
                if point.add(Point(1, 0)).equals(ball.get_position()):
                    ball.set_x_velocity(1)
            # - Right
            else:
                if point.add(Point(-1, 0)).equals(ball.get_position()):
                    ball.set_x_velocity(-1)
                 