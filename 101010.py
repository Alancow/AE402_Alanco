

import pygame

BLACK = (0,0,0)
WRITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
purple=(255,0,255)



pygame.init()

#size=(700,500)  
screen =pygame.display.set_mode(size)
pygame.display.set_caption("房子")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
         if event.type ==pygame.QUIT:
            done ==True
            
    screen.fill(WRITE)
    
    pygame.draw.rect(screen, GREEN,(350,250,200,100 ))
    pygame.draw.rect(screen, BLACK,(500,190,50,70) )
    pygame.display.flip()
    clock.tick(60)
            
pygame.quit()