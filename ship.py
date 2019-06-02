import pygame
class Ship():
    def __init__(self, screen):
        # 初始化飞船
        self.screen = screen
        # 加载飞船图像并过去其中外接矩形
        self.image= pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 移动标志
        self.moving_right = False
        self.moving_left = False
    def updata(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right:
            self.rect.centerx += 1

        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
