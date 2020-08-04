import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRASS_GREEN = (86, 125, 70)
SNAKE_RED = (128, 0, 0)
GREEN = (0, 230, 0)

# fonts
MAIN_FONT = pygame.font.SysFont('KronaOne-Regular.ttf', 90)
BUTTON_FONT = pygame.font.SysFont('ShadowslntoLight-regular.ttf', 40)


def write_text(txt, font, color, x, y, screen):
    text = font.render(txt, 1, color)
    screen.blit(text, (int(x - (text.get_width() / 2)), int(y - (text.get_height() / 2))))


# Button
class Button:
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, font):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            text = font.render(self.text, 1, BLACK)
            screen.blit(text, (
            int(self.x + (text - text.get_width() / 2)), int(self.y + (text - text.get_height() / 2))))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False

# Meny Buttons
Run_button = Button(GREEN, int(WIDTH * 0.3), int(HEIGHT * 0.8), 60, 40, 'Run')

def start_Meny():
    print('start_Meny')
    run = True

    while run:

        # set Background color
        win.fill(WHITE)

        # set buttons
        Run_button.draw(win, BUTTON_FONT)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # draw header
        write_text('Snake', MAIN_FONT, BLACK, int(WIDTH / 2), int(HEIGHT * 0.4), win)

        # draw image
        image = pygame.image.load("snake.jpg")
        win.blit(image, (int(WIDTH / 2 - (image.get_width() / 2)), int(HEIGHT * 0.2 - (image.get_height() / 2))))

        pygame.display.update()
        clock.tick(15)


# game run
start_Meny()
pygame.quit()
