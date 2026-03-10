import pygame
from objects.snake import Snake
from objects.apple import Apple
from uses.const import SCREEN



def start_game():
    pygame.init()
    clock = pygame.time.Clock()
    background_image = pygame.image.load("assets/background.png").convert()

    running = True

    snake = Snake()
    apple = Apple()
    score = snake.get_score()

    while running:
        running = snake.fail()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                snake.check_direction(event)

                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.set_caption("Snake Game")
        SCREEN.blit(background_image, (0, 0))

        snake.draw()
        apple.draw_apple()
        snake.move(snake.eat_food(apple))

        score.update_score()
        score.show_score()

        pygame.display.flip()
        clock.tick(10)

    score.save_score()
    pygame.quit()

if __name__ == '__main__':
    start_game()