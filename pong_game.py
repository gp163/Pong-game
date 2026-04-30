import pygame
import random

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 90))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self, keys, is_left):
        if is_left:
            if keys[pygame.K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_s] and self.rect.y < SCREEN_HEIGHT - self.rect.height:
                self.rect.y += self.speed
        else:
            if keys[pygame.K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN] and self.rect.y < SCREEN_HEIGHT - self.rect.height:
                self.rect.y += self.speed

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x = 5 * random.choice([-1, 1])
        self.speed_y = 5 * random.choice([-1, 1])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top/bottom
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1

        # Reset if out of bounds
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.speed_x = 5 * random.choice([-1, 1])
            self.speed_y = 5 * random.choice([-1, 1])

# Initialize Pygame only when run as main
if __name__ == "__main__":
    pygame.init()

    # Create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong Game")

    # Clock for FPS
    clock = pygame.time.Clock()
    FPS = 60

    # Sprite groups
    all_sprites = pygame.sprite.Group()
    paddles = pygame.sprite.Group()

    # Create paddles
    left_paddle = Paddle(10, SCREEN_HEIGHT // 2 - 45)
    right_paddle = Paddle(SCREEN_WIDTH - 25, SCREEN_HEIGHT // 2 - 45)
    paddles.add(left_paddle)
    paddles.add(right_paddle)
    all_sprites.add(left_paddle, right_paddle)

    # Create ball
    ball = Ball()
    all_sprites.add(ball)

    # Game loop
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Update
        left_paddle.update(keys, True)
        right_paddle.update(keys, False)
        ball.update()

        # Collision with paddles
        if pygame.sprite.spritecollide(ball, paddles, False):
            ball.speed_x *= -1

        # Draw
        screen.fill(BLACK)
        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()
