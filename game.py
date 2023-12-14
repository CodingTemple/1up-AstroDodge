import pygame  # Import the Pygame library
import random  # Import the random library for random number generation

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 640, 480  # Define the width and height of the game screen
screen = pygame.display.set_mode((screen_width, screen_height))  # Create the game screen
pygame.display.set_caption("AstroDodge")  # Set the title of the window

# Load and scale images for player and enemy
player_image_original = pygame.transform.scale(pygame.image.load('./assets/astronaut.png'), (100, 100))
enemy_image = pygame.transform.scale(pygame.image.load('./assets/asteroid.png'), (50, 50))

# Player setup
player_size = player_image_original.get_size()  # Get the size of the player image
player_pos = [screen_width // 2, screen_height - player_size[1]]  # Set the initial position of the player
player_image = player_image_original.copy()  # Create a copy of the player image for manipulation
facing_right = False  # Flag to keep track of player's facing direction

# Enemy setup
enemy_size = enemy_image.get_size()  # Get the size of the enemy image
enemy_pos = [random.randint(0, screen_width - enemy_size[0]), 0]  # Set initial position of the enemy
enemy_speed = 5  # Set the falling speed of the enemy

# Game loop
clock = pygame.time.Clock()  # Create a clock object to manage frame rate
game_over = False  # Flag to control the game loop

# To make the game pregessively harder start a speed_clock to track game time
speed_clock=0

while not game_over:
    for event in pygame.event.get():  # Check for events
        if event.type == pygame.QUIT:  # If window is closed, quit the game
            game_over = True

    # Increase enemy speed as the game progresses to increase difficulty 
    if speed_clock%50==0:
        enemy_speed += 1

    # Player movement
    keys = pygame.key.get_pressed()  # Get the state of all keyboard buttons
    if keys[pygame.K_LEFT]:  # If left arrow key is pressed
        player_pos[0] -= 10  # Move player left
        if facing_right:  # If player is currently facing right
            player_image = pygame.transform.flip(player_image, True, False)  # Flip image to left
            facing_right = False  # Update facing direction
    elif keys[pygame.K_RIGHT]:  # If right arrow key is pressed
        player_pos[0] += 10  # Move player right
        if not facing_right:  # If player is currently facing left
            player_image = pygame.transform.flip(player_image, True, False)  # Flip image to right
            facing_right = True  # Update facing direction

    # Ensure player remains within screen bounds
    player_pos[0] = max(0, min(player_pos[0], screen_width - player_size[0]))

    # Update enemy position
    enemy_pos[1] += enemy_speed  # Move enemy down
    if enemy_pos[1] > screen_height:  # If enemy moves off-screen
        enemy_pos = [random.randint(0, screen_width - enemy_size[0]), -enemy_size[1]]  # Reset enemy at the top

    # Collision detection
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size[0], player_size[1])  # Define player hitbox
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_size[0], enemy_size[1])  # Define enemy hitbox
    if player_rect.colliderect(enemy_rect):  # Check for collision between player and enemy
        game_over = True  # End game on collision

    # Draw elements
    screen.fill((0, 0, 0))  # Clear the screen by filling it with black
    screen.blit(player_image, (player_pos[0], player_pos[1]))  # Draw the player image
    screen.blit(enemy_image, (enemy_pos[0], enemy_pos[1]))  # Draw the enemy image
    pygame.display.update()  # Update the full display Surface to the screen
    
    # Increment the speed_clock by 1
    speed_clock+=1

    # Cap the frame rate
    clock.tick(30)  # Keep the game running at 30 frames per second

# Quit Pygame
pygame.quit()
