import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 24
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

# Initialize screen and font
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sigmascript")
font = pygame.font.Font(None, FONT_SIZE)

# Variables storage
variables = {}

def draw_text(text, y):
    rendered_text = font.render(text, True, TEXT_COLOR)
    screen.blit(rendered_text, (10, y))

def process_input(user_input):
    global variables
    lines = user_input.splitlines()
    output = []
    
    for line in lines:
        line = line.strip()
        if line.startswith("sigma(") and line.endswith(")"):
            output.append(line[6:-1])
        elif line.startswith("variable(") and line.endswith(")"):
            var_name = line[9:-1]
            variables[var_name] = 0
            output.append(f"Variable '{var_name}' created with initial value 0.")
        elif line.startswith("question(") and line.endswith(")"):
            parts = line[9:-1].split(')(')
            if len(parts) == 2:
                var_name = parts[0]
                new_value = int(parts[1])
                if var_name in variables:
                    variables[var_name] = new_value
                    output.append(f"Variable '{var_name}' changed to {new_value}.")
                else:
                    output.append(f"Variable '{var_name}' does not exist.")
        elif line.startswith("add ") and " to " in line:
            parts = line.split(" to ")
            if len(parts) == 2:
                increment = int(parts[0][4:])
                var_name = parts[1]
                if var_name in variables:
                    variables[var_name] += increment
                    output.append(f"Variable '{var_name}' increased by {increment}. New value: {variables[var_name]}.")
                else:
                    output.append(f"Variable '{var_name}' does not exist.")
        elif line == "clear":
            output.clear()
        else:
            output.append("Invalid command.")
    
    return output

def main():
    input_buffer = ""
    output_lines = []
    y_offset = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    output_lines.extend(process_input(input_buffer))
                    input_buffer = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_buffer = input_buffer[:-1]
                else:
                    input_buffer += event.unicode

        screen.fill(BACKGROUND_COLOR)
        for i, line in enumerate(output_lines):
            draw_text(line, 10 + i * FONT_SIZE)
        draw_text(f"> {input_buffer}", 10 + len(output_lines) * FONT_SIZE)

        pygame.display.flip()

if __name__ == "__main__":
    main()
