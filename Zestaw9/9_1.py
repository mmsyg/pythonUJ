import pygame
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snowfall")

snowflakes = []
score = 0
lives = 5

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
done = False


ADD_SNOWFLAKE = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_SNOWFLAKE, 1000) 

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == ADD_SNOWFLAKE:
            x = random.randrange(0, 800)
            y = random.randrange(-50, -10)
            radius = random.randint(8, 15)
            snowflakes.append([x, y, radius])

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for flake in snowflakes[:]:
                    distance = ((flake[0] - mouse_pos[0]) ** 2 + (flake[1] - mouse_pos[1]) ** 2) ** 0.5
                    if distance < flake[2]:
                        snowflakes.remove(flake)
                        score += 1

    screen.fill(black)

    for flake in snowflakes:
        pygame.draw.circle(screen, white, flake[:2], flake[2])

        flake[1] += 1

        if flake[1] > 800:
            snowflakes.remove(flake)
            lives -= 1

    score_text = font.render("Score: " + str(score), True, white)
    lives_text = font.render("Lives: " + str(lives), True, white)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    if lives <= 0:
        game_over_text = font.render("Game Over!", True, white)
        screen.blit(game_over_text, (300, 400))
        pygame.display.flip()
        pygame.time.delay(2000)
        break

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
