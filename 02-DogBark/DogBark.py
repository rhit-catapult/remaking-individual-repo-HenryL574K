import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    image = pygame.image.load("/Users/henrylevinson/hulman/remaking-individual-repo-HenryL574K/02-DogBark/2dogs.JPG")
    image = pygame.transform.scale(image, (IMAGE_SIZE, IMAGE_SIZE))
    # Prepare the text caption(s)
    font1 = pygame.font.SysFont("applesdgothicneo", 28)
    caption1 = font1.render("Me first", True, WHITE)
    my_fonts = pygame.font.get_fonts()
    print("Available fonts:", my_fonts)
    # Prepare the music
    # TODO 8: Create a Sound object from the "bark.wav" file.
    bark_sound = pygame.mixer.Sound("bark.mp3")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 9: Play the music (bark) if there's a mouse click.
             if event.type == pygame.MOUSEBUTTONDOWN:
                # Play the sound when mouse is clicked
                bark_sound.play()
        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # TODO 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(image, (0, 0))
        # Draw the text onto the screen
        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        x_loc = screen.get_width() / 2 - caption1.get_width() / 2
        y_loc = image.get_height() - 200
        screen.blit(caption1, (x_loc, y_loc))
        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        # Update the screen
        pygame.display.update()


main()
