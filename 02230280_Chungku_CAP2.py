import pygame  # for the game framework
import random  # for generating random numbers
import os  # for working with the file system

# Initialize Pygame
pygame.init()

# Constants for the game, such as window dimensions, object sizes, and colors.
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 40
PLAYER_SIZE = 60
BACKGROUND_COLOR = (255, 255, 255)
BALL_COLOR = (255, 255, 255)
PLAYER_COLOR = (0, 0, 255)
BUTTON_COLOR = (0, 255, 0)
game_over = False

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Changes the current working directory to the specified path
os.chdir('/home/chungku/Desktop/game')

# Initialize player position, character (player_x and player_y), and the player's movement speed
player_x = (WIDTH - PLAYER_SIZE) // 2
player_y = HEIGHT - PLAYER_SIZE
player_speed = 3

# Initialize ball position and speed
ball_x = random.randint(0, WIDTH - BALL_SIZE)
ball_y = 0
ball_speed = 3

# Load the background image
background_image = pygame.image.load("Nature.jpeg").convert()
# Scale the background image to match the screen size
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load the ball icon
icon = pygame.image.load("en.png")
pygame.display.set_icon(icon)

# Initialize and load the high score
high_score = 0

def load_high_score(): #defines a function named
    global high_score #declares that we want to use the global variable ,high_score inside this function, which means we can modify the global variable 
    try: #try-except block to handle potential exceptions that may occur during the file loading process.
        with open("high_score.txt", "r") as file: # it opens a file named "high_score.txt" in read mode ("r"), with statement is used to ensure that the file is properly closed after reading its contents.
            high_score = int(file.read()) #read the contents of the file and convert it to an integer.
    except FileNotFoundError: # if there is an issue opening it, then a FileNotFoundError exception is raised.
        high_score = 0 # if the high score file does not exist, the high score is initialized to 0.

def save_high_score(): #defines a function named save_high_score and it is responsible for saving the high score to a file.
    with open("high_score.txt", "w") as file: #it is used to ensure that the file is properly closed after writing the high score to it, even if an error occurs.
        file.write(str(high_score)) # convert the current value of the global variable high_score to a string and then write that string to the file.

load_high_score()  # Load the high score at the beginning of the game

# Load the sound
catch_sound = pygame.mixer.Sound("ok.mp3")

# Load the background music
background_music = pygame.mixer.Sound("hi.mp3")

# Play the background music
background_music.play(loops=-1)

# Play the background music on a separate channel
background_music_channel = pygame.mixer.Channel(0)
background_music_channel.play(background_music, loops=-1)

# Define a function to display the start menu
def start_menu(): # defines a function named abd it is  responsible for displaying the game's start menu and waiting for user input to start the game.
    while True: #start menu will keep running until the player takes action or closes the game window.
        for event in pygame.event.get(): #it will iterates over a list of events returned by pygame.event.get()
            if event.type == pygame.QUIT: #it will  checks if the current event is a "QUIT" event, which occurs when the player closes the game window.
                pygame.quit() #If the player closes the game window, this line quits the Pygame framework
                quit() #it quits the Python script itself.

#background, color and fonts
        screen.fill(BACKGROUND_COLOR)
        font = pygame.font.Font(None, 72)
        text = font.render("Catch the Ball", True, PLAYER_COLOR)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))

        # Draw the start button
        pygame.draw.rect(screen, BUTTON_COLOR, (WIDTH // 2 - 100, HEIGHT // 2, 200, 50))
        font = pygame.font.Font(None, 36)
        text = font.render("Start", True, BACKGROUND_COLOR)
        screen.blit(text, (WIDTH // 2 - 30, HEIGHT // 2 + 15))

        # Draw the exit button
        pygame.draw.rect(screen, BUTTON_COLOR, (WIDTH // 2 - 100, HEIGHT // 2 + 70, 200, 50))
        exit_text = font.render("Exit", True, BACKGROUND_COLOR)
        screen.blit(exit_text, (WIDTH // 2 - 30, HEIGHT // 2 + 85))

        pygame.display.flip() #is used at the end of the game loop to ensure that any changes to the game screen, such as rendering the game elements, are displayed to the player.

        if event.type == pygame.MOUSEBUTTONDOWN: #checks if the event type is a mouse button click. It's looking for user input where the mouse button is pressed.
            mouse_x, mouse_y = pygame.mouse.get_pos() #it determine where the user clicked.
            if (WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100) and (HEIGHT // 2 <= mouse_y <= HEIGHT // 2 + 50): # checks if the mouse click occurred within the region of a button
                return  # Start button is clicked
            if (WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100) and (HEIGHT // 2 + 70 <= mouse_y <= HEIGHT // 2 + 120): #checks if the mouse click occurred within the region of another button, depending on the context.
                pygame.quit()  # Exit button is clicked


# Define a function to restart the game
def restart_game():#defines a function named restart_game and used to restart the game when called.
    global game_over, score, player_x, player_y, ball_x, ball_y, ball_speed, player_speed #changes made to these variables within the function will affect the global variables with the same names.
    game_over = False #game is not over, and it's ready to be restarted.
    score = 0 #The player's score is reset to 0, as the game is starting over.
    player_x = (WIDTH - PLAYER_SIZE) // 2 #This calculation ensures that the player character is initially centered horizontally.
    player_y = HEIGHT - PLAYER_SIZE #The Y-coordinate of the player character's position is set to a vertical position at the bottom of the game window, just above the edge.
    player_speed = 3 #The speed of the player character is reset to its initial value and we change it
    ball_x = random.randint(0, WIDTH - BALL_SIZE) #the starting position of the ball along the horizontal axis, making it appear at a random horizontal location.
    ball_y = 0 #The Y-coordinate of the ball's position is set to 0, which places the ball at the top of the game window, ready to start falling
    ball_speed = 3 #it determines how fast the ball descends down the screen.

# Initialize the start menu
start_menu()

# Game loop
running = True  # to control the game loop
clock = pygame.time.Clock()  # manage the game's frame rate
score = 0  # track the player's score

while running: #it handles user input and updates the game state 
    #this loop controls player movement, ball movement, collision detection, game over conditions, and rendering the game elements on the screen
    for event in pygame.event.get():  #it iterates over the list of events that have occurred since the last frame.
        if event.type == pygame.QUIT: #it checks if the user closed the game window
            running = False #effectively exiting the game loop and ending the game.
        if event.type == pygame.MOUSEBUTTONDOWN: #it checks if the user clicked the mouse.
            if game_over: #it  used to control certain aspects of the game logic
                mouse_x, mouse_y = pygame.mouse.get_pos() #These lines get the current position of the mouse
                #t checks if the mouse click occurred within the region of the restart button. The restart button is centered horizontally 
                if (WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100) and (HEIGHT // 2 <= mouse_y <= HEIGHT // 2 + 50): 
                    restart_game()

    if not game_over: # checks if the game is not in the "Game Over" state. If it's not game over, the following code block runs.
        keys = pygame.key.get_pressed() #This line gets the state of all keyboard keys and stores it in the keys variable.
        ##if the left arrow key is pressed and if the player's x-coordinate is greater than 0.If both conditions are met, it moves the player to the left.
        if keys[pygame.K_LEFT] and player_x > 0: 
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
            player_x += player_speed

        #makes the ball fall down the screen.
        ball_y += ball_speed
         #checks if the ball has gone beyond the screen's height
        if ball_y > HEIGHT:
            game_over = True
    
       #t's used for conditional execution of code based on whether the condition inside the parentheses is True.
        if (
            player_x < ball_x + BALL_SIZE #it checks if the player's left edge is to the left of the ball's right edge.
            and player_x + PLAYER_SIZE > ball_x #It checks if the player's right edge is to the right of the ball's left edge.
            and player_y < ball_y + BALL_SIZE #hecks if the bottom edge of the player's rectangle is above the top edge of the ball's rectangle
            and player_y + PLAYER_SIZE > ball_y  #It checks if the player's bottom edge is below the ball's top edge.
        ):
            ball_x = random.randint(0, WIDTH - BALL_SIZE) #represents the horizontal (x) position of the ball
            ball_y = 0 #position of the ball at the top of the game window, making it start from the top.
            score += 1 # increments the score by 1 ,it executed when the player successfully catches the ball, so their score increases.
            catch_sound.play() #when the player successfully catches the ball
            
            #This condition is used to determine if the player achieved a new high score.
            if score > high_score:
                high_score = score # the player achieved a new high score and it updated with the current score
                save_high_score() #it is responsible for saving the updated high score to a file 

            ## Increase both player and ball speed as the score increases
            ball_speed += 0.2 ## we can adjust this increment as needed
            player_speed += 1  # we can adjust this increment as needed

    #loaded background image.
    screen.blit(background_image, (0, 0))
    screen.blit(icon, (ball_x, ball_y)) #positions the ball icon based on its current coordinates.
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)) #defines the rectangle's position and dimensions.
    font = pygame.font.Font(None, 36) # deal with rendering and displaying the player's current score on the game screen. It creates a font object with a size of 36, then renders the player's score.
    text = font.render("Score: " + str(score), True, PLAYER_COLOR)
    screen.blit(text, (10, 10)) #it blits the text at the position (10, 10) on the game screen.

    #It checks if the game_over variable is True
    if game_over:
        font = pygame.font.Font(None, 72) #it creates a font object with a size of 72 
        text = font.render("Game Over", True, PLAYER_COLOR) #the "Game Over" text in the PLAYER_COLOR
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4)) #    calculating the position based on the screen's dimensions.
        pygame.draw.rect(screen, BUTTON_COLOR, (WIDTH // 2 - 100, HEIGHT // 2, 200, 50)) #it draw a rectangular button on the screen for restarting the game
        font = pygame.font.Font(None, 36) # font with a size of 36.
        text = font.render("Restart", True, BACKGROUND_COLOR) 
        screen.blit(text, (WIDTH // 2 - 45, HEIGHT // 2 + 15))#The text is positioned slightly below the button's center.

        # Render and display high score
        high_score_text = font.render("High Score: " + str(high_score), True, PLAYER_COLOR)
        screen.blit(high_score_text, (10, 50))

    pygame.display.flip()
    clock.tick(30)

# Quit the game
pygame.quit()
