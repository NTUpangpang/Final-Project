import pygame
import random
import sys
import os

# 設定基本數值
FPS = 60
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 700
BAR_LENGTH = 100
BAR_WIDTH = 20
energy = 100
loss_energy = 0
pressure = 50
blood_flow = 50
grease = 50
day = 1

# 建立需要使用的顏色
BLACK = (0, 0, 0)
SPRINGGREEN = (0, 255, 127)
DEEPSKYBLUE = (0, 191, 255)
WHITE = (255, 255, 255)


# 建立資料類別
class Button():
    # 設定初始輸入值
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # 建立按鈕
    def draw_button(self):
        screen.blit(self.image, self.rect)
        pygame.display.update()
        waiting = True
        while waiting:
            time.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                    return waiting

    # 建立選項
    def draw_option(option_1, option_2, option_3, option_4, option_5, num_1, num_2, num_3):
        screen.blit(option_1.image, option_1.rect)
        screen.blit(option_2.image, option_2.rect)
        screen.blit(option_3.image, option_3.rect)
        screen.blit(option_4.image, option_4.rect)
        screen.blit(option_5.image, option_5.rect)
        pygame.display.update()
        waiting = True
        while waiting:
            time.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if option_1.rect.collidepoint(event.pos) and check_energy(num_1):
                        return num_1
                    elif option_2.rect.collidepoint(event.pos) and check_energy(num_2):
                        return num_2
                    elif option_3.rect.collidepoint(event.pos) and check_energy(num_3):
                        return num_3
                    elif option_4.rect.collidepoint(event.pos) and check_energy(-1):
                        return -1
                    elif option_5.rect.collidepoint(event.pos):
                        return -2

    # 建立結局
    def draw_ending(self):
        screen.blit(self.image, self.rect)
        draw_text("點擊畫面重新開始遊戲...", 20, 490, 670, BLACK)
        pygame.display.update()
        waiting = True
        while waiting:
            time.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                    return waiting


# 建立進度條
def draw_bar(data, x, y):
    if data < 0:
        data = 0
    elif data > 100:
        data = 100
    fill = (data / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_WIDTH)
    fill_rect = pygame.Rect(x, y, fill, BAR_WIDTH)
    pygame.draw.rect(screen, SPRINGGREEN, fill_rect)
    pygame.draw.rect(screen, WHITE, outline_rect, 2)


# 顯示進度條
def show_bar():
    draw_bar(energy, 5, 10)
    draw_bar(pressure, 5, 36)
    draw_bar(blood_flow, 5, 62)
    draw_bar(grease, 5, 88)


# 建立數值(英文和數字)
def draw_index(text, size, x, y, color):
    font = pygame.font.Font(font_name_en, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    screen.blit(text_surface, text_rect)


# 建立文字(中文)
def draw_text(text, size, x, y, color):
    font = pygame.font.Font(font_name_cn, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    screen.blit(text_surface, text_rect)


# 顯示剩餘數值
def show_remain():
    draw_index(str(energy), 14, 115, 10, WHITE)
    draw_index(str(pressure), 14, 115, 36, WHITE)
    draw_index(str(blood_flow), 14, 115, 62, WHITE)
    draw_index(str(grease), 14, 115, 88, WHITE)
    draw_index("Energy", 14, 145, 10, WHITE)
    draw_index("Pressure", 14, 150, 36, WHITE)
    draw_index("Blood flow", 14, 155, 62, WHITE)
    draw_index("Grease", 14, 145, 88, WHITE)


# 顯示天數
def show_day():
    draw_index("Day", 20, 540, 10, DEEPSKYBLUE)
    draw_index(str(day), 20, 570, 10, DEEPSKYBLUE)


# 顯示選項
def show_option():
    select = random.sample(range(15), 3)
    pic_1 = pygame.image.load(option[select[0]])
    pic_2 = pygame.image.load(option[select[1]])
    pic_3 = pygame.image.load(option[select[2]])
    option_1 = Button(pic_1, 0, 450)
    option_2 = Button(pic_2, 200, 450)
    option_3 = Button(pic_3, 400, 450)
    option_4 = Button(refresh_img, 0, 400)
    option_5 = Button(sleep_img, 525, 400)
    selection = option_1.draw_option(option_2, option_3, option_4, option_5, select[0], select[1], select[2])
    function(selection)


# 檢查精力值
def check_energy(selection):
    global energy, pressure, blood_flow, grease
    check = False
    if selection == 0 and energy - 15 >= 0:
        check = True
    elif selection == 1 and energy - 30 >= 0:
        check = True
    elif selection == 2 and energy - 25 >= 0:
        check = True
    elif selection == 3 and energy - 15 >= 0:
        check = True
    elif selection == 4 and energy - 40 >= 0:
        check = True
    elif selection == 5 and energy - 25 >= 0:
        check = True
    elif selection == 6 and energy - 30 >= 0:
        check = True
    elif selection == 7 and energy - 15 >= 0:
        check = True
    elif selection == 8 and energy - 20 >= 0:
        check = True
    elif selection == 9 and energy - 10 >= 0:
        check = True
    elif selection == 10 and energy - 25 >= 0:
        check = True
    elif selection == 11 and energy - 15 >= 0:
        check = True
    elif selection == 12 and energy - 50 >= 0:
        check = True
    elif selection == 13 and energy - 30 >= 0:
        check = True
    elif selection == 14 and energy - 20 >= 0:
        check = True
    elif selection == -1 and energy - 5 >= 0:
        check = True
    return check


# 各選項功能
def function(selection):
    global energy, pressure, blood_flow, grease, loss_energy, day
    # 洗頭
    if selection == 0:
        energy -= 15
        pressure -= 10
        blood_flow += 25
        grease -= 15
    # 看A片
    elif selection == 1:
        energy -= 30
        pressure -= 30
        blood_flow += 20
        grease -= 30
    # 看Vtuber
    elif selection == 2:
        energy -= 25
        pressure -= 25
        blood_flow += 10
        grease += 30
    # 吃麥當勞
    elif selection == 3:
        energy -= 15
        pressure -= 15
        blood_flow -= 10
        grease += 15
    # 跟長輩吃飯
    elif selection == 4:
        energy -= 40
        pressure += 15
        blood_flow += 35
        grease += 10
    # 刮刮樂
    elif selection == 5:
        energy -= 25
        lottery = random.sample(range(2), 1)
        if lottery == 0:
            pressure -= 25
        else:
            pressure += 25
    # 做瑜珈
    elif selection == 6:
        energy -= 30
        pressure -= 20
        blood_flow += 15
    # 梳頭髮
    elif selection == 7:
        energy -= 15
        blood_flow += 10
    # 使用落健
    elif selection == 8:
        energy -= 20
        blood_flow += 30
        grease -= 30
    # 喝酒
    elif selection == 9:
        energy -= 10
        pressure -= 20
    # 寫PBC作業
    elif selection == 10:
        energy -= 25
        pressure += 10
        blood_flow -= 10
        grease += 5
    # 針灸
    elif selection == 11:
        energy -= 15
        blood_flow += 30
    # 暈船
    elif selection == 12:
        energy -= 50
        pressure -= 10
        blood_flow -= 20
        grease += 20
    # 跳breaking
    elif selection == 13:
        energy -= 30
        pressure -= 10
        blood_flow += 30
        grease += 10
    # 打疫苗
    elif selection == 14:
        energy -= 20
        side_effect = random.sample(range(10), 1)
        if side_effect == 0:
            blood_flow -= 50
        else:
            blood_flow += 10
    # 重置
    elif selection == -1:
        energy -= 5
    # 睡眠
    elif selection == -2:
        loss_energy += energy
        energy = 100
        if day < 3:
            day += 1
        else:
            ending()
    if pressure < 0:
        pressure = 0
    elif pressure > 100:
        pressure = 100
    if blood_flow < 0:
        blood_flow = 0
    elif blood_flow > 100:
        blood_flow = 100
    if grease < 0:
        grease = 0
    elif grease > 100:
        grease = 100


def ending():
    global loss_energy, day, main_menu, restart
    outcome = -1
    if pressure < 50:
        if blood_flow < 50:
            if grease < 50:
                outcome = 0
            else:
                outcome = 1
        else:
            if grease < 50:
                outcome = 2
            else:
                outcome = 3
    else:
        if blood_flow < 50:
            if grease < 50:
                outcome = 4
            else:
                outcome = 5
        else:
            if grease < 50:
                outcome = 6
            else:
                outcome = 7
    if loss_energy == 300:
        outcome = 8
    loss_energy = 0
    day = 1
    outcome = pygame.image.load(result[outcome])
    outcome = Button(outcome, 0, 0)
    if outcome.draw_ending():
        main_menu = True
        restart = True


pygame.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Hair or Fail?")
time = pygame.time.Clock()
font_name_en = pygame.font.match_font("arial")
font_name_cn = os.path.join("font.ttf")
icon_img = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon_img)
start_img = pygame.image.load("starting.jpg")
start_button_img = pygame.image.load("start_button.png")
story_img = pygame.image.load("story.jpg")
bg_img = pygame.image.load("background.png")
refresh_img = pygame.image.load("refresh.png")
sleep_img = pygame.image.load("sleep.png")
option = ["0. washing_head.jpg", "1. porn.jpg", "2. Vtuber.jpg", "3. McDonald's.jpg",
          "4. dine_with_relatives.jpg", "5. lottery.jpg", "6. yoga.jpg", "7. combing_hair.jpg",
          "8. hair_tonic.jpg", "9. drink.jpg", "10. PBC_hw.jpg", "11. acupuncture.jpg",
          "12. falling_in_love.jpg", "13. breaking.jpg", "14. vaccine.jpg"]
result = ["15. 000.jpg", "16. 001.jpg", "17. 010.jpg", "18. 011.jpg", "19. 100.jpg",
          "20. 101.jpg", "21. 110.jpg", "22. 111.jpg", "23. do_nothing.jpg"]

running = True
main_menu = True
restart = False
story = False
while running:
    time.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if main_menu:
        screen.blit(start_img, [0, 0])
        start_button = Button(start_button_img, 150, 296)
        if start_button.draw_button():
            if restart:
                main_menu = False
            else:
                main_menu = False
                story = True
    elif story:
        intro = Button(story_img, 0, 0)
        if intro.draw_button():
            story = False
    else:
        screen.blit(bg_img, [0, 0])
        show_bar()
        show_remain()
        show_day()
        show_option()
        pygame.display.update()

pygame.quit()
sys.exit()
