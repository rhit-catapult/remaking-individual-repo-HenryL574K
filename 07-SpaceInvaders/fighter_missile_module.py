import pygame
import sys

class Missile:
    def __init__(self, screen, x):
        self.screen = screen
        self.x = x
        self.y = 591  # Hardcoded starting position
        self.has_exploded = False

    def move(self):
        self.y -= 5  # Move the missile up by 5 pixels

    def draw(self):
        pygame.draw.line(self.screen, (255, 0, 0), (self.x, self.y), (self.x, self.y - 8), 4)

    def is_off_screen(self):
        return self.y < 0  # Return True if the missile is off the screen


class Fighter:
    def __init__(self, screen):
        self.missiles = []
        self.screen = screen
        self.image = pygame.image.load("/Users/henrylevinson/hulman/remaking-individual-repo-HenryL574K/07-SpaceInvaders/fighter.png").convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        self.x = screen.get_width() / 2 - self.image.get_width() / 2
        self.y = screen.get_height() - self.image.get_height()

    def move(self, move_amount_x):
        self.x += move_amount_x
        self.x = max(-self.image.get_width() / 2, min(self.x, self.screen.get_width() - self.image.get_width() / 2))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        missile_x = self.x + self.image.get_width() / 2
        missile = Missile(self.screen, missile_x)
        self.missiles.append(missile)

    def remove_exploded_missiles(self):
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].has_exploded or self.missiles[k].y < -8:
                del self.missiles[k]




def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Testing the Fighter and Missiles only")
    screen = pygame.display.set_mode((640, 650))

    fighter = Fighter(screen)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_SPACE]:
                    fighter.fire()
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            fighter.move(-5)
        if pressed_keys[pygame.K_RIGHT]:
            fighter.move(5)

        screen.fill((0, 0, 0))
        fighter.draw()
        for missile in fighter.missiles:
            missile.move()
            missile.draw()
        fighter.remove_exploded_missiles()
        pygame.display.update()


if __name__ == "__main__":
    main()