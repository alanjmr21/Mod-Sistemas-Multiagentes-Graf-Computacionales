#import libraries
import pygame
from math import pi, cos, sin

pygame.init()

#window size
scr = pygame.display.set_mode((400,400))

#variable de radio y centro
r = 400/2
centro = (400/2,400/2)

#TRIANGLE
#top corner
x1 = centro[0]
y1 = 0

#right bottom corner
x2 = r*cos(11 * pi / 6) + centro[0]
y2 = r/2 + 200

#left bottom corner
x3 = r*cos(7 * pi / 6) + centro[0]
y3 = r/2 + 200

coordenadas = [[x1,y1],[x2,y2],[x3,y3]]

#colors
purple = (131,86,222)
orange = (235,175,86)
white = (255,255,255)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.draw.circle(scr,white,centro,4)
        pygame.draw.circle(scr,purple,centro,r,4)
        pygame.draw.polygon(scr,orange,coordenadas,5)
        pygame.display.flip()
pygame.quit()
