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
import os

# TODO: Add imports similar to the following when you create these classes
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

def main():

    cast = {}
    cast["bricks"] = []
  
    x = [20, 80, 140, 200, 260, 320, 380, 440, 500, 560, 620, 680, 740]
    y = [10, 50, 90, 130, 170, 210]

    #x = [300]
    #y = [400]

    bricks = []
    colors = ['assets/brick-0.png',
                'assets/brick-1.png',
                'assets/brick-2.png',
                'assets/brick-3.png',
                'assets/brick-4.png',
                'assets/brick-5.png']
    for i in range(len(y)):
        color = colors[i]
        for j in range(len(x)):
            brick = Brick()
            brick.set_image(os.path.join(os.getcwd(), color))
            brick.set_height(constants.BRICK_HEIGHT)
            brick.set_width(constants.BRICK_WIDTH)
            position = Point(x[j],y[i])
            brick.set_position(position)
            
            bricks.append(brick)

    cast["bricks"]= bricks

    cast["balls"] = []
    ball = Ball()
    info = []
    ball.set_image(constants.IMAGE_BALL)
    ball.set_height(constants.BALL_HEIGHT)
    ball.set_width(constants.BALL_WIDTH)
    b_pos = Point(constants.BALL_X, constants.BALL_Y)
    ball.set_position(b_pos)
    pos_vel = Point(constants.BALL_DX, constants.BALL_DY)
    ball.set_velocity(pos_vel)
    info.append(ball)

    cast["balls"] = info
  
 
    cast["paddle"] = []
    paddle = Paddle()
    p_info = []
    paddle.set_image(constants.IMAGE_PADDLE)
    paddle.set_height(constants.PADDLE_HEIGHT)
    paddle.set_width(constants.PADDLE_WIDTH)
    paddle_pos = Point(350,550)
    paddle.set_position(paddle_pos)
    p_info.append(paddle)


    cast["paddle"] = p_info

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction()
    physics_service = PhysicsService()
    audio_service = AudioService()
    # end_game = End_Game()
    # keep_playing = Keep_Playing()

    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]


    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
