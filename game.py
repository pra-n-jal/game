
# blehhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
import pygame
from sys import exit
import random

# Game dimensions
GAME_WIDTH = 1200
GAME_HEIGHT = 750

# Bird properties
bird_x = GAME_WIDTH / 8
bird_y = GAME_HEIGHT / 2
bird_width = 80
bird_height = 60

# Pipe properties
pipe_x = GAME_WIDTH
pipe_y = 0
pipe_width = 64
pipe_height = 510
 
#Obstacles and Bullets
obstacles = []
bullets = []

obstacle_x = GAME_WIDTH
obstacle_width = 30
obstacle_height = 30

bullet_speed = 12


class Bird(pygame.Rect):
    def __init__(self, img):
        super().__init__(bird_x, bird_y, bird_width, bird_height)
        self.img = img


class Pipe(pygame.Rect):
    def __init__(self, img):
        super().__init__(pipe_x, pipe_y, pipe_width, pipe_height)
        self.img = img
        self.passed = False


# Game images
background_image = pygame.image.load("assets/background.jpg")
bird_image = pygame.image.load("assets/bird.png")
obstacle_image = pygame.image.load("assets/obstacle.png")
bullets_image = pygame.image.load("assets/bullets.png")

bird_image = pygame.transform.scale(
    bird_image, (bird_width, bird_height)
)

obstacle_image = pygame.transform.scale(
    obstacle_image, (obstacle_width, obstacle_height)
)

bullets_image = pygame.transform.scale(
    bullets_image, (20, 10)
)

top_pipe_image = pygame.image.load("assets/toppipe.png")
top_pipe_image = pygame.transform.scale(
    top_pipe_image, (pipe_width, pipe_height)
)

bottom_pipe_image = pygame.image.load("assets/bottompipe.png")
bottom_pipe_image = pygame.transform.scale(
    bottom_pipe_image, (pipe_width, pipe_height)
)

# Game logic
bird = Bird(bird_image)
pipes = []

velocity_x = -2
velocity_y = 0
gravity = 0.4

score = 0
game_over = False


def draw():
    window.blit(background_image, (0, 0))
    window.blit(bird.img, bird)

    for obstacle in obstacles:
        window.blit(obstacle_image, obstacle["rect"])

    for bullet in bullets:
        window.blit(bullets_image, bullet)

    for pipe in pipes:
        window.blit(pipe.img, pipe)

    text_str = str(int(score))

    if game_over:
        text_str = "Game Over: " + text_str

    text_font = pygame.font.SysFont("Comic Sans MS", 45)
    text_render = text_font.render(text_str, True, "white")
    window.blit(text_render, (5, 0))


def move():
    global velocity_y, score, game_over

    velocity_y += gravity
    bird.y += velocity_y

    # Prevent bird from leaving the top of the screen
    bird.y = max(bird.y, 0)

    if bird.y > GAME_HEIGHT:
        game_over = True
        return

    # Move bullets
    for bullet in bullets[:]:
        bullet.x += bullet_speed

        if bullet.x > GAME_WIDTH:
            bullets.remove(bullet)

    # Move obstacles
    for obstacle in obstacles:
        obstacle["rect"].x += velocity_x

    # Remove obstacles that have moved off-screen
    for obstacle in obstacles[:]:
        if obstacle["rect"].right < 0:
            obstacles.remove(obstacle)

    # Bullet collision with obstacles
    for bullet in bullets[:]:
        for obstacle in obstacles[:]:

            if bullet.colliderect(obstacle["rect"]):

                obstacle["health"] -= 1
                bullets.remove(bullet)

                if obstacle["health"] <= 0:
                    obstacles.remove(obstacle)

                break

    # Bird collision with obstacles
    for obstacle in obstacles:
        if bird.colliderect(obstacle["rect"]):
            game_over = True
            return

    for pipe in pipes:
        pipe.x += velocity_x

        # Score when bird passes a pipe
        if not pipe.passed and bird.x > pipe.x + pipe.width:
            score += 0.5
            pipe.passed = True

        # Collision detection
        if bird.colliderect(pipe):
            game_over = True
            return

    # Remove pipes that have moved off-screen
    while len(pipes) > 0 and pipes[0].x < -pipe_width:
        pipes.pop(0)


def create_pipes():
    random_pipe_y = (
        pipe_y - pipe_height / 4
        - random.random() * (pipe_height / 2)
    )

    opening_space = GAME_HEIGHT / 4

    top_pipe = Pipe(top_pipe_image)
    top_pipe.y = random_pipe_y
    pipes.append(top_pipe)

    bottom_pipe = Pipe(bottom_pipe_image)
    bottom_pipe.y = (
        top_pipe.y + top_pipe.height + opening_space
    )
    pipes.append(bottom_pipe)

    # Create an obstacle in the gap between the pipes
    obstacle_y = (
        top_pipe.bottom + bottom_pipe.top
    ) // 2 - obstacle_height // 2

    obstacle_rect = pygame.Rect(
        GAME_WIDTH + (pipe_width - obstacle_width) // 2,
        obstacle_y,
        obstacle_width,
        obstacle_height
    )

    obstacles.append({
        "rect": obstacle_rect,
        "health": 3
    })


# Initialize Pygame
pygame.init()

window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Mappy Bird")

clock = pygame.time.Clock()

# Pipe creation timer
create_pipes_timer = pygame.USEREVENT + 0
pygame.time.set_timer(create_pipes_timer, 1500)


# Main game loop
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == create_pipes_timer and not game_over:
            create_pipes()

        if event.type == pygame.KEYDOWN:

            # Shoot bullets using C
            if event.key == pygame.K_c and not game_over:
                bullets.append(
                    pygame.Rect(
                        bird.right,
                        bird.centery - 5,
                        20,
                        10
                    )
                )

            if event.key in (pygame.K_SPACE, pygame.K_x, pygame.K_UP):

                if game_over:
                    # Reset game
                    bird.y = bird_y
                    bird.x = bird_x

                    pipes.clear()
                    obstacles.clear()
                    bullets.clear()

                    score = 0
                    velocity_y = 0
                    game_over = False

                else:
                    velocity_y = -6
            
    if not game_over:
        move()

    # Draw continuously, including after game over
    draw()
    pygame.display.update()

    clock.tick(60)
