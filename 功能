import pygame
import random

FPS = 60
display_WIDTH = 600
display_HEIGHT = 700

WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((display_WIDTH, display_HEIGHT))
pygame.display.set_caption("Final Project")
time = pygame.time.Clock()
screen.fill(WHITE)


# 以下需加入圖片
image = pygame.image.load("C:/Users/劉家齊/Desktop/sqrt.png")
screen.blit(image, [100, 550])
rect_1 = pygame.Rect(100, 550, 100, 100)
screen.blit(image, [300, 550])
rect_2 = pygame.Rect(300, 550, 100, 100)
screen.blit(image, [500, 550])
rect_3 = pygame.Rect(500, 550, 100, 100)
screen.blit(image, [550, 450])
rect_4 = pygame.Rect(550, 450, 100, 100)
screen.blit(image, [150, 150])
pygame.display.update()

running = True
step1 = 0
step2 = 0
step3 = 0
step4 = 0
while running:
    time.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, 16)
        # text1 = font.render('%s %%' % str(int((step % 200) / 200*100)), True, RED)

        # 精力條
        pygame.draw.rect(screen, GRAY, [50, 10, 200, 15])
        pygame.draw.rect(screen, BLUE, [50, 10, step1 % 200, 15])
        text1 = font.render('%s %%' % str(int((step1 % 200)/100 * 100)), True, RED)
        # 壓力條
        pygame.draw.rect(screen, GRAY, [50, 40, 200, 15])
        pygame.draw.rect(screen, BLUE, [50, 40, step2 % 200, 15])
        text2 = font.render('%s %%' % str(int((step2 % 200)/100 * 100)), True, RED)
        # 氣血條
        pygame.draw.rect(screen, GRAY, [50, 70, 200, 15])
        pygame.draw.rect(screen, BLUE, [50, 70, step3 % 200, 15])
        text3 = font.render('%s %%' % str(int((step3 % 200)/100 * 100)), True, RED)
        # 油脂條
        pygame.draw.rect(screen, GRAY, [50, 100, 200, 15])
        pygame.draw.rect(screen, BLUE, [50, 100, step4 % 200, 15])
        text4 = font.render('%s %%' % str(int((step4 % 200)/100 * 100)), True, RED)

        screen.blit(text1, (140, 10))
        screen.blit(text2, (140, 40))
        screen.blit(text3, (140, 70))
        screen.blit(text4, (140, 100))

        result = random.sample(range(15), 3)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_1.collidepoint(event.pos):
                step1 += 1
            elif rect_2.collidepoint(event.pos):
                step2 += 1
            elif rect_3.collidepoint(event.pos):
                step3 += 1
            elif rect_4.collidepoint(event.pos):
                step4 += 1

        pygame.display.flip()

pygame.quit()
