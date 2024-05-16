import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width = 950
window_height = 630
window = pygame.display.set_mode((window_width, window_height))

# Set the title of the window
pygame.display.set_caption("Matrix of Buttons")

# Load the image for the buttons
boton_img = pygame.image.load("pixeles/6.png")

# Create a 100x100 matrix
matriz = [[0 for _ in range(100)] for _ in range(100)]

# Create a list to store the buttons
botones = []

# Calculate the offset to center the buttons
offset_x = (window_width - 600) // 2  # 600 is the total width of the buttons (100 * 6)
offset_y = (window_height - 600) // 2  # 600 is the total height of the buttons (100 * 6)

# Create the buttons and add them to the list
for i in range(100):
    for j in range(100):
        boton = pygame.Rect(j * 6 + offset_x, i * 6 + offset_y, 6, 6)  # Create a rectangle for the button
        botones.append(boton)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the buttons
    window.fill((255, 255, 255))  # Clear the window with a white background
    for boton in botones:
        window.blit(boton_img, boton)

    # Update the window
    pygame.display.update()