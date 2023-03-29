import pygame
import time

pygame.init()

# Set up the window and background
width = 800
height = 600
window = pygame.display.set_mode((width, height))
background = pygame.Surface((width, height))
background.fill((255, 255, 255))

# Load the robot image
robot_image = pygame.image.load('robot.png')

# Set up the initial robot position and velocity
robot_x = 100
robot_y = 400
robot_vy = -10

# Define the main game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the robot position and velocity
    robot_y += robot_vy
    robot_vy += 1

    # Draw the robot
    window.blit(background, (0, 0))
    window.blit(robot_image, (robot_x, robot_y))

    # Update the display
    pygame.display.update()

    # Pause for a short time to slow down the animation
    time.sleep(0.02)