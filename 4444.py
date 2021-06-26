 


import random
import pygame
from queue import Queue



BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

segment_width = 48
segment_height = 48

segment_margin = 2
segment_head_x = 0
segment_head_y = 0

x_change = 1
y_change = 2

score = 0
class Segment(pygame.sprite.Sprite):
    """Class to represent one segment of the snake. """
    
    def __init__(self,x,y):
        
        super().__init__()
        
        
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)
        
        
        self.rect = self.image.get_rect()
        self.rect.x = x*(segment_width+segment_margin)
        self.rect.y = y*(segment_height+segment_margin)
        
        self.x = x
        self.y = y
        
pygame.init()


screen = pygame.display.set_mode([800,600])


pygame.display.set_caption('貪食蛇')


allspriteslist = pygame.sprite.Group()



snake_segments = Queue()
for i in range(5):
    x = 3 + i
    y = 3
    segment = Segment(x, y)
    snake_segments.put(segment)
    allspriteslist.add(segment)
    segment_head_x = x
    segment_head_y = y
    print(i, segment.x, segment.y)
    
clock = pygame.time.Clock()
done=False

eat = True
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
         
         
         
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 1
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 1
                
    
    segment_head_x += x_change
    segment_head_y += y_change
    segment = Segment(segment_head_x, segment_head_y)             
     
    snake_segments.put(segment)
    allspriteslist.add(segment)
    
    if eat:
        xa = random.randrange(16)
        ya = random.randrange(12)
        eat = False
    else:
         old_segment = snake_segments.get()
         allspriteslist.remove(old_segment)
    apple = Segment(xa,ya)
    
    if segment.x==apple.x and segment.y==apple.y:
        score = score+1
        pygame.display.set_caption("貪食蛇/分數: "+ str(score))
        eat = True
         
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, RED, (xa*(segment_width+segment_margin),ya*(segment_width+segment_margin),segment_width, segment_height))
    allspriteslist.draw(screen)
    
    pygame.display.flip()
    
    
    clock.tick(5)
    
pygame.quit()
exit()
    
        
        
