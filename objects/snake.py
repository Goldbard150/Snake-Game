import pygame
from uses.const import SCREEN, SIZE
from objects.apple import Apple
from score.score import Score

TITLE_SIZE = 20
COLOR = (0, 100, 0)

class Snake:
    def __init__(self):
        self._coordinates = [(100, 100), (80, 100), (60, 100)]
        self._direction = "RIGHT"
        self._score = Score()

    def draw(self):
        """
        The function draws the snake.
        """
        for segment in self._coordinates:
            pygame.draw.rect(SCREEN, COLOR, [segment[0], segment[1], TITLE_SIZE, TITLE_SIZE])

    def move(self, remove: bool):
        """
        The function changes the direction of the snake.
        """
        head_x, head_y = self._coordinates[0]
        if self._direction == "RIGHT":
            head_x += TITLE_SIZE
        elif self._direction == "LEFT":
            head_x -= TITLE_SIZE
        elif self._direction == "UP":
            head_y -= TITLE_SIZE
        elif self._direction == "DOWN":
            head_y += TITLE_SIZE

        new_head = (head_x, head_y)

        self._coordinates.insert(0, new_head)

        if not remove:
            self._coordinates.pop()

    def check_direction(self, event: pygame.event.EventType) -> None:
        """
        The function checks which key event is pressed and changes the direction.
        :param event: pygame.KEYDOWN
        """
        if ((event.key == pygame.K_UP or event.key == pygame.K_w)
                and self._direction != "DOWN"):
            self._direction = "UP"
        elif ((event.key == pygame.K_DOWN or event.key == pygame.K_s)
              and self._direction != "UP"):
            self._direction = "DOWN"
        elif ((event.key == pygame.K_RIGHT or event.key == pygame.K_d)
              and self._direction != "LEFT"):
            self._direction = "RIGHT"
        elif ((event.key == pygame.K_LEFT or event.key == pygame.K_a)
              and self._direction != "RIGHT"):
            self._direction = "LEFT"

    def eat_food(self, apple: Apple) -> bool:
        """
        The function eats the food of the snake, the collision with the apple.
        When the snake is collided with the apple, the apple is generated in other x, y.
        :param apple: Apple object
        :return: return True or False if collided or not.
        """
        head_rect = pygame.Rect(self._coordinates[0][0], self._coordinates[0][1],
                                TITLE_SIZE, TITLE_SIZE)

        apple_rect = pygame.Rect(apple.position[0], apple.position[1],
                                 apple.size, apple.size)

        if head_rect.colliderect(apple_rect):
            apple.change_collision()
            self._score.increase()
            return True
        return False

    def fail(self) -> bool:
        """
        The function checks if there was any kind of bad collision.
        :return: True if not collided, False if collided.
        """
        return not (self._check_self_collision() or self._check_out_board())

    def _check_self_collision(self) -> bool:
        """
        The function checks if the snake is collided with itself.
        :return: True of False if collided or not.
        """
        head = self._coordinates[0]
        body = self._coordinates[1:]

        if head in body:
            return True
        return False

    def _check_out_board(self) -> bool:
        """
        The function checks if the snake is out of the board.
        :return: True if the snake is out of the board, else, return False.
        """
        head_x, head_y = self._coordinates[0]
        if head_x < 0 or head_x >= SIZE[0] or head_y < 0 or head_y >= SIZE[1]:
           return True
        return False

    def get_score(self):
        return self._score










