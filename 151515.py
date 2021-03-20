

import pygame

BLACK = (0,0,0)
WRITE = (255,255,255)
GREEN = (0,255,0)
RED = (255, 0, 0)


PINK = pygame.color.Color("#FF87EE")



pygame.init()

size=(700,500)
screen =pygame.display.set_mode(size)
pygame.display.set_caption("粉圓")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
          if event.type ==pygame.QUIT:
            done==True
            
    screen.fill(WRITE)
    
    pygame.draw.circle(screen, PINK, (100,100),50, 0)
    pygame.draw.circle(screen, BLACK, (100,100),1, 1)
    
    
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
            
            
