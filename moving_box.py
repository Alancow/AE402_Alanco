

import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.init()

size=(500,500)
screen =pygame.display.set_mode(size)

pygame.display.set_caption("移動")





x = 0
y = 0

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
         if event.type ==pygame.QUIT:
            done =True
            
    keys = pygame.key.get_pressed()
            
    if keys[pygame.K_LEFT]:
        x -=1
        
    elif keys[pygame.K_RIGHT]:
          x +=1
          
    elif keys[pygame.K_UP]:
          y -=1      
          
    elif keys[pygame.K_DOWN]:
          y+=1     
          
    
          
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, [x+10, y+10, 10 ,10])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
    
    
    
    
    
    
    
   