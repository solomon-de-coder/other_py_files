import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 400, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Fonts
font = pygame.font.SysFont("Arial", 32)

# Bird Class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.width = 40
        self.height = 40
        self.velocity = 0
        self.gravity = 0.5
        self.lift = -10

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def jump(self):
        self.velocity = self.lift  

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

# Pipe Class
class Pipe:
    def __init__(self):
        self.width = 60
        self.height = random.randint(150, 450)
        self.x = WIDTH
        self.gap = 150  # Vertical gap between the top and bottom pipes
        self.velocity = 5

    def update(self):
        self.x -= self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, 0, self.width, self.height))  # Top pipe
        pygame.draw.rect(screen, GREEN, (self.x, self.height + self.gap, self.width, HEIGHT - self.height - self.gap))  # Bottom pipe

# Function to check collisions
def check_collision(bird, pipes):
    if bird.y <= 0 or bird.y >= HEIGHT - bird.height:
        return True
    for pipe in pipes:
        if pipe.x < bird.x + bird.width and pipe.x + pipe.width > bird.x:
            if bird.y < pipe.height or bird.y + bird.height > pipe.height + pipe.gap:
                return True
    return False

# Main Game Loop
def game():
    bird = Bird()
    pipes = [Pipe()]
    clock = pygame.time.Clock()
    score = 0
    run_game = True

    while run_game:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        # Update game state
        bird.update()
        for pipe in pipes:
            pipe.update()

        # Add new pipes
        if pipes[-1].x < WIDTH - 300:
            pipes.append(Pipe())

        # Remove pipes that passed the screen
        if pipes[0].x + pipes[0].width < 0:
            pipes.pop(0)
            score += 1

        # Check for collisions
        if check_collision(bird, pipes):
            print(f"Game Over! Final Score: {score}")
            run_game = False

        # Drawing
        screen.fill(WHITE)
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)

        # Display score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

    pygame.quit()
    sys.exit()

# Start the game
if __name__ == "__main__":
    game()
 