import pygame
class Ship():
    def __init__( self, ai_settings, screen):
        # 初始化
        self.screen = screen
        # 加载图像并过去其中外接矩形
        self.ai_settings = ai_settings
        self.image= pygame.image.load('images/1332.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将物品放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
    def updata(self):
        '''根据移动标志调整飞船位置'''
        # 更新物品的center值, 而不是rect

        if self.moving_right and self.rect.right < self.screen_rect.right:

            self.center += self.ai_settings.ship_speed_factor


        if self.moving_left and self.rect.left > 0 :

            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
