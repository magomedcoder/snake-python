import random

from src.score import Score
from src.settings import *
from src.snake import Snake

module_charge = pygame.init()
print(module_charge)
msg_font = pygame.font.SysFont('ubuntu', 20)
scr_font = pygame.font.SysFont('ubuntu', 25)


def print_score(score):
    text = scr_font.render("Счет: " + str(score), True, white)
    game_display.blit(text, [0, 0])


def game_start():
    game_over = False
    game_close = False
    x, y = width / 2, height / 2
    x_speed, y_speed = 0, 0
    snake_pixels = []
    snake_length = 1
    target_x, target_y = round(random.randrange(0, width - snake_size) / 10.0) * 10.0, round(
        random.randrange(0, height - snake_size) / 10.0) * 10.0
    while not game_over:
        while game_close:
            game_over_message = msg_font.render("Игра закончена!", True, red)
            high_score = Score.get(game_over_message)
            if snake_length - 1 > high_score:
                high_score = snake_length - 1
                Score.save(high_score)
            high_score_message = msg_font.render("Рекорд: " + str(high_score), True, white)
            game_display.blit(high_score_message, [width / 3 + 30, height / 3 + 60])
            game_display.blit(game_over_message, [width / 4, height / 3])
            print_score(snake_length - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        game_start()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_speed
        y += y_speed
        pygame.draw.rect(game_display, black, [target_x, target_y, snake_size, snake_size])
        snake_pixels.append([x, y])
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]
        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True
        Snake.draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)
        pygame.display.update()
        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()


game_start()
