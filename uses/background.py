from pygame import draw, image, Surface, Rect
from const import SIZE, SCREEN

GREEN = (69, 255, 72)
BLUE = (145, 255, 247)

SQUARE_SIZE = 40

def generate():
    """
    Generate background image and saves it in assets/background.png
    """
    background = Surface(SCREEN.get_size())
    background = background.convert()

    background.fill(GREEN)
    for start in range(0, SQUARE_SIZE * 2, SQUARE_SIZE):
        for i in range(start, SIZE[0], SQUARE_SIZE * 2):
            for j in range(start, SIZE[1], SQUARE_SIZE * 2):
                square_rect = Rect(i, j, SQUARE_SIZE, SQUARE_SIZE)
                draw.rect(background, BLUE, square_rect)


    image.save(background, "../assets/background.png")


if __name__ == '__main__':
    generate()