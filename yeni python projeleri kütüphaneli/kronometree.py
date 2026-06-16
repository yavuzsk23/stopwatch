import pygame
import sys
import time
import winsound

def main():
    pygame.init()
    
    # Screen Configuration
    WIDTH, HEIGHT = 400, 200
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Stopwatch")
    
    # Typography
    font = pygame.font.SysFont("Arial", 40)
    input_font = pygame.font.SysFont("Arial", 30)

    # State Variables
    target = None
    start_time = None
    user_text = ""
    finished = False

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN and user_text.isdigit():
                    target = int(user_text)       # Set countdown seconds
                    start_time = time.time()
                    finished = False
                elif e.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]    # Delete last character
                else:
                    if e.unicode.isdigit():
                        user_text += e.unicode    # Append digit to input

        # Clear screen with background color
        screen.fill((0, 0, 0))

        if target is None:
            # Render user input screen
            text_surface = input_font.render("Seconds: " + user_text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text_surface, text_rect)
        else:
            remaining = target - int(time.time() - start_time)
            if remaining > 0:
                # Render remaining time
                text_surface = font.render(str(remaining), True, (255, 255, 255))
            else:
                # Handle countdown completion
                text_surface = font.render("BEEP! BEEP!", True, (255, 0, 0))
                if not finished:  # Play alert sound only once
                    winsound.Beep(1000, 500)  # Frequency=1000Hz, duration=500ms
                    winsound.Beep(1000, 500)
                    finished = True
                    
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text_surface, text_rect)

        pygame.display.update()

if __name__ == "__main__":
    main()
