import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
def run_game():
    # 初始化游戏并创建一个屏幕对象

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('打蚊子游戏')
    # 设置背景色
    # bg_color = (230, 230, 230)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.updata()
        bullets.update()
        # 删除子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()