import pygame
import random

# Pygame ni boshlash
pygame.init()

# Oyna o'lchovlari
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zamonaviy Jangari O'yin")

# Ranglar
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# O'yinchi parametrlar
player_width = 50
player_height = 50
player_x = width // 2
player_y = height // 2
player_speed = 5

# Dushman parametrlar
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemies = []

# O'q parametrlar
bullet_width = 5
bullet_height = 10
bullets = []
bullet_speed = 7

# Dushmanlarni yaratish
def create_enemies(num):
    for i in range(num):
        enemy_x = random.randint(0, width - enemy_width)
        enemy_y = random.randint(0, height - enemy_height)
        enemies.append([enemy_x, enemy_y])

# O'yin davomida ishga tushirish
def gameLoop():
    global player_x, player_y
    create_enemies(5)
    run = True
    while run:
        pygame.time.delay(30)  # O'yin tezligini belgilash

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_width:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < height - player_height:
            player_y += player_speed
        if keys[pygame.K_SPACE]:
            bullets.append([player_x + player_width // 2, player_y])  # O'qni o'yinchi pozitsiyasidan chiqarish

        # Dushmanlar harakatlanishi
        for enemy in enemies:
            if enemy[0] < player_x:
                enemy[0] += enemy_speed
            if enemy[0] > player_x:
                enemy[0] -= enemy_speed
            if enemy[1] < player_y:
                enemy[1] += enemy_speed
            if enemy[1] > player_y:
                enemy[1] -= enemy_speed

        # O'q harakatlanishi
        for bullet in bullets:
            bullet[1] -= bullet_speed  # O'q yuqoriga harakatlanadi
            if bullet[1] < 0:  # O'q ekran tashqarisiga chiqsa
                bullets.remove(bullet)

        # Oynani to'ldirish
        win.fill(black)

        # O'yinchini chizish
        pygame.draw.rect(win, green, (player_x, player_y, player_width, player_height))

        # Dushmanlarni chizish
        for enemy in enemies:
            pygame.draw.rect(win, red, (enemy[0], enemy[1], enemy_width, enemy_height))

        # O'qni chizish
        for bullet in bullets:
            pygame.draw.rect(win, blue, (bullet[0], bullet[1], bullet_width, bullet_height))

        pygame.display.update()

    pygame.quit()

gameLoop()
