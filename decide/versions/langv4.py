import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 1366, 768
FONT_SIZE = 24
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sigmascript v4")
font = pygame.font.Font(None, FONT_SIZE)

# Variables
user_input = ""
output_lines = []
variables = {}

def draw_text(text, position):
    text_surface = font.render(text, True, TEXT_COLOR)
    screen.blit(text_surface, position)

def process_input(input_text):
    global variables
    if input_text.startswith("sigma(") and input_text.endswith(")"):
        output_lines.append(input_text[6:-1])
    elif input_text.startswith("question(") and input_text.endswith(")"):
        question = input_text[9:-1]
        output_lines.append(question)
        # Here you can implement a way to get user response
    elif " add " in input_text:
        var_name, value = input_text.split(" add ")
        var_name = var_name.strip()
        if var_name in variables:
            variables[var_name] += int(value)
        else:
            variables[var_name] = int(value)
    elif " onclick add " in input_text:
        parts = input_text.split(" ")
        var_name = parts[2]
        value = int(parts[4])
        if var_name in variables:
            variables[var_name] += value
        else:
            variables[var_name] = value
    elif input_text.startswith("variable(") and input_text.endswith(")"):
        var_name = input_text[9:-1]
        if var_name not in variables:
            variables[var_name] = 0

def main():
    global user_input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    process_input(user_input)
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        screen.fill(BACKGROUND_COLOR)

        # Draw output
        for i, line in enumerate(output_lines):
            draw_text(line, (10, 10 + i * FONT_SIZE))

        # Draw variables
        var_text = ", ".join(f"{k}-{v}" for k, v in variables.items())
        draw_text(var_text, (WIDTH - 200, 10))

        # Draw user input
        draw_text(user_input, (10, HEIGHT - 30))

        pygame.display.flip()

if __name__ == "__main__":
    main()
