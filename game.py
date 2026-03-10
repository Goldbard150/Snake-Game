import pygame
from objects.snake import Snake
from objects.apple import Apple
from uses.background import show_background

def start_game():
    """
    Start the game
    """
    pygame.init()
    clock = pygame.time.Clock()
    snake = Snake()
    apple = Apple()
    score = snake.get_score()

    running = True

    while running:
        pygame.display.set_caption("Snake Game")
        show_background()

        apple.draw_apple()
        snake.draw()
        snake.move(snake.eat_food(apple))

        score.update_score()
        score.show_score()

        pygame.display.flip()
        clock.tick(10)

        running = snake.fail()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                snake.check_direction(event)

                if event.key == pygame.K_p:
                    score.reset_score()

                if event.key == pygame.K_ESCAPE:
                    running = False


    score.save_score()
    pygame.quit()

if __name__ == '__main__':
    start_game()