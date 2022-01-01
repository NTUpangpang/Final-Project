import pygame
from sys import exit

pygame.init()
# 畫面大小
display_WIDTH = 600
display_HEIGHT = 700

# color used
WHITE = (255, 255, 255)
GREEN = (0, 255, 127)  # SpringGreen1

FPS = 50
time = pygame.time.Clock()

# 各數值初始値
energy = 100
pressure = 50
blood_flow = 50
grease = 50

# 數值條的長寬
BAR_LENGTH = 100
BAR_WIDTH = 20

while True:
    time.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    def draw_bar(sur, data, x, y):  # 繪製數值條
        global BAR_LENGTH, BAR_WIDTH
        if data <= 0:
            data = 0
        fill = (data / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_WIDTH)
        fill_rect = pygame.Rect(x, y, fill, BAR_WIDTH)
        pygame.draw.rect(screen, GREEN, fill_rect)
        pygame.draw.rect(screen, WHITE, outline_rect, 2)


    font_name = pygame.font.match_font("arial")


    def show_remain(sur, text, size, x, y):  # 顯示剩餘數值
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        sur.blit(text_surface, text_rect)


    #  顯示
    screen = pygame.display.set_mode((display_WIDTH, display_HEIGHT))
    pygame.display.set_caption("Final Project")
    #  會根據各數值改變
    draw_bar(screen, energy, 5, 10)
    draw_bar(screen, pressure, 5, 36)
    draw_bar(screen, blood_flow, 5, 62)
    draw_bar(screen, grease, 5, 88)
    #  會根據各數值改變
    show_remain(screen, str(energy), 14, 115, 10)
    show_remain(screen, str(pressure), 14, 115, 36)
    show_remain(screen, str(blood_flow), 14, 115, 62)
    show_remain(screen, str(grease), 14, 115, 88)
    pygame.display.update()
