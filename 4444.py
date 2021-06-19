 



import pygame
from queue import Queue



BLACK = (0,0,0)
WHITE = (255,255,255)


segment_width = 15
segment_heght = 15

segment_margin = 3
segment_head_x = 0
segment_head_y = 0

x_change = segment_width + segment_margin
y_change = 0

class Segment(pygame.sprite.Sprite):
    
    
    def __init__():
        
        super().__init__()
        
        
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)
        
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
pygame.init()


screen = pygame.display.set_mode([800,600])


pygame.display.set_caption('貪食蛇')


allspriteslist = pygame.sprite.Group()



snake_segments = Queue
for i in range(15):
    x = 0 + (segment_width + segment_margin)*i
    y = 30
    segment = Segment(x, y)
    snake_segments.put(segment)
    allspriteslist.add(segment)
    segment_head_x = x
    segment_head_y = y
    
    
clock = pygame.time.Clock()
done=False


while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
         
         
         
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEET:
                x_change = (segment_width + segment_margin) *- 1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width +segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) *- 1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)
                 
                
    old_segment = snake_segments.get()
    allspriteslist.remove(old_segment)
    
    
    
    
    segment_head_x = segment_head_x + x_change
    segment_head_y = segment_head_y + y_change
    segment = Segment(segment_head_x, segment_head_y)
    
    
    snake_segments.put(segment)
    allspriteslist.add(segment)
    
    screen.fill(BLACK)
    
    allspriteslist.draw(screen)
    
    pygame.display.flip()
    
    
    clock.tick(5)
    
pygame.quit()
exit()
    
        
        
