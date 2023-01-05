import pygame, sys
from pygame.locals import QUIT


#display stuff
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)


#player
player_img = pygame.image.load('spaceship.png')
player_x = 400
player_y = 480

def player(x,y):
  DISPLAYSURF.blit(player_img, (x, y))
  



# game loop
while True:
  DISPLAYSURF.fill((255, 255, 255))

  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
      

  
    

  player(player_x, player_y)
  
  pygame.display.update()