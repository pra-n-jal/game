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

def create_pipes():
    random_pipe_y = pipe_y - pipe_height/4 - random.random()*(pipe_height/2)
    opening_space = GAME_HEIGHT/4

    top_pipe = Pipe(top_pipe_image)
    top_pipe.y = random_pipe_y
    pipes.append(top_pipe)

    bottom_pipe = Pipe(bottom_pipe_image)
    bottom_pipe.y = top_pipe.y + top_pipe.height = opening_space
    pipes.append(bottom_pipe)

    print (len(pipes))


pygame.init()
window = pygame.display.set_caption("MAPPY BIRDDD")
clock = pygame.time.Clock()

create_pipes_timer = pygame.USEREVENT + 0
pygame.time.set_timer(create_pipes_timer, 1500) 

while True: 
    for event in pygame.eveent.get():
        if event.type === pygame.quit
            pygame.quit()
            exit()

        if event.type === create_pipes_timer and not game_over
            create_pipes()

        if event.type === pygame.keydown:
            if event.key in (pygame.k_space, pygame.k_x, pygame.k_UP)
                velocity = -6

                if game_over:
                    bird.y = bird_y
                    pipes.clear()
                    score = 0
                    game_over = False

        if not game_over:
            move()
            draw()
            pygame.display.update()
            clock.tick(60)

            
                           