import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up paddles
paddle_width = 10
paddle_height = 100
paddle_speed = 7

# Player 1 (left paddle)
paddle1_x = 20
paddle1_y = window_height // 2 - paddle_height // 2
paddle1_score = 0

# Player 2 (right paddle)
paddle2_x = window_width - 30
paddle2_y = window_height // 2 - paddle_height // 2
paddle2_score = 0

# Set up ball
ball_size = 20
ball_x = window_width // 2 - ball_size // 2
ball_y = window_height // 2 - ball_size // 2
ball_dx = 7 * random.choice((1, -1))
ball_dy = 7 * random.choice((1, -1))

# Set up the game clock to control the frame rate
clock = pygame.time.Clock()

# Display "Press Enter to start the game" message
font_start = pygame.font.Font(None, 36)
start_text = font_start.render("Press Enter to start the game", True, WHITE)
window.blit(start_text, (window_width // 2 - start_text.get_width() // 2, window_height // 2 - start_text.get_height() // 2))
pygame.display.update()

# Wait for player to press Enter
waiting_for_start = True
while waiting_for_start:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                waiting_for_start = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s]:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP]:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddle2_y += paddle_speed

    # Keep paddles within the window bounds
    paddle1_y = max(0, min(window_height - paddle_height, paddle1_y))
    paddle2_y = max(0, min(window_height - paddle_height, paddle2_y))

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collisions with top and bottom walls
    if ball_y <= 0 or ball_y >= window_height - ball_size:
        ball_dy *= -1

    # Ball collisions with paddles
    if paddle1_x + paddle_width >= ball_x >= paddle1_x and paddle1_y + paddle_height >= ball_y >= paddle1_y:
        ball_dx *= -1
    elif paddle2_x - ball_size <= ball_x <= paddle2_x and paddle2_y + paddle_height >= ball_y >= paddle2_y:
        ball_dx *= -1

    # Score points
    if ball_x <= 0:
        paddle2_score += 1
        ball_x = window_width // 2 - ball_size // 2
        ball_y = window_height // 2 - ball_size // 2
        ball_dx *= -1
    elif ball_x >= window_width - ball_size:
        paddle1_score += 1
        ball_x = window_width // 2 - ball_size // 2
        ball_y = window_height // 2 - ball_size // 2
        ball_dx *= -1

    # Check for winning condition
    if paddle1_score == 10 or paddle2_score == 10:
        running = False

    # Clear the window
    window.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(window, WHITE, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(window, WHITE, (ball_x, ball_y, ball_size, ball_size))

    # Display scores
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{paddle1_score} - {paddle2_score}", True, WHITE)
    window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, 10))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)  # Set the desired frames per second (e.g., 60 FPS)

# Clear the window
window.fill(BLACK)

# Determine the winner
winner = "Player 1" if paddle1_score == 10 else "Player 2"
winner_text = font.render(f"{winner} wins the game!", True, WHITE)
window.blit(winner_text, (window_width // 2 - winner_text.get_width() // 2, window_height // 2 - 50))

# Update the display
pygame.display.update()

# Wait for player input to quit the game
waiting_for_input = True
while waiting_for_input:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()