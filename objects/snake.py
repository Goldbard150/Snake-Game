import pygame
from uses.use import SCREEN, SIZE
from uses.background import SQUARE_SIZE
from objects.apple import Apple
from score.score import Score

SNAKE_SIZE = 40
COLOR = (0, 100, 0)

pygame.mixer.init()
eat_sound = pygame.mixer.Sound("sounds/eat_apple.wav")

def load_images() -> list:

    body_img = pygame.image.load("assets/snake_body.png")
    body_img = pygame.transform.scale(body_img, (SNAKE_SIZE * 2, SNAKE_SIZE * 2))

    file_mapping = {"RIGHT": "assets/snake_head_RIGHT.png",
                    "LEFT": "assets/snake_head_LEFT.png",
                    "UP": "assets/snake_head_UP.png",
                    "DOWN": "assets/snake_head_DOWN.png"}

    head_names = {}
    for direction,path in file_mapping.items():
        try:
            img = pygame.image.load(path).convert_alpha()
            head_names[direction] = pygame.transform.scale(img, (SNAKE_SIZE * 1.2, SNAKE_SIZE * 1.2))
        except FileNotFoundError as e:
            print(f"Can't Load The Image: {e}")

    return [head_names, body_img]

class Snake:
    def __init__(self):
        self._body = [(100, 100), (80, 100), (60, 100)]
        self._direction = "RIGHT"
        self._score = Score()
        self._images = load_images()

    def draw(self):
        """
        The function draws the snake.
        """
        head_images, body_img = self._images
        for i, pos in enumerate(self._body):
            if i == 0:
                grid_rect = pygame.Rect(pos[0], pos[1], SQUARE_SIZE, SQUARE_SIZE)
                image_rect = head_images[self._direction].get_rect()
                image_rect.center = (grid_rect.centerx + SQUARE_SIZE // 2,
                                     grid_rect.centery + SQUARE_SIZE // 2)
                SCREEN.blit(head_images[self._direction], image_rect)
            else:
                SCREEN.blit(body_img, pos)


    def move(self, remove: bool):
        """
        The function changes the direction of the snake.
        """
        head_x, head_y = self._body[0]
        if self._direction == "RIGHT":
            head_x += SNAKE_SIZE
        elif self._direction == "LEFT":
            head_x -= SNAKE_SIZE
        elif self._direction == "UP":
            head_y -= SNAKE_SIZE
        else:
            head_y += SNAKE_SIZE

        new_head = (head_x, head_y)
        self._body.insert(0, new_head)

        if not remove:
            self._body.pop()

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
        head_rect = pygame.Rect(self._body[0][0], self._body[0][1], SNAKE_SIZE, SNAKE_SIZE)
        head_rect.centerx += SQUARE_SIZE // 2
        head_rect.centery += SQUARE_SIZE // 2

        if head_rect.colliderect(apple.rect):
            apple.change_collision()
            self._score.increase()
            eat_sound.play()
            return True
        return False

    def fail(self) -> bool:
        """
        The function checks if there was any kind of bad collision.
        :return: True if not collided, False if collided.
        """
        if self._check_self_collision() or self._check_out_board():
            return False
        return True

    def _check_self_collision(self) -> bool:
        """
        The function checks if the snake is collided with itself.
        :return: True of False if collided or not.
        """
        head = self._body[0]
        body = self._body[1:]

        if head in body:
            return True
        return False

    def _check_out_board(self) -> bool:
        """
        The function checks if the snake is out of the board.
        :return: True if the snake is out of the board, else, return False.
        """
        head_x, head_y = self._body[0]

        if (head_x < -SQUARE_SIZE or head_x > SIZE[0] - SQUARE_SIZE * 1.5 or
                head_y < -SQUARE_SIZE or head_y > SIZE[1] - SQUARE_SIZE * 1.5):
            return True
        return False

    def get_score(self):
        return self._score
