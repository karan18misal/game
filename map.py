import pygame.image
import map_data as m
from camera import camera
class Tilekind:
    def __init__(self,name,image,is_solid):
        self.name=name
        self.image=pygame.image.load(image)
        self.is_solid=is_solid
class Map:
    def __init__(self,tile_kinds):
        self.tile_kinds=tile_kinds
        self.tiles=[]
        data = m.data()
        for line in data:
                row=[]
                for tile_number in line:
                    row.append(int(tile_number))
                self.tiles.append(row)
    def draw(self,screen):
        for y, row in enumerate(self.tiles):
                for x,tile in enumerate(row):
                    image=self.tile_kinds[tile].image
                    screen.blit(image, (x*64-camera.x,y*64-camera.y))
