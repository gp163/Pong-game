import pytest
import pygame
from pong_game import Paddle, Ball, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE

@pytest.fixture
def init_pygame():
    pygame.init()
    yield
    pygame.quit()

def test_paddle_initialization(init_pygame):
    paddle = Paddle(10, 100)
    assert paddle.rect.x == 10
    assert paddle.rect.y == 100
    assert paddle.speed == 5

def test_ball_initialization(init_pygame):
    ball = Ball()
    assert ball.rect.center == (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    assert ball.speed_x in [-5, 5]
    assert ball.speed_y in [-5, 5]

def test_paddle_movement_up(init_pygame):
    paddle = Paddle(10, 100)
    keys = {pygame.K_w: True, pygame.K_s: False}
    paddle.update(keys, True)
    assert paddle.rect.y == 95  # Moved up by speed

def test_paddle_movement_down(init_pygame):
    paddle = Paddle(10, 100)
    keys = {pygame.K_w: False, pygame.K_s: True}
    paddle.update(keys, True)
    assert paddle.rect.y == 105  # Moved down by speed

def test_ball_update(init_pygame):
    ball = Ball()
    initial_x = ball.rect.x
    initial_y = ball.rect.y
    ball.update()
    assert ball.rect.x != initial_x or ball.rect.y != initial_y  # Ball moved