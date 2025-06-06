import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

class Ball:
    def __init__ (self, screen, color, x, y, radius, speed_x, speed_y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        screen_width, screen_height = self.screen.get_size()
        # Check for collision with walls
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.speed_y = -self.speed_y
        # Update position
        self.x += self.speed_x
        self.y += self.speed_y


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    balls = []
    for _ in range(100):
        radius = random.randint(1, 15)
        x = random.randint(radius, 1000 - radius)
        y = random.randint(radius, 800 - radius)
        #color = random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'orange'])
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        speed_x = random.randint(1, 25)
        speed_y = random.randint(1, 25)

        ball = Ball(screen, color, x, y, radius, speed_x, speed_y)
        balls.append(ball)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        for ball in balls:
            ball.move()
            ball.draw()

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
