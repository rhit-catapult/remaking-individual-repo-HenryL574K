import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 15)

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        self.y += self.speed

    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        return self.y > self.screen.get_height()

        

    def draw(self):
        """ Draws this sprite onto the screen. """
        pygame.draw.line(self.screen, (0, 0, 225), (self.x, self.y), (self.x, self.y + 5), 2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        self.screen = screen
        self.x = x
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0

    def draw(self):
        """ Draws this sprite onto the screen. """
        if time.time() > self.last_hit_time + 0.1:
            self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_umbrella, (self.x, self.y))

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        hit_box = pygame.Rect(self.x, self.y, self.image_no_umbrella.get_width(), self.image_no_umbrella.get_height())
        return hit_box.collidepoint(raindrop.x, raindrop.y)


class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        self.screen = screen
        self.x = x
        self.y = y 
        self.image = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
        """ Draws this sprite onto the screen. """
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        new_drop = Raindrop(self.screen, random.randint(self.x , self.x + self.image.get_width()), self.y + self.image.get_height()-10)
        self.raindrops.append(new_drop)



def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()
    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()
    mike = Hero(screen, 250, 400, "/Users/henrylevinson/hulman/remaking-individual-repo-HenryL574K/04-Raindrops/Mike_umbrella.png", "/Users/henrylevinson/hulman/remaking-individual-repo-HenryL574K/04-Raindrops/Mike.png")
    alyssa = Hero(screen, 700, 400, "/Users/henrylevinson/hulman/remaking-individual-repo-HenryL574K/04-Raindrops/Alyssa_umbrella.png", "/Users/henrylevinson/hulman/remaking-individual-repo-HenryL574K/04-Raindrops/Alyssa.png")

    cloud = Cloud(screen, 300, 50, "/Users/henrylevinson/hulman/remaking-individual-repo-HenryL574K/04-Raindrops/another_cloud.png")


    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            cloud.y -= 10    
        if pressed_keys[pygame.K_DOWN]:
            cloud.y += 10
        if pressed_keys[pygame.K_LEFT]:
            cloud.x -= 10
        if pressed_keys[pygame.K_RIGHT]:    
            cloud.x += 10


        screen.fill(pygame.Color("White"))

        cloud.draw()
        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

        mike.draw()
        alyssa.draw()

        pygame.display.update()

main()