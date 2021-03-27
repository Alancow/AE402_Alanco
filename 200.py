

import pygame
import random

def _move(image1,image2):
    global count
    if count < 5:
        image=image1
    elif count >=5:
        image=image2
        
    if count >=10:
        count = 0
    else:
        count += 1
    return image
        

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
count=0
locked=0
done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
         if event.type ==pygame.QUIT:
            done =True
            
         if event.type == pygame.MOUSEBUTTONDOWN:
             POS = pygame.mouse.get_pos()
             print(POS)

    
          
    screen.fill(WHITE)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
    
    
    
    
    
    
    
   