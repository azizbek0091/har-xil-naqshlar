import os; os.system("cls")
import pygame
import time
import random

pygame.init()

# Oynani o'lchamlari
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ilon O'yini")

# Ranglar
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
light_green = (144, 238, 144)  # Yashil rangning engil versiyasi
blue = (50, 153, 213)

# Ilon parametrlar
snake_block = 10
snake_speed = 15

# Ilon va uning o'lchami
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        color = green if i == 0 else light_green  # Ilon boshini yashil rangda, qolgan qismlarini engil yashil rangda
        pygame.draw.rect(win, color, [x[0], x[1], snake_block, snake_block])

def your_score(score):
    value = score_font.render("Ball: " + str(score), True, white)
    win.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            win.fill(black)
            message("Yutqazdingiz! Qaytadan o'ynash uchun Q, chiqish uchun C ni bosing", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        win.fill(black) 
        pygame.draw.rect(win, red, [foodx, foody, snake_block, snake_block])  # Oziq-ovqat rangini qizil
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
