import pygame
import random

FPS = 60
display_WIDTH = 600
display_HEIGHT = 700
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (192, 192, 192)
WHITE = (255, 255, 255)

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self):
        screen.blit(self.image, self.rect)
        pygame.display.update()
        action = False
        time.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                action = True
        return action


pygame.init()
screen = pygame.display.set_mode((display_WIDTH, display_HEIGHT))
pygame.display.set_caption("Final Project")
time = pygame.time.Clock()
start_img = pygame.image.load("starting.jpg")
story_img = pygame.image.load("story.jpg")  # 跳下一頁的方式改成點任意畫面繼續(文字)
bg_img = pygame.image.load("background.jpg")
image = pygame.image.load("sqrt.png")
# 以下需加入圖片

# screen.blit(image, [100, 550])
# rect_1 = pygame.Rect(100, 550, 100, 100)
# screen.blit(image, [300, 550])
# rect_2 = pygame.Rect(300, 550, 100, 100)
# screen.blit(image, [500, 550])
# rect_3 = pygame.Rect(500, 550, 100, 100)
# screen.blit(image, [550, 450])
# rect_4 = pygame.Rect(550, 450, 100, 100)
# screen.blit(image, [150, 150])

running = True
main_menu = True
story = False
while running:
    time.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if main_menu:
        screen.blit(start_img, [0, 0])  # start_img改成去掉start button的圖
        start_button = Button(290, 340, image)  # image改成start button的圖(位置要調整)
        if start_button.draw():
            main_menu = False
            story = True
    if story:
        intro = Button(0, 0, story_img)
        if intro.draw():
            story = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
            # if rect_1.collidepoint(event.pos):
                # pass
            # elif rect_2.collidepoint(event.pos):
                # pass
            # elif rect_3.collidepoint(event.pos):
                # pass
            # elif rect_4.collidepoint(event.pos):
                # pass


pygame.quit()