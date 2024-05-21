import pygame
import sys
from Editor import Editor
# Initialize Pygame
pygame.init()

editor = Editor()
# Set the window dimensions
window_width = 950
window_height = 630
window = pygame.display.set_mode((window_width, window_height))

# Set the title of the window
pygame.display.set_caption("Matrix of Buttons")

# Load the image for the buttons
boton_img = pygame.image.load("pixeles/9_prueba.png")

# Create a 100x100 matrix
matriz = editor.get_matriz()

# Create a list to store the buttons
botones = []

# Calculate the offset to center the buttons
offset_x = (window_width - 600) // 2  # 600 is the total width of the buttons (100 * 6)
offset_y = (window_height - 600) // 2  # 600 is the total height of the buttons (100 * 6)

# Create the buttons and add them to the list
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        boton = pygame.Rect(j * 10 + offset_x, i * 10 + offset_y, 10, 10)  # Create a rectangle for the button
        botones.append(boton)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                if boton.collidepoint(event.pos):
                    print("¡Botón presionado!")

    # Draw the buttons
    window.fill((255, 255, 255))  # Clear the window with a white background
    for boton in botones:
        window.blit(boton_img, boton)

    # Update the window
    pygame.display.update()