import pygame, sys, time, winsound

pygame.init()
screen = pygame.display.set_mode((400,200))
pygame.display.set_caption("Stopwatch")
font = pygame.font.SysFont("Arial", 40)
input_font = pygame.font.SysFont("Arial", 30)

target = None          # countdown target in seconds
start_time = None      # time when countdown started
user_text = ""         # text input from user
finished = False       # flag to check if beep already played
running = False        # True if running, False if paused
elapsed_time = 0       # total time already counted before pause

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.KEYDOWN:
            # Enter: set target seconds from user input
            if e.key == pygame.K_RETURN and user_text.isdigit():
                target = int(user_text)
                start_time = None
                elapsed_time = 0
                finished = False
                running = False   # wait until "S" pressed
            # Backspace: delete last character
            elif e.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            # Add digit to input
            elif e.unicode.isdigit():
                user_text += e.unicode
            # S key: Start
            elif e.key == pygame.K_s:
                if target is not None and not running:
                    start_time = time.time()
                    running = True
            # P key: Pause
            elif e.key == pygame.K_p:
                if running:
                    elapsed_time += time.time() - start_time
                    running = False
            # R key: Reset
            elif e.key == pygame.K_r:
                running = False
                finished = False
                elapsed_time = 0
                start_time = None

    screen.fill((0,0,0))

    if target is None:
        # Ask user to enter seconds
        text = input_font.render("Seconds: " + user_text, True, (255,255,255))
        screen.blit(text, (50,80))
    else:
        # Calculate remaining time
        if running:
            remaining = target - int(elapsed_time + (time.time() - start_time))
        else:
            remaining = target - int(elapsed_time)

        # Display countdown or beep message
        if remaining > 0:
            text = font.render(str(remaining), True, (255,255,255))
        else:
            text = font.render("BEEP! BEEP!", True, (255,0,0))
            if not finished:
                winsound.Beep(1000, 500)  # frequency=1000Hz, duration=500ms
                winsound.Beep(1000, 500)
                finished = True
        screen.blit(text, (80,80))

    pygame.display.update()
