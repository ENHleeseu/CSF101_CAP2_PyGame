#game.py

import pygame
import random
import os

class GameQuitException(Exception):
    pass

class CatchTheBallGame:
    def __init__(self):
        pygame.init()
        self.test_mode = False

        # Constants
        self.WIDTH, self.HEIGHT = 800, 600
        self.BALL_SIZE = 40
        self.PLAYER_SIZE = 60
        self.BACKGROUND_COLOR = (255, 255, 255)
        self.BALL_COLOR = (255, 255, 255)
        self.PLAYER_COLOR = (0, 0, 255)
        self.BUTTON_COLOR = (0, 255, 0)

        # Create the game window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Catch the Ball")

        # Changes the current working directory to the specified path
        os.chdir('/home/chungku/Desktop/game')

        # Initialize player position, character, and the player's movement speed
        self.player_x = (self.WIDTH - self.PLAYER_SIZE) // 2
        self.player_y = self.HEIGHT - self.PLAYER_SIZE
        self.player_speed = 3

        # Initialize ball position and speed
        self.ball_x = random.randint(0, self.WIDTH - self.BALL_SIZE)
        self.ball_y = 0
        self.ball_speed = 3

        # Load the background image
        self.background_image = pygame.image.load("Nature.jpeg").convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.WIDTH, self.HEIGHT))

        # Load the ball icon
        self.icon = pygame.image.load("en.png")
        pygame.display.set_icon(self.icon)

        # Load high score
        self.high_score = 0
        self.load_high_score()

        # Load the sound
        self.catch_sound = pygame.mixer.Sound("ok.mp3")

        # Load the background music
        self.background_music = pygame.mixer.Sound("hi.mp3")

        # Game state attributes
        self.game_over = False
        self.score = 0

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def quit_game(self):
        pygame.quit()
        raise GameQuitException("Game quit called")

    def restart_game(self):
        self.game_over = False
        self.score = 0
        self.player_x = (self.WIDTH - self.PLAYER_SIZE) // 2
        self.player_y = self.HEIGHT - self.PLAYER_SIZE
        self.player_speed = 3
        self.ball_x = random.randint(0, self.WIDTH - self.BALL_SIZE)
        self.ball_y = 0
        self.ball_speed = 3

    def start_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

            self.screen.fill(self.BACKGROUND_COLOR)
            font = pygame.font.Font(None, 72)
            text = font.render("Catch the Ball", True, self.PLAYER_COLOR)
            self.screen.blit(text, (self.WIDTH // 2 - text.get_width() // 2, self.HEIGHT // 4))

            pygame.draw.rect(self.screen, self.BUTTON_COLOR, (self.WIDTH // 2 - 100, self.HEIGHT // 2, 200, 50))
            font = pygame.font.Font(None, 36)
            text = font.render("Start", True, self.BACKGROUND_COLOR)
            self.screen.blit(text, (self.WIDTH // 2 - 30, self.HEIGHT // 2 + 15))

            pygame.draw.rect(self.screen, self.BUTTON_COLOR, (self.WIDTH // 2 - 100, self.HEIGHT // 2 + 70, 200, 50))
            exit_text = font.render("Exit", True, self.BACKGROUND_COLOR)
            self.screen.blit(exit_text, (self.WIDTH // 2 - 30, self.HEIGHT // 2 + 85))

            pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (self.WIDTH // 2 - 100 <= mouse_x <= self.WIDTH // 2 + 100) and \
                        (self.HEIGHT // 2 <= mouse_y <= self.HEIGHT // 2 + 50):
                    return
                if (self.WIDTH // 2 - 100 <= mouse_x <= self.WIDTH // 2 + 100) and \
                        (self.HEIGHT // 2 + 70 <= mouse_y <= self.HEIGHT // 2 + 120):
                    self.quit_game()

    def run_game(self):
        self.start_menu()

        # Game loop
        self.running = True
        self.clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_over:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if (self.WIDTH // 2 - 100 <= mouse_x <= self.WIDTH // 2 + 100) and \
                                (self.HEIGHT // 2 <= mouse_y <= self.HEIGHT // 2 + 50):
                            self.restart_game()

            if not self.game_over:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and self.player_x > 0:
                    self.player_x -= self.player_speed
                if keys[pygame.K_RIGHT] and self.player_x < self.WIDTH - self.PLAYER_SIZE:
                    self.player_x += self.player_speed

                self.ball_y += self.ball_speed

                if self.ball_y > self.HEIGHT:
                    self.game_over = True

                if (
                    self.player_x < self.ball_x + self.BALL_SIZE
                    and self.player_x + self.PLAYER_SIZE > self.ball_x
                    and self.player_y < self.ball_y + self.BALL_SIZE
                    and self.player_y + self.PLAYER_SIZE > self.ball_y
                ):
                    self.ball_x = random.randint(0, self.WIDTH - self.BALL_SIZE)
                    self.ball_y = 0
                    self.score += 1
                    self.catch_sound.play()

                    if self.score > self.high_score:
                        self.high_score = self.score
                        self.save_high_score()

                    self.ball_speed += 0.2
                    self.player_speed += 1

            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.icon, (self.ball_x, self.ball_y))
            pygame.draw.rect(self.screen, self.PLAYER_COLOR, (self.player_x, self.player_y, self.PLAYER_SIZE, self.PLAYER_SIZE))
            font = pygame.font.Font(None, 36)
            text = font.render("Score: " + str(self.score), True, self.PLAYER_COLOR)
            self.screen.blit(text, (10, 10))

            if self.game_over:
                font = pygame.font.Font(None, 72)
                text = font.render("Game Over", True, self.PLAYER_COLOR)
                self.screen.blit(text, (self.WIDTH // 2 - text.get_width() // 2, self.HEIGHT // 4))
                pygame.draw.rect(self.screen, self.BUTTON_COLOR, (self.WIDTH // 2 - 100, self.HEIGHT // 2, 200, 50))
                font = pygame.font.Font(None, 36)
                text = font.render("Restart", True, self.BACKGROUND_COLOR)
                self.screen.blit(text, (self.WIDTH // 2 - 45, self.HEIGHT // 2 + 15))

                high_score_text = font.render("High Score: " + str(self.high_score), True, self.PLAYER_COLOR)
                self.screen.blit(high_score_text, (10, 50))

            pygame.display.flip()
            self.clock.tick(30)

        self.quit_game()

# Add the following block at the end of game.py
if __name__ == "__main__":
    game = CatchTheBallGame()
    game.run_game()
