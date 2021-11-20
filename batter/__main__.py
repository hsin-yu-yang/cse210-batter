import random

from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}
    
    bricks = []
    for x in range(14):
        for y in range(7):
            brick = Brick()
            brick.set_position(Point(x * 58, y * 28))
            #brick.set_image(constants.IMAGE_BRICK)
            bricks.append(brick)
            
    cast["bricks"] = bricks
    # TODO: Create bricks here and add them to the list

    game_balls = []
    ball = Ball()
    ball_x = int(constants.BALL_X)
    ball_y = int(constants.BALL_Y)
    ball.set_position(Point(ball_x, ball_y))
    game_balls.append(ball)
    cast["balls"] = game_balls
    # TODO: Create a ball here and add it to the list

    game_paddles = []
    paddle = Paddle()
    paddle_x = int(constants.PADDLE_X)
    paddle_y = int(constants.PADDLE_Y)
    paddle.set_position(Point(paddle_x, paddle_y))
    game_paddles.append(paddle)
    cast["paddle"] = game_paddles
    # TODO: Create a paddle here and add it to the list


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]


    # Start the game
    output_service.open_window("Batter");
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()