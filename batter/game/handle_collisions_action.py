from game.action import Action
from game import ball
from game.audio_service import AudioService
from game import constants
from game.point import Point

class HandleCollisionsAction(Action):
    """handles the interaction of actors on screen. The responsibility of 
    this class of objects is to check how actors have collided and then update the
    actors as necessary.
    
    Stereotype:
        Controller
    Attributes:
        _pysics_service (class): The class which handles physics in game. 
    """
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service


    def execute(self, cast):
        '''
        This method receives the cast from main and then checks through the actors within cast for collisions.
        If the ball and a brick collide then the brick is removed from play. 
        If the ball and the paddle collide then the ball bounces. 
        attributes:
            cast: a dictionary storing all the actors in play. {key: name, value: object}
        '''
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]
        balls = cast["balls"]
        
        # the bricks and balls are iterated through for collisions.
        # physics service is called to check for collisions, and then which axis the collision occured on
        # is checked. 
        for ball in balls:
            if self._physics_service.is_collision(ball, paddle):
                self.check_collision(ball, paddle)
            for brick in bricks:
                if self._physics_service.is_collision(ball, brick):
                    self.check_collision(ball, brick)
                    bricks.remove(brick)
                
                    #possible bug fix, take ball y position and add hald paddle plus ball height to y position to fix collision
            

    def check_collision(self, obj_1, obj_2):
        '''
        This method checks for which axis a collision occured on, a sound bite is played, and the bounce method is called.
        attributes:
            obj_1: an actor from cast
            obj_2: another actor from cast
        '''
        
        if self.check_vertical_collison(obj_1, obj_2) or self.check_horizontal_collison(obj_1, obj_2):
            if self.check_vertical_collison(obj_1, obj_2):
                self.play_audio_bounce()
                obj_1.bounce_vertical()
            elif self.check_horizontal_collison(obj_1, obj_2):
                self.play_audio_bounce()
                obj_1.bounce_horizontal()
        elif self.check_vertical_collison(obj_1, obj_2) and self.check_horizontal_collison(obj_1, obj_2):
            self.play_audio_bounce()
            obj_1.bounce_vertical()
            obj_1.bounce_horizontal()


    def check_vertical_collison(self, ball, game_object):
        '''
        This method checks for a collision on the y-axis, a bool is returned if true, and the ball's position is moved slightly.
        attributes:
            ball: an actor from cast
            game_object: another actor from cast
        '''
        position = ball.get_position()
        x = position.get_x()
        y = position.get_y()

        if ball.get_bottom_edge() >= game_object.get_top_edge():
            ball.set_position(Point(x, (y - 5)))
            return True

        elif ball.get_top_edge() <= game_object.get_bottom_edge():
            ball.set_position(Point(x, (y + 5)))
            return True

        else:
            return False

    def check_horizontal_collison(self, ball, game_object):
        '''
        This method checks for a collision on the x-axis, a bool is returned if true.
        attributes:
            ball: an actor from cast
            game_object: another actor from cast
        '''
        
        if ball.get_left_edge() <= game_object.get_right_edge():
            
            return True

        elif ball.get_right_edge() >= game_object.get_left_edge():
            
            return True

        else:
            return False

    def play_audio_bounce(self):
        '''
        handles opening audio service and then playing a sound effect.
        '''
        audio_service = AudioService()
        audio_service.play_sound(constants.SOUND_BOUNCE)
