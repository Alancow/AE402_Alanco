

import pygame

BLACK = (0,0,0)
WRITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.init()

size=(500,500)
screen =pygame.display.set_mode(size)

pygame.display.set_caption("下雪")


x=random.randrang(0, 500)
y=random.randrang(0, 500)



done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
         if event.type ==pygame.QUIT:
            done ==True
            
    screen.fill(BLACK)
    
    pygame.draw.circle(screen, WRITE, (x,y), 30, 0)
    
    y =y + 1
    
    
    
    
    
    
    
    if y>400:
    
    pygame.display.flip()
    clock.tick(60)
            
pygame.quit()