

import pygame



BLACK = (0,0,0)
WHITE = (255,255,255)


pygame.init()

size=(800,600)
screen =pygame.display.set_mode(size)

pygame.display.set_caption("laser5.ogg")



backgroud_position = [0,0]

backgroud_image = pygame.image.load("saturn_family1.jpg").conveert()
player_image = pygame.image.load("playerShip1_orange.png").conveert()

player_image.set_colorkey(BLACK)

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
         if event.type ==pygame.QUIT:
            done =True
            
         elif event.type == pygame.MOUSEBUTTONDOWN:
             click_sound.play()
              
              
    screen.blit(backgroud_image,backgroud_position)          
    player_position = pygame.mouse.get_pos()  
    x = player_position[0]
    y = player_position[1]
    
    screen.blit()
          
    screen.fill(WHITE)
    pygame.display.flip(player_image,[x,y])
    
    clock.tick(60)
pygame.quit()
    
    
    
    
    
    
    
   