import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    # TODO 4: Return the actual distance between point 1 and point 2.
    #  Hint: you will need the math library for the sqrt function.
    #       distance = sqrt(   (delta x) ** 2 + (delta y) ** 2  )
    return math.sqrt((point2_x - point1_x)**2 + (point2_y - point1_y)**2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)

    pygame.mixer.music.load("/Users/henrylevinson/hulman/remaking-individual-repo-HenryL574K/03-ClickInTheCircle/drums.wav")

    instruction_text = 'Click in the circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    circle_color = (154, 58, 212)
    circle_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle_radius = 50
    circle_border_width = 3

    message_text = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(event.pos)
                print(mouse_pos)
                distance_to_center = distance(mouse_pos, circle_center)
                print(distance_to_center)
                if distance_to_center <= circle_radius:
                    message_text = 'Bullseye!'
                    pygame.mixer.music.play(-1)
                else:
                    message_text = 'Miss!'
                    pygame.mixer.music.stop()



                # TODO 9: Start playing the music mixer looping forever if the click is within the circle

                # TODO 10: Stop playing the music if the click is outside the circle

        screen.fill(pygame.Color("Black"))

        pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)
        caption = font.render(message_text, True, (0, 255, 255))

        screen.blit(instructions_image, (25, 25))
        screen.blit(caption, (25, 300))
        pygame.display.update()


main()
