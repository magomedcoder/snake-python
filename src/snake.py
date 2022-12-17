from src.settings import game_display, white, red, pygame


class Snake:
    def draw_snake(self, snake_pixels):
        i = 0
        for pixel in snake_pixels:
            if i == len(snake_pixels) - 1:
                pygame.draw.rect(game_display, red, [pixel[0], pixel[1], self, self])
            else:
                pygame.draw.rect(game_display, white, [pixel[0], pixel[1], self, self])
            i += 1
