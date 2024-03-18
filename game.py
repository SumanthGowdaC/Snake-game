import pygame
import sys
import random
pygame.init()
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
snake_size = 20
snake_speed = 10
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = 'RIGHT'
food_size = 20
food_position = (random.randrange(1, (width//food_size)) * food_size,
                 random.randrange(1, (height//food_size)) * food_size)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
clock = pygame.time.Clock()
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(win, white, (segment[0], segment[1], snake_size, snake_size))
def draw_food(food_position):
    pygame.draw.rect(win, red, (food_position[0], food_position[1], food_size, food_size))
def game_over():
    font = pygame.font.SysFont(None, 50)
    text = font.render('Game Over', True, white)
    win.blit(text, (width//2 - 100, height//2 - 50))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_LEFT]:
                snake_direction = 'LEFT'
            elif keys[pygame.K_RIGHT]:
                snake_direction = 'RIGHT'
            elif keys[pygame.K_UP]:
                snake_direction = 'UP'
            elif keys[pygame.K_DOWN]:
                snake_direction = 'DOWN'
    if snake_direction == 'RIGHT':
        snake[0] = (snake[0][0] + snake_size, snake[0][1])
    elif snake_direction == 'LEFT':
        snake[0] = (snake[0][0] - snake_size, snake[0][1])
    elif snake_direction == 'UP':
        snake[0] = (snake[0][0], snake[0][1] - snake_size)
    elif snake_direction == 'DOWN':
        snake[0] = (snake[0][0], snake[0][1] + snake_size)
    if snake[0][0] == food_position[0] and snake[0][1] == food_position[1]:
        food_position = (random.randrange(1, (width//food_size)) * food_size,
                         random.randrange(1, (height//food_size)) * food_size)
        snake.append((0, 0))
    if (
        snake[0][0] >= width or snake[0][0] < 0 or
        snake[0][1] >= height or snake[0][1] < 0 or
        snake[0] in snake[1:]
    ):
        game_over()
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    win.fill(black)
    draw_snake(snake)
    draw_food(food_position)
    pygame.display.update()
    clock.tick(snake_speed)
