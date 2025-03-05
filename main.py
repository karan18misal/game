import pygame
import input as i
import player as p
import sprite as s
from map import Map
from tile_loader import Tile_loder
from camera import create_screen
from spammer import sprites_spam
pygame.init()
screen=create_screen(800,600,'game')
color=(30,150,50)
running= True
map1=Map(Tile_loder())
sprites_spam()
player=p.Player(r'C:\Users\ravi4\OneDrive\Pictures\Saved Pictures\player.png',400,300)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            i.key_down.add(event.key)
        elif event.type == pygame.KEYUP:
            i.key_down.remove(event.key)
        screen.fill(color)
        player.update()
        map1.draw(screen)
        for S in s.sprites:
            S.draw(screen)
        for P in p.playerss:
            P.draw_player(screen)
        pygame.display.flip()
pygame.quit()
