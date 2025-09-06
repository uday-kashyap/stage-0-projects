# Project Name: Flappy Bird (clone)
# @author: Uday Kashyap
# Created: 02 September 2025

# Import required dependencies
import pygame
from pygame.locals import *
import random
import sys

# Initial game configurations
FPS = 32
SCREENHEIGHT = 500
SCREENWIDTH = 300
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GAME_SPRITES = {}
GAME_SOUNDS = {}
MESSAGE = r"gallery\sprites\message.png"
PLAYER = r"gallery\sprites\bird.png"
PIPE = r"gallery\sprites\pipe.png"
BACKGROUND = r"gallery\sprites\background.png"
BASE = r"gallery\sprites\base.png"
GROUNDY = SCREENHEIGHT * 0.8

def isCollide(playerx, playery, upperpipes, lowerpipes):
    playerRect = pygame.Rect(playerx, playery, PLAYERWIDTH, PLAYERHEIGHT)

    if playery > (SCREENHEIGHT - BASEHEIGHT)-25 or playery < 0:
        GAME_SOUNDS["die"].play()
        return True

    # Upper pipe collision
    for pipe in upperpipes:
        pipeRect = pygame.Rect(pipe['x'], pipe['y'], PIPEWIDTH, PIPEHEIGHT)
        if playerRect.colliderect(pipeRect):
            GAME_SOUNDS["hit"].play()
            return True
        
    # Lower pipe collision
    for pipe in lowerpipes:
        pipeRect = pygame.Rect(pipe['x'], pipe['y'], PIPEWIDTH, PIPEHEIGHT)
        if playerRect.colliderect(pipeRect):
            GAME_SOUNDS["hit"].play()
            return True
        
    return False

def generate_random_pipe():
    """
    Generate random pipes.
    """

    # Define pipe attributes
    OFFSET = int(SCREENHEIGHT/3)
    y2 = OFFSET + random.randrange(0, int(SCREENHEIGHT - BASEHEIGHT - 1.2*OFFSET))
    y1 = PIPEHEIGHT - y2 + OFFSET
    PIPEX = SCREENWIDTH + 10

    pipe = [
        {'x': PIPEX, 'y': -y1}, # upper pipe
        {'x': PIPEX, 'y': y2} # lower pipe
    ]
    return pipe

def welcomeScreen():
    PLAYERX = int(SCREENWIDTH/7)
    PLAYERY = int((SCREENHEIGHT - PLAYERHEIGHT)/2)
    MESSAGEX = int((SCREENWIDTH - MESSAGEWIDTH)/2)
    MESSAGEY = int(SCREENHEIGHT*0.05)
    BASEX = 0
    BASEY = SCREENHEIGHT - BASEHEIGHT

    while True:
        for event in pygame.event.get():

            # Exit game if 'X' icon or 'Esc' key is pressed
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # Start the game if 'Space' key or 'Up arrow' key is pressed
            elif event.type == KEYDOWN and (event.key in (K_SPACE, K_UP)):
                return
            
            # Blit sprites
            else:
                SCREEN.blit(GAME_SPRITES["background"], (0, 0))
                SCREEN.blit(GAME_SPRITES["message"], (MESSAGEX, MESSAGEY))
                SCREEN.blit(GAME_SPRITES["player"], (PLAYERX, PLAYERY))
                SCREEN.blit(GAME_SPRITES["base"], (BASEX, BASEY))
                pygame.display.update()
                FPS_CLOCK.tick(FPS)



def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/7)
    playery = int((SCREENHEIGHT - PLAYERHEIGHT)/2)
    BASEX = 0
    BASEY = SCREENHEIGHT - BASEHEIGHT

    # Generate random pipes
    newPipe1 = generate_random_pipe()
    newPipe2 = generate_random_pipe()

    # List of upper pipes
    upperpipes = [
        {'x': SCREENWIDTH+200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y': newPipe2[0]['y']}
        ]
    
    # List of lower pipes
    lowerpipes = [
        {'x': SCREENWIDTH+200, 'y': newPipe1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y': newPipe2[1]['y']}
        ]
    
    PIPE_VEL_X = -4
    player_vel_y = -9
    PLAYER_MIN_VEL_Y = -8
    PLAYER_MAX_VEL_Y = 10
    PLAYER_ACC_Y = 1
    PLAYER_FLAP_VEL = -8 # velocity of bird while flapping
    player_flapped = False # 'True' only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key in (K_SPACE, K_UP)):
                if playery > 0:
                    player_vel_y = PLAYER_FLAP_VEL
                    player_flapped = True
                    GAME_SOUNDS["wing"].play()
        
        crashTest = isCollide(playerx, playery, upperpipes, lowerpipes)

        if crashTest:
            print("Game Over!!")
            return
        
        # Check for score
        player_mid_pos = playerx + PLAYERWIDTH
        for pipe in upperpipes:
            pipe_mid_pos = pipe['x'] + PIPEWIDTH
            if pipe_mid_pos <= player_mid_pos < pipe_mid_pos+4:
                score += 1
                print(f"Your score is: {score}")
                GAME_SOUNDS["point"].play()
        
        if player_vel_y < PLAYER_MAX_VEL_Y and not player_flapped:
            player_vel_y += PLAYER_ACC_Y
        
        if player_flapped:
            player_flapped = False

        playery = playery + min(player_vel_y, GROUNDY - playery - PLAYERHEIGHT)

        # Move pipes to the left
        for upperpipe, lowerpipe in zip(upperpipes, lowerpipes):
            upperpipe['x'] += PIPE_VEL_X
            lowerpipe['x'] += PIPE_VEL_X

        # Add a new pipe when the first one is about to cross the leftmost part of the screen
        if 0 < upperpipes[0]['x'] < 5:
            newPipe = generate_random_pipe()
            upperpipes.append(newPipe[0])
            lowerpipes.append(newPipe[1])

        # Remove the pipe, if it crosses the screen
        if upperpipes[0]['x'] < -PIPEWIDTH:
            upperpipes.pop(0)
            lowerpipes.pop(0)

        # Blit sprites
        SCREEN.blit(GAME_SPRITES["background"], (0, 0))
        for upperpipe, lowerpipe in zip(upperpipes, lowerpipes):
            SCREEN.blit(GAME_SPRITES["pipe"][0], (upperpipe['x'], upperpipe['y']))
            SCREEN.blit(GAME_SPRITES["pipe"][1], (lowerpipe['x'], lowerpipe['y']))
        SCREEN.blit(GAME_SPRITES["player"], (playerx, playery))
        SCREEN.blit(GAME_SPRITES["base"], (BASEX, BASEY))

        score_digits = [int(x) for x in list(str(score))]
        digit_width = 0
        for digit in score_digits:
            digit_width += GAME_SPRITES["numbers"][digit].get_width()
        x_offset = (SCREENWIDTH - digit_width)/2
        for digit in score_digits:
            SCREEN.blit(GAME_SPRITES["numbers"][digit], (x_offset, SCREENHEIGHT * 0.12))
            x_offset += GAME_SPRITES["numbers"][digit].get_width()

        pygame.display.update()
        FPS_CLOCK.tick(FPS)


if __name__ == '__main__':
    # Core logic of the game

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird by Uday Kashyap")
    # Rescale and load game images
    background = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES["background"] = pygame.transform.scale(
        background,
        (SCREENWIDTH, SCREENHEIGHT)
        )
    
    message = pygame.image.load(MESSAGE).convert_alpha()
    MESSAGEWIDTH = int(SCREENWIDTH * 0.7)
    MESSAGEHEIGHT = int(SCREENHEIGHT * 0.35)
    GAME_SPRITES["message"] = pygame.transform.scale(
        message,
        (MESSAGEWIDTH, MESSAGEHEIGHT)
        )
    
    base = pygame.image.load(BASE).convert_alpha()
    BASEWIDTH = SCREENWIDTH
    BASEHEIGHT = int(SCREENHEIGHT * 0.3)
    GAME_SPRITES["base"] = pygame.transform.scale(
        base,
        (BASEWIDTH, BASEHEIGHT)
        )
    
    player = pygame.image.load(PLAYER).convert_alpha()
    PLAYERHEIGHT = int(SCREENHEIGHT * 0.11)
    PLAYERWIDTH = int(player.get_width() * PLAYERHEIGHT / player.get_height())
    GAME_SPRITES["player"] = pygame.transform.scale(
        player,
        (PLAYERWIDTH, PLAYERHEIGHT)
        )

    pipe = pygame.image.load(PIPE).convert_alpha()
    lower_pipe = pygame.transform.scale(
        pipe,
        (int(SCREENWIDTH * 0.25), int(SCREENHEIGHT * 0.6))
    )
    upper_pipe = pygame.transform.rotate(lower_pipe, 180)
    PIPEWIDTH = lower_pipe.get_width()
    PIPEHEIGHT = lower_pipe.get_height()
    GAME_SPRITES["pipe"] = (upper_pipe, lower_pipe)

    GAME_SPRITES["numbers"] = []
    for i in range(10):
        number = pygame.image.load(rf"gallery\sprites\{i}.png").convert_alpha()

        NUMBERHEIGHT = int(SCREENHEIGHT * 0.06)  
        NUMBERWIDTH = int(number.get_width() * (NUMBERHEIGHT / number.get_height()))

        number = pygame.transform.scale(number, (NUMBERWIDTH, NUMBERHEIGHT))
        GAME_SPRITES["numbers"].append(number)

    # Load game sounds
    GAME_SOUNDS["hit"] = pygame.mixer.Sound(r"gallery\audio\hit.mp3")
    GAME_SOUNDS["die"] = pygame.mixer.Sound(r"gallery\audio\die.mp3")
    GAME_SOUNDS["swoosh"] = pygame.mixer.Sound(r"gallery\audio\swoosh.mp3")
    GAME_SOUNDS["point"] = pygame.mixer.Sound(r"gallery\audio\point.mp3")
    GAME_SOUNDS["wing"] = pygame.mixer.Sound(r"gallery\audio\wing.mp3")

    while True:
        welcomeScreen()
        mainGame()