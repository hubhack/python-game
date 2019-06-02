import sys
import pygame
def check_events(ship):
    '''响应鼠标和按键'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                # 将向右移动飞船
                ship.moving_right  = True
            elif event.key == pygame.K_LEFT:

                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key ==pygame.K_RIGHT:
                ship.moving_right  = False
            elif event.key == pygame.K_LEFT:

                ship.moving_left = False
def updata_screen(ai_settings, screen , ship):
        '''更新屏幕上的图像, 并切换到新屏幕'''
        # 每次循环都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


