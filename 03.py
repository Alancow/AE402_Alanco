

import pygame

BLACK = (0,0,0)
WRITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

def recursive_draw(x,y, width, height):
    pygame.draw.rect(screen,BLACK , [x,y,width, height],1)
     
    
    if (width > 14):
        x +=width*0.1
        y +=width*0.1
        width*=0.8
        height*0.8
        recursive_draw(x, y, width, height)
        


pygame.init()

size=(700,500)
screen =pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
         if event.type ==pygame.QUIT:
            done ==True
            
    screen.fill(WRITE)
    
    pygame.draw.line(screen, BLACK, (0,250), (700,250),4)
    pygame.draw.line(screen, BLACK, (350,0), (350, 500),4)
    pygame.draw.circle(screen, BLACK, (100,50), 2,2)
    
    pygame.display.flip()
    clock.tick(60)
            
pygame.quit()