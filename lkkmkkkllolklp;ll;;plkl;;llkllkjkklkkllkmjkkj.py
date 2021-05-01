import pygame
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

class Block(pygame.sprite.Sprite):
    
    def __init__(self, color,width, height):
        
       
        super().__init__()
        
        
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        
pygame.init()


screen_width = 700
screen_heigth = 400
screen = pygame.display.set_mode([screen_width,screen_heigth])

block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

for i in range(100):
    
    block = Block(BLACK, 20 ,15)
    
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_heigth)
    
    
    all_sprites_list.add(block)
    
    
    
player = Block(RED,20,15)
all_sprites_list.add(player)

play = True
#畫面更新頻率
clock = pygame.time.Clock()


while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    screen.fill(WHITE)
    
    all_sprites_list.draw(screen)

    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()









