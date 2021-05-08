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

for i in range(100000):
    
    block = Block(GREEN, 20 ,15)
    
    
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_heigth)
    
    block_list.add(block)
    all_sprites_list.add(block)
    
    
    
player = Block(RED,20,15)
all_sprites_list.add(player)



score = 0
font = pygame.font.Font(None, 100)

play = True
#畫面更新頻率
clock = pygame.time.Clock()
start_ticks=pygame.time.get_ticks()


while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    #清除畫面       
    screen.fill(WHITE)
    
    #計算秒數
    seconds=int((pygame.time.get_ticks()-start_ticks)/1000)
     
    pos = pygame.mouse.get_pos()
    
    player.rect.x=pos[0]
    player.rect.y=pos[1]
    
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    
    for block in blocks_hit_list:
        score += 1
         
    all_sprites_list.draw(screen)
    
    
    message = str(score)+' point'
    text = font.render(message, 10 ,RED)
    screen.blit(text, (10,40))
    
    t = font.render(str(seconds), 10, GREEN)
    screen.blit(t,(100,100))
    
    if seconds>100:
        text = font.render("GAME OVER",50, BLACK)
        screen.blit(text, (100,100))
        play=False
        
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()


