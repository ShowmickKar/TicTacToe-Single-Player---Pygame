import math
import pygame
import sys
import random

pygame.init()

(width, length) = (590, 590)
background_color = (0, 0, 0)

AI = False
toggle: bool = True
human = True

screen = pygame.display.set_mode((width, length))
screen.fill(background_color)
pygame.display.set_caption("TIC TAC TOE using Pygame(Single Player)")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
INDIGO = (70, 130, 255)
GREEN = (0, 255, 0)

first = pygame.draw.rect(screen, WHITE, (20, 20, 170, 170))
second = pygame.draw.rect(screen, WHITE, (210, 20, 170, 170))
third = pygame.draw.rect(screen, WHITE, (400, 20, 170, 170))
fourth = pygame.draw.rect(screen, WHITE, (20, 210, 170, 170))
fifth = pygame.draw.rect(screen, WHITE, (210, 210, 170, 170))
sixth = pygame.draw.rect(screen, WHITE, (400, 210, 170, 170))
seventh = pygame.draw.rect(screen, WHITE, (20, 400, 170, 170))
eight = pygame.draw.rect(screen, WHITE, (210, 400, 170, 170))
ninth = pygame.draw.rect(screen, WHITE, (400, 400, 170, 170))

remaining_moves = 9

board_position_name = []
board_position = []

board_position_name.extend(
    [0, first, second, third, fourth, fifth, sixth, seventh, eight, ninth]
)

board_position.extend(
    [
        0,
        [20, 20],
        [210, 20],
        [400, 20],
        [20, 210],
        [210, 210],
        [400, 210],
        [20, 400],
        [210, 400],
        [400, 400],
    ]
)

grid = [0, "", "", "", "", "", "", "", "", ""]


def check_win():
    if grid[1] == "X" and grid[5] == "X" and grid[9] == "X":
        return "First Player"
    elif grid[3] == "X" and grid[5] == "X" and grid[7] == "X":
        return "First Player"
    elif grid[1] == "X" and grid[4] == "X" and grid[7] == "X":
        return "First Player"
    elif grid[1] == "X" and grid[2] == "X" and grid[3] == "X":
        return "First Player"
    elif grid[3] == "X" and grid[6] == "X" and grid[9] == "X":
        return "First Player"
    elif grid[7] == "X" and grid[8] == "X" and grid[9] == "X":
        return "First Player"
    elif grid[2] == "X" and grid[5] == "X" and grid[8] == "X":
        return "First Player"
    elif grid[4] == "X" and grid[5] == "X" and grid[6] == "X":
        return "First Player"

    elif grid[1] == "O" and grid[5] == "O" and grid[9] == "O":
        return "Second Player"
    elif grid[3] == "O" and grid[5] == "O" and grid[7] == "O":
        return "Second Player"
    elif grid[1] == "O" and grid[4] == "O" and grid[7] == "O":
        return "Second Player"
    elif grid[1] == "O" and grid[2] == "O" and grid[3] == "O":
        return "Second Player"
    elif grid[3] == "O" and grid[6] == "O" and grid[9] == "O":
        return "Second Player"
    elif grid[7] == "O" and grid[8] == "O" and grid[9] == "O":
        return "Second Player"
    elif grid[2] == "O" and grid[5] == "O" and grid[8] == "O":
        return "Second Player"
    elif grid[4] == "O" and grid[5] == "O" and grid[6] == "O":
        return "Second Player"
    else:
        return "No one"


def check_draw():
    return not remaining_moves


def setup():
    global toggle
    global human
    global AI
    toggle = True
    if not AI:
        human = True
    else:
        human = False
    AI = not AI
    grid = [None, "", "", "", "", "", "", "", "", ""]
    board_position_name = []
    board_position = []
    board_position_name.extend(
        [None, first, second, third, fourth, fifth, sixth, seventh, eight, ninth]
    )
    board_position.extend(
        [
            None,
            [20, 20],
            [210, 20],
            [400, 20],
            [20, 210],
            [210, 210],
            [400, 210],
            [20, 400],
            [210, 400],
            [400, 400],
        ]
    )
    return (grid, board_position_name, board_position)


def decide_best_move_AI():
    global grid
    global remaining_moves

    if remaining_moves == 9:
        return random.choice([1, 3, 7, 9])

    for i in range(1, 10):
        if grid[i] == "":
            grid[i] = "X"
            if check_win() == "First Player":
                grid[i] = ""
                return i
            grid[i] = ""
    for i in range(1, 10):
        if grid[i] == "":
            grid[i] = "O"
            if check_win() == "Second Player":
                grid[i] = ""
                return i
            grid[i] = ""
    if remaining_moves == 7:
        if (
            grid[1] == "X" or grid[3] == "X" or grid[7] == "X" or grid[9] == "X"
        ) and grid[5] == "O":
            if grid[1] == "X" or grid[9] == "X":
                return random.choice([3, 7])
            else:
                return random.choice([1, 9])
        else:
            return 5

    if remaining_moves == 5:
        pass

    best_score = -math.inf
    best_move = 0
    for i in range(1, 10):
        if grid[i] == "":
            grid[i] = "X"
            remaining_moves -= 1
            score = minimax_AI(True)
            grid[i] = ""
            remaining_moves += 1
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


def minimax_AI(is_maximizer):
    global grid
    global remaining_moves
    result = check_win()
    if result == "First Player":
        return -1
    if result == "Second Player":
        return 1
    if check_draw():
        return 0

    if is_maximizer:
        best_score = -math.inf
        for i in range(1, 10):
            if grid[i] == "":
                grid[i] = "X"
                remaining_moves -= 1
                best_score = max(best_score, minimax(not is_maximizer))
                grid[i] = ""
                remaining_moves += 1
        return best_score
    else:
        best_score = math.inf
        for i in range(1, 10):
            if grid[i] == "":
                grid[i] = "O"
                remaining_moves -= 1
                best_score = min(best_score, minimax(not is_maximizer))
                grid[i] = ""
                remaining_moves += 1
        return best_score


def decide_best_move():
    global grid
    global remaining_moves

    if not AI:
        return decide_best_move_AI()

    for i in range(1, 10):
        if grid[i] == "":
            grid[i] = "O"
            if check_win() == "Second Player":
                grid[i] = ""
                return i
            grid[i] = ""
    for i in range(1, 10):
        if grid[i] == "":
            grid[i] = "X"
            if check_win() == "First Player":
                grid[i] = ""
                return i
            grid[i] = ""
    if remaining_moves == 8 and (
        grid[1] == "X" or grid[3] == "X" or grid[7] == "X" or grid[9] == "X"
    ):
        # print("What's Happening????")
        return 5
    if remaining_moves == 6 and (
        (grid[1] == "X" and grid[9] == "X") or (grid[3] == "X") and grid[7] == "X"
    ):
        if grid[1] == "":
            return 2
        else:
            return 8
    best_score = -math.inf
    best_move = 0
    for i in range(1, 10):
        if grid[i] == "":
            grid[i] = "O"
            remaining_moves -= 1
            score = minimax(True)
            grid[i] = ""
            remaining_moves += 1
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


def minimax(is_maximizer):
    global grid
    global remaining_moves
    result = check_win()
    if result == "First Player":
        return -1
    if result == "Second Player":
        return 1
    if check_draw():
        return 0

    if is_maximizer:
        best_score = -math.inf
        for i in range(1, 10):
            if grid[i] == "":
                grid[i] = "O"
                remaining_moves -= 1
                best_score = max(best_score, minimax(not is_maximizer))
                grid[i] = ""
                remaining_moves += 1
        return best_score
    else:
        best_score = math.inf
        for i in range(1, 10):
            if grid[i] == "":
                grid[i] = "X"
                remaining_moves -= 1
                best_score = min(best_score, minimax(not is_maximizer))
                grid[i] = ""
                remaining_moves += 1
        return best_score


flag = False

First_Game = True

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if flag and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flag = False
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            raise SystemExit

        if First_Game:
            First_Game = False
            # toggle = not toggle
            # AI = not AI
            (
                grid,
                board_position_name,
                board_position,
            ) = setup()
            screen.fill(background_color)
            remaining_moves = 9
            first = pygame.draw.rect(screen, WHITE, (20, 20, 170, 170))
            second = pygame.draw.rect(screen, WHITE, (210, 20, 170, 170))
            third = pygame.draw.rect(screen, WHITE, (400, 20, 170, 170))
            fourth = pygame.draw.rect(screen, WHITE, (20, 210, 170, 170))
            fifth = pygame.draw.rect(screen, WHITE, (210, 210, 170, 170))
            sixth = pygame.draw.rect(screen, WHITE, (400, 210, 170, 170))
            seventh = pygame.draw.rect(screen, WHITE, (20, 400, 170, 170))
            eight = pygame.draw.rect(screen, WHITE, (210, 400, 170, 170))
            ninth = pygame.draw.rect(screen, WHITE, (400, 400, 170, 170))
            pygame.display.update()
            continue
        if not human and not toggle:
            computer_move = decide_best_move()
            grid[computer_move] = "O"
            img = pygame.image.load("circle_icon.png")
            img = pygame.transform.scale(img, (120, 120))
            screen.blit(
                img,
                (
                    board_position[computer_move][0] + 27,
                    board_position[computer_move][1] + 27,
                ),
            )
            # pygame.time.delay(1000)
            pygame.display.update()
            toggle = not toggle
            human = not human
            remaining_moves -= 1
        elif not human and toggle:
            computer_move = decide_best_move()
            grid[computer_move] = "X"
            img = pygame.image.load("cross_icon.png")
            img = pygame.transform.scale(img, (120, 120))
            screen.blit(
                img,
                (
                    board_position[computer_move][0] + 27,
                    board_position[computer_move][1] + 27,
                ),
            )
            # pygame.time.delay(1000)
            pygame.display.update()
            toggle = not toggle
            human = not human
            remaining_moves -= 1

        elif event.type == pygame.MOUSEBUTTONDOWN and human and toggle:
            click_position = pygame.mouse.get_pos()
            for position in range(1, len(board_position_name)):
                if board_position_name[position].collidepoint(click_position):
                    if grid[position] != "":
                        continue
                    grid[position] = "X"
                    img = pygame.image.load("cross_icon.png")
                    img = pygame.transform.scale(img, (120, 120))
                    screen.blit(
                        img,
                        (
                            board_position[position][0] + 27,
                            board_position[position][1] + 27,
                        ),
                    )
                    pygame.display.update()
                    toggle = not toggle
                    human = not human
                    remaining_moves -= 1
        elif event.type == pygame.MOUSEBUTTONDOWN and human and not toggle:
            click_position = pygame.mouse.get_pos()
            for position in range(1, len(board_position_name)):
                if board_position_name[position].collidepoint(click_position):
                    if grid[position] != "":
                        continue
                    grid[position] = "O"
                    img = pygame.image.load("circle_icon.png")
                    img = pygame.transform.scale(img, (120, 120))
                    screen.blit(
                        img,
                        (
                            board_position[position][0] + 27,
                            board_position[position][1] + 27,
                        ),
                    )
                    pygame.display.update()
                    toggle = not toggle
                    human = not human
                    remaining_moves -= 1

        pygame.display.update()

        if check_win() == "First Player":
            pygame.time.delay(500)
            screen.fill((0, 0, 0))
            pygame.display.update()
            text_surface = pygame.image.load("first_player.win.png")
            screen.blit(text_surface, (20, 0))
            pygame.display.update()
            pygame.time.delay(1000)
            # print(grid)
            # toggle = True
            # human = True
            (
                grid,
                board_position_name,
                board_position,
            ) = setup()
            screen.fill(background_color)
            remaining_moves = 9
            first = pygame.draw.rect(screen, WHITE, (20, 20, 170, 170))
            second = pygame.draw.rect(screen, WHITE, (210, 20, 170, 170))
            third = pygame.draw.rect(screen, WHITE, (400, 20, 170, 170))
            fourth = pygame.draw.rect(screen, WHITE, (20, 210, 170, 170))
            fifth = pygame.draw.rect(screen, WHITE, (210, 210, 170, 170))
            sixth = pygame.draw.rect(screen, WHITE, (400, 210, 170, 170))
            seventh = pygame.draw.rect(screen, WHITE, (20, 400, 170, 170))
            eight = pygame.draw.rect(screen, WHITE, (210, 400, 170, 170))
            ninth = pygame.draw.rect(screen, WHITE, (400, 400, 170, 170))
            pygame.display.update()
            continue

        if check_win() == "Second Player":
            pygame.time.delay(500)
            screen.fill((0, 0, 0))
            pygame.display.update()
            text_surface = pygame.image.load("second_player_win.png")
            screen.blit(text_surface, (20, 0))
            pygame.display.update()
            pygame.time.delay(1000)
            # print(grid)
            # toggle = True
            # human = True
            (
                grid,
                board_position_name,
                board_position,
            ) = setup()
            screen.fill(background_color)
            remaining_moves = 9
            first = pygame.draw.rect(screen, WHITE, (20, 20, 170, 170))
            second = pygame.draw.rect(screen, WHITE, (210, 20, 170, 170))
            third = pygame.draw.rect(screen, WHITE, (400, 20, 170, 170))
            fourth = pygame.draw.rect(screen, WHITE, (20, 210, 170, 170))
            fifth = pygame.draw.rect(screen, WHITE, (210, 210, 170, 170))
            sixth = pygame.draw.rect(screen, WHITE, (400, 210, 170, 170))
            seventh = pygame.draw.rect(screen, WHITE, (20, 400, 170, 170))
            eight = pygame.draw.rect(screen, WHITE, (210, 400, 170, 170))
            ninth = pygame.draw.rect(screen, WHITE, (400, 400, 170, 170))
            pygame.display.update()
            continue

        if check_draw():
            pygame.time.delay(500)
            screen.fill((0, 0, 0))
            pygame.display.update()
            text_surface = pygame.image.load("draw.png")
            screen.blit(text_surface, (20, 0))
            pygame.display.update()
            pygame.time.delay(1000)
            # print(grid)
            # toggle = True
            # human = True
            (
                grid,
                board_position_name,
                board_position,
            ) = setup()
            screen.fill(background_color)
            remaining_moves = 9
            first = pygame.draw.rect(screen, WHITE, (20, 20, 170, 170))
            second = pygame.draw.rect(screen, WHITE, (210, 20, 170, 170))
            third = pygame.draw.rect(screen, WHITE, (400, 20, 170, 170))
            fourth = pygame.draw.rect(screen, WHITE, (20, 210, 170, 170))
            fifth = pygame.draw.rect(screen, WHITE, (210, 210, 170, 170))
            sixth = pygame.draw.rect(screen, WHITE, (400, 210, 170, 170))
            seventh = pygame.draw.rect(screen, WHITE, (20, 400, 170, 170))
            eight = pygame.draw.rect(screen, WHITE, (210, 400, 170, 170))
            ninth = pygame.draw.rect(screen, WHITE, (400, 400, 170, 170))
            pygame.display.update()
            continue

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            raise SystemExit

    pygame.display.flip()

pygame.quit()