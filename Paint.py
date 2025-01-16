import pygame

pygame.init()

# Set up display for the initial screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set up font 
font = pygame.font.Font(None, 30)

# Colors
black_rgb = (0, 0, 0)
white_rgb = (255, 255, 255)
gray_rgb = (120, 120, 120)
blue_rgb = (0, 0, 255)
red_rgb = (255, 0, 0)
green_rgb = (0, 255, 0)
yellow_rgb = (255, 255, 0)
purple_rgb = (128, 0, 128)
orange_rgb = (255, 165, 0)
pink_rgb = (255, 192, 203)
brown_rgb = (165, 42, 42)
cyan_rgb = (0, 255, 255)
magenta_rgb = (255, 0, 255)
lime_rgb = (0, 255, 0)
navy_rgb = (0, 0, 128)
color_rgb_list = [blue_rgb, red_rgb, green_rgb, yellow_rgb, purple_rgb, orange_rgb,
                  pink_rgb, brown_rgb, cyan_rgb, magenta_rgb, lime_rgb, navy_rgb]

# Menu (Canvas)
menu_rect = pygame.Rect(125, 10, width - 125 - 10, height - 10 - 10)
pygame.draw.rect(screen, (240, 240, 240), menu_rect)  # Canvas background

# Paint button
button_rect = pygame.Rect(10, 10, 100, 50)
pygame.draw.rect(screen, (255, 0, 0), button_rect)  # Button background
text = font.render('Paint', True, (255, 255, 255))  # White text
text_rect = text.get_rect(center=button_rect.center)  # Center text in the rectangle
screen.blit(text, text_rect)  # Draw the text onto the screen

current_color = (240, 240, 240)
current_size = 0
painting = []

# Draw brush size and color options
pygame.draw.rect(screen, gray_rgb, [0, 0, width, 70])
pygame.draw.line(screen, black_rgb, (0, 70), (width, 70), 3)
xl_brush = pygame.draw.rect(screen, black_rgb, [10, 10, 50, 50])
pygame.draw.circle(screen, white_rgb, (35, 35), 20)
l_brush = pygame.draw.rect(screen, black_rgb, [70, 10, 50, 50])
pygame.draw.circle(screen, white_rgb, (95, 35), 15)
m_brush = pygame.draw.rect(screen, black_rgb, [130, 10, 50, 50])
pygame.draw.circle(screen, white_rgb, (155, 35), 10)
s_brush = pygame.draw.rect(screen, black_rgb, [190, 10, 50, 50])
pygame.draw.circle(screen, white_rgb, (215, 35), 5)
brush_size_list = [s_brush, m_brush, l_brush, xl_brush]

# Color palette
blue = pygame.draw.rect(screen, blue_rgb, [width - 35, 10, 25, 25])
red = pygame.draw.rect(screen, red_rgb, [width - 35, 35, 25, 25])
green = pygame.draw.rect(screen, green_rgb, [width - 60, 10, 25, 25])
yellow = pygame.draw.rect(screen, yellow_rgb, [width - 60, 35, 25, 25])
purple = pygame.draw.rect(screen, purple_rgb, [width - 85, 10, 25, 25])
orange = pygame.draw.rect(screen, orange_rgb, [width - 85, 35, 25, 25])
pink = pygame.draw.rect(screen, pink_rgb, [width - 110, 10, 25, 25])
brown = pygame.draw.rect(screen, brown_rgb, [width - 110, 35, 25, 25])
cyan = pygame.draw.rect(screen, cyan_rgb, [width - 135, 10, 25, 25])
magenta = pygame.draw.rect(screen, magenta_rgb, [width - 135, 35, 25, 25])
lime = pygame.draw.rect(screen, lime_rgb, [width - 160, 10, 25, 25])
navy = pygame.draw.rect(screen, navy_rgb, [width - 160, 35, 25, 25])
color_list = [blue, red, green, yellow, purple, orange, pink, brown, cyan, magenta, lime, navy]

pygame.display.update()

# Main game loop
running = True
clock = pygame.time.Clock()

def draw(p):
    for circle in p:
        pygame.draw.circle(screen, circle[0], circle[1], circle[2])

while running:
    clock.tick(60)

    # Clear the screen and redraw the canvas
    screen.fill((240, 240, 240))
    pygame.draw.rect(screen, (240, 240, 240), menu_rect)  # Canvas background
    pygame.draw.rect(screen, gray_rgb, [0, 0, width, 70])
    pygame.draw.line(screen, black_rgb, (0, 70), (width, 70), 3)

    # Redraw brush size and color options
    pygame.draw.rect(screen, black_rgb, xl_brush)
    pygame.draw.circle(screen, white_rgb, (35, 35), 20)
    pygame.draw.rect(screen, black_rgb, l_brush)
    pygame.draw.circle(screen, white_rgb, (95, 35), 15)
    pygame.draw.rect(screen, black_rgb, m_brush)
    pygame.draw.circle(screen, white_rgb, (155, 35), 10)
    pygame.draw.rect(screen, black_rgb, s_brush)
    pygame.draw.circle(screen, white_rgb, (215, 35), 5)

    # Redraw color palette
    pygame.draw.rect(screen, blue_rgb, blue)
    pygame.draw.rect(screen, red_rgb, red)
    pygame.draw.rect(screen, green_rgb, green)
    pygame.draw.rect(screen, yellow_rgb, yellow)
    pygame.draw.rect(screen, purple_rgb, purple)
    pygame.draw.rect(screen, orange_rgb, orange)
    pygame.draw.rect(screen, pink_rgb, pink)
    pygame.draw.rect(screen, brown_rgb, brown)
    pygame.draw.rect(screen, cyan_rgb, cyan)
    pygame.draw.rect(screen, magenta_rgb, magenta)
    pygame.draw.rect(screen, lime_rgb, lime)
    pygame.draw.rect(screen, navy_rgb, navy)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brush_size_list)):
                if brush_size_list[i].collidepoint(event.pos):
                    current_size = (i + 1) * 5

            for i in range(len(color_list)):
                if color_list[i].collidepoint(event.pos):
                    current_color = color_rgb_list[i]

    # Check if mouse is pressed and position is below menu
    if pygame.mouse.get_pressed()[0]:  # Left mouse button
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[1] > 70:  # Ensure the brush doesn't draw in the menu
            painting.append((current_color, mouse_pos, current_size))

    draw(painting)
    pygame.display.flip()

pygame.quit()
