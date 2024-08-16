import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 1366, 768
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sigmascript v3")

# Font
font = pygame.font.Font(None, 36)

# Output list
outputs = []
shapes = {}

def draw_circle():
    pygame.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), 50, 2)

def draw_square(position):
    x, y = position
    pygame.draw.rect(screen, BLACK, (x, y, 50, 50), 2)

def draw_grid():
    for i in range(1, 6):
        pygame.draw.line(screen, BLACK, (100, i * 100), (600, i * 100), 2)
        pygame.draw.line(screen, BLACK, (i * 100, 100), (i * 100, 600), 2)
    for i in range(5):
        label = font.render(chr(65 + i), True, BLACK)
        screen.blit(label, (50, 100 + i * 100))
        for j in range(1, 6):
            label = font.render(str(j), True, BLACK)
            screen.blit(label, (100 + i * 100, 50))

def main():
    global outputs, shapes
    input_text = ""
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.startswith("sigma(") and input_text.endswith(")"):
                        output = input_text[6:-1]
                        outputs.append(output)
                    elif input_text.startswith("line"):
                        outputs.append("01101100 01101001 01101110 01100101")
                    elif input_text.startswith("circle"):
                        outputs.append("01101111 01110110 01100001 01101100")
                    elif input_text.startswith("square"):
                        position = input_text.split()[1]
                        if position in shapes:
                            outputs.append(f"Square already exists at {position}.")
                        else:
                            shapes[position] = (100 + (ord(position[0]) - 65) * 100, 100 + (int(position[1]) - 1) * 100)
                            outputs.append(f"Drawing a square at {position}...")
                    elif input_text == "grid":
                        outputs.append("01100111 01110010 01101001 01100100")
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill(WHITE)

        # Draw outputs
        y_offset = 0
        for output in outputs:
            text_surface = font.render(output, True, BLACK)
            screen.blit(text_surface, (10, 10 + y_offset))
            y_offset += 30

        # Draw input text
        input_surface = font.render(input_text, True, BLACK)
        screen.blit(input_surface, (10, HEIGHT - 40))

        # Draw shapes
        if "01101100 01101001 01101110 01100101" in outputs:
            pygame.draw.line(screen, BLACK, (10, HEIGHT // 2), (WIDTH - 10, HEIGHT // 2), 2)
        if "01101111 01110110 01100001 01101100" in outputs:
            draw_circle()
        if "01100111 01110010 01101001 01100100" in outputs:
            draw_grid()
        for position, pos in shapes.items():
            draw_square(pos)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()