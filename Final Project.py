import pygame

FPS = 60
display_WIDTH = 600
display_HEIGHT = 700

pygame.init()
screen = pygame.display.set_mode((display_WIDTH, display_HEIGHT))
pygame.display.set_caption("Final Project")
time = pygame.time.Clock()
# 以下需加入圖片
image = pygame.image.load("sqrt.png")
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
while running:
    time.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_1.collidepoint(event.pos):
                pass
            elif rect_2.collidepoint(event.pos):
                pass
            elif rect_3.collidepoint(event.pos):
                pass
            elif rect_4.collidepoint(event.pos):
                pass


pygame.quit()