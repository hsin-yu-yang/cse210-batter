from game import constants
from game.action import Action
from game.point import Point
from game.audio_service import AudioService
from game.actor import (Actor)

class HandleOffScreenAction():
    def __init__(self) -> None:
        super().__init__()
    def execute(self, cast):
        audio_service = AudioService()
        end = Actor()
        ball = cast["balls"][0]
        x_pos = ball._position.get_x()
        y_pos = ball._position.get_y()
        end_info = []
        if x_pos >= 775:
            new_vel = Point(-1 * ball._velocity._x, ball._velocity._y)
            ball.set_velocity(new_vel)
        elif x_pos <= 5:
            new_vel = Point(-1 * ball._velocity._x, ball._velocity._y)
            ball.set_velocity(new_vel)
        elif y_pos <= 5:
            new_vel = Point(ball._velocity._x, ball._velocity._y * -1)
            ball.set_velocity(new_vel)
        elif y_pos >= 575:
            pass
        paddle = cast["paddle"][0]
        right_wall = (constants.MAX_X - constants.PADDLE_WIDTH)
        x_pos = paddle._position.get_x()
        if x_pos >= (right_wall):
            new_vel = Point(right_wall, paddle._position._y)
            paddle.set_position(new_vel)
        elif x_pos <= 0:
            new_vel = Point(0, paddle._position._y)
            paddle.set_position(new_vel)