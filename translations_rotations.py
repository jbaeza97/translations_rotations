import pygame
import math

rectangle = [[50, 50], [50, 100], [100, 100], [100, 50]]
triangle = [[50, 50], [50, 100], [100, 100]]
hexagon = [[50, 50], [50, 100], [75, 125], [100, 100], [100, 50], [75, 25]]


def convert_deg_to_rad(degrees):
    return degrees * math.pi / 180


def rotation(figure, degrees):
    for coord in figure:
        coord[0] = (coord[0] * math.cos(degrees)) + (coord[1] * math.sin(degrees))  # x' coord
        coord[1] = (-coord[0] * math.sin(degrees)) + (coord[1] * math.cos(degrees))  # y' coord
    return figure


def main(figure):
    background_colour = (255, 255, 255)  # define variable for background color
    (width, height) = (600, 600)
    blue = (0, 0, 255)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Translations & Rotations')
    screen.fill(background_colour)
    pygame.display.flip()

    running = True
    while running:
        pygame.draw.polygon(screen, blue, figure)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    for coord in figure:
                        coord[1] += 10
                    screen.fill(background_colour)
                    pygame.draw.polygon(screen, blue, figure)
                elif event.key == pygame.K_UP:
                    for coord in figure:
                        coord[1] -= 10
                    screen.fill(background_colour)
                    pygame.draw.polygon(screen, blue, figure)
                elif event.key == pygame.K_LEFT:
                    for coord in figure:
                        coord[0] -= 10
                    screen.fill(background_colour)
                    pygame.draw.polygon(screen, blue, figure)
                elif event.key == pygame.K_RIGHT:
                    for coord in figure:
                        coord[0] += 10
                    screen.fill(background_colour)
                    pygame.draw.polygon(screen, blue, figure)
                elif event.key == pygame.K_e:
                    figure = rotation(figure, convert_deg_to_rad(5))
                    screen.fill(background_colour)
                    pygame.draw.polygon(screen, blue, figure)
                elif event.key == pygame.K_q:
                    figure = rotation(figure, convert_deg_to_rad(-5))
                    screen.fill(background_colour)
                    pygame.draw.polygon(screen, blue, figure)

        pygame.display.update()


main(rectangle)
