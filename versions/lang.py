import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sigmascript")

# Font
font = pygame.font.Font(None, 36)

# Input text
input_text = ""
shapes = []

def draw_shapes():
    for shape in shapes:
        if shape['type'] == 'line':
            pygame.draw.line(screen, BLACK, shape['start'], shape['end'], 2)
        elif shape['type'] == 'circle':
            pygame.draw.circle(screen, BLACK, shape['center'], shape['radius'], 2)

def execute_command(command):
    if command.startswith("sigma(") and command.endswith(")"):
        output = command[6:-1]
        print(output)
    elif command.startswith("line"):
        start = (100, 100)
        end = (700, 100)
        shapes.append({'type': 'line', 'start': start, 'end': end})
    elif command.startswith("circle"):
        center = (400, 300)
        radius = 50
        shapes.append({'type': 'circle', 'center': center, 'radius': radius})

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                execute_command(input_text)
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    screen.fill(WHITE)
    draw_shapes()

    # Render input text
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (10, HEIGHT - 40))

    pygame.display.flip()