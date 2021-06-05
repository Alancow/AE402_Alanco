import pygame, random, math

class Ball(pygame.sprite.Sprite):
    dx = 0
    dy = 0
    x = 0
    y = 0
    direction = 0
    speed = 0
    
    def __init__(self, sp, srx, sry, radium, color):
        pygame.sprite.Sprite.__init__(self)
        self.speed = sp
        self.x = srx
        self.y = sry
        
        self.image = pygame.Surface([radium*2, radium*2])
        self.image.fill((255,255,255))
        pygame.draw.circle(self.image, color, (radium,radium), radium,0)
        
        self.rect = self.image.get_rect()
        self.rect.center = (srx,sry)
        self.direction = random.randint(40,70)
     
        
    def update(self):
        radian = math.radians(self.direction)
        self.dx = self.speed * math.cos(radian)
        self.dy = self.speed * math.sin(radian)
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()-10):
            self.bouncelr()
        elif(self.rect.top <= 10):
            self.rect.top = 10
            self,bounceup()
        elif( self.rect.bottom >= screen.get_height()-10):
            return True
        else:
            return False
        
    def bouncelr(self):
       self.dx *= -1
    def bounceup(self):
        self.direction = 360 - self.direction
        
    
       
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("建立及使用角色")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))


allsprite = pygame.sprite.Group()
ball1 = Ball(8, 100, 100, 15, (0,0,255))
allsprite.add(ball1)
ball2 = Ball(6, 200, 250, 15, (255,0,0))
allsprite.add(ball2)

clock = pygame.time.Clock()
done = True
while done:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            
    screen.blit(background, (0,0))
    ball1.update()
    ball2.update()
    allsprite.draw(screen)
    
    result = pygame.sprite.collide_rect(ball1, ball2)
    if result == True:
        ball1.collidebounce()
        ball2.collidebounce()
        
    pygame.display.update()
pygame.quit()












