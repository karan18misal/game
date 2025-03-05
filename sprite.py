import pygame
from camera import camera
sprites = []
loaded={}
class Sprite:
    def __init__(self,image,x,y):
        if image is loaded:
            self.image= loaded[image]
        else:
            self.image= pygame.image.load(image)
            loaded[image]=self.image
        self.x=x
        self.y=y
        sprites.append(self)
    def delete(self):
        sprites.remove(self)
    def draw(self,screen):
        screen.blit(self.image,(self.x-camera.x,self.y-camera.y))
    def not_allowed_xy(self,x,y):
        if y in range(self.y-57,self.y +self.image.get_height()-51) and x in range(self.x-27,self.x + self.image.get_width()):
            return True
