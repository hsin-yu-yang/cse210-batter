from game import constants
from game.action import Action
from game.audio_service import AudioService

class HandleOffScreenAction(Action):
    """Code template for the rules that govern the interaction of the ball and the game window.
    
    Stereotype:
        Controller
    Attributes:
        none
    """
    def __init__(self):
        super().__init__()
    

    def execute(self, cast):
        '''
        exectues the functionality of the class, handles calls to check border collisions. 
        attributes:
            cast, the collection of all actors in play.
        
        '''
        ball = cast["balls"][0]

        # logic statements to determine if the ball has bounced off a surface.
        if self.check_bounce_horizontal(ball) == True:
            ball.bounce_horizontal()
        if self.check_bounce_vertical(ball) == True:
            ball.bounce_vertical()
        elif self.check_bounce_vertical(ball) == False:
            ball.bounce_vertical()
            cast["balls"].remove(ball)


    def check_bounce_horizontal(self, ball):
        '''
        checks for an interaction between the balls horizontal edges and the horizontal edges of the game window.
        attributes:
            ball, an instance of a ball actor
        '''
        if ball.get_left_edge() <= 0 or ball.get_right_edge() >= constants.MAX_X:
            audio_service = AudioService()
            audio_service.play_sound(constants.SOUND_BOUNCE)
            return True
            
        

    def check_bounce_vertical(self, ball):
        '''
        handles checking for an interaction between the ball and the game window on the vertical axis.
        attributes:
            ball, an instance of a ball actor
        '''
        audio_service = AudioService()
        if ball.get_top_edge() <= 0:
            audio_service.play_sound(constants.SOUND_BOUNCE)
            return True
        elif ball.get_bottom_edge() >= constants.MAX_Y:
            audio_service.play_sound(constants.SOUND_BOUNCE)
            return False