import pygame
import sprite as s
from input import is_key_down
from camera import camera
from allowed_notallowed import allow_x,allow_not_y
playerss = []
loaded={}
class Player:
    def __init__(self,image,x,y):
        if image is loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image)
            loaded[image] = self.image
        self.x = x
        self.y = y
        playerss.append(self)
        self.movement_speed =4
    def draw_player(self,screen):
        screen.blit(self.image,(self.x-camera.x,self.y-camera.y))
    def update(self):
        previous_x=self.x
        previous_y=self.y
        if self.x<=-1:
            self.x=0
        if self.y<=-1:
            self.y=0
        if is_key_down(pygame.K_w):
            self.y-=self.movement_speed
            if allow_x(self.x) and allow_not_y(self.y):
                self.y = previous_y
                self.x = previous_x
            for S in s.sprites:
                if S.not_allowed_xy(self.x,self.y):
                    self.y = previous_y
                    self.x = previous_x
        if is_key_down(pygame.K_a):
            self.x-=self.movement_speed
            if allow_x(self.x) and allow_not_y(self.y):
                self.y = previous_y
                self.x = previous_x
            for S in s.sprites:
                if S.not_allowed_xy(self.x,self.y):
                    self.y = previous_y
                    self.x = previous_x
        if is_key_down(pygame.K_s):
            self.y+=self.movement_speed
            if allow_x(self.x) and allow_not_y(self.y):
                self.y = previous_y
                self.x = previous_x
            for S in s.sprites:
                if S.not_allowed_xy(self.x,self.y):
                    self.y = previous_y
                    self.x = previous_x
        if is_key_down(pygame.K_d):
            self.x+=self.movement_speed
            if allow_x(self.x) and allow_not_y(self.y):
                self.y = previous_y
                self.x = previous_x
            for S in s.sprites:
                if S.not_allowed_xy(self.x,self.y):
                    self.y = previous_y
                    self.x = previous_x
        camera.x=self.x-camera.width/2+self.image.get_width()
        camera.y=self.y-camera.height/2+self.image.get_height()
