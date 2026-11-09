import pygame 
from sys import exit
import random


#game dimension 
GAME_WIDTH = 360
GAME_HEIGHT = 640

#bird properties
bird_x = GAME_HEIGHT/8
bird_y = GAME_HEIGHT/2
bird_width = 34
bird_height = 24

class bird(pygame.Rect):
    def _init_(self, img)
        pygame.rect._init_(self, bird_x,bird_y,bird_width,bird_height)
        self.img = img


#pipe properties
pipe_x = GAME_WIDTH
pipe_y = 0
pipe_width= 64
pipe_height = 510

class pipe(pygame.Rect):
    def_init(self,img):
    pygame.rect._inti_(self, pipe_x, pipe_y, pipe_width, pipe_height)
    self.img = img
    self.passed = False



#game images
background_image = pygame.image.load("assets/background.jpg")
bird_image = pygame.image.load("assets/bird.png")
bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))
top_pipe_image = pygame.image.load("toppipe.png")
top_pipe_image = pygame.transform.scale(top_pipe_image, (pipe_width, pipe_height))
bottom_pipe_image = pygame.image.load("bottompipe.png")
bottom_pipe_image = pygame.transform.scale(bottom_pipe_image, (pipe_width, pipe_height))

#game logic
bird = Bird(bird_image)
pipes = []
velocity_x = -2 #move pipes to the left speed (simulates bird moving right)
velocity_y = 0 #move bird up/down speed
gravity = 0.4
score = 0
game_over = False


def draw():
    window.blit(background_image, (0, 0))
    window.blit(bird.img, bird)

    for pipe in pipes:
        window.blit(pipe.img, pipe)

        text_str = str(int(score))
        if game_over:
            text_str = "Game Over:" + text_str

        text_font = pygame.font.SysFont("Times New Roman", 57)
        text render = text_font.render(text_str, true, "white")
        window.blit(text_render, (5,0))


def move():
    global velocity_y, score, game_over
    velocity_y += gravity
    bird.y += velocity_y

    if bird.y > GAME_HEIGHT
    game_over = True
    return

    for pipe in pipe:
        pipe.x += velocity_x

        if not pipe.passed and bird.x > pipe.x + pipe.width
        score += 0.5
        pipe.passed = True

        if bird.colliderect(pipe):
            game_over = ture 
            return
        # clean up pipes that moved off left side of screen
        while len(pipes) > 0 pipes[0].x , -pipe_width:
            pipes.pop(0)

