# for some reason this doesnt work, i think the cpu is getting overloaded
# for some reason pressing space ends the game



import pygame, sys
from pygame.locals import QUIT
import random
import math
#music stuff
from pygame import mixer

#display stuff
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#background
background_img = pygame.image.load('background1.png')

# background sound
mixer.music.load('background.wav')#load music with mixer
mixer.music.play(-1)# play music in mixer forevevr





#player
player_img = pygame.image.load('bigger_spaceship.png')
player_x = 368
player_y = 480
player_x_change = 0
player_y_change = 0

def player(x,y):
  DISPLAYSURF.blit(player_img, (x, y))
  
#enemies
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

num_enemies = 6

for i in range(num_enemies):  
  enemy_img.append(pygame.image.load('ufo.png'))
  enemy_x.append(random.randint(0,736))
  enemy_y.append(random.randint(50,150))
  enemy_x_change.append(4)
  enemy_y_change.append(40)

def enemy(x, y, i):
  DISPLAYSURF.blit(enemy_img[i], (x, y))

#bullet
# 'ready' cant see bullet
# 'fired' can see bullet and it is moving
bullet_img = pygame.image.load('blue_bullet.png')
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = 'ready'

# bullet firing loop
def bullet_fire(x,y):
  global bullet_state
  bullet_state = 'fired'
  DISPLAYSURF.blit(bullet_img, (x + 16, y + 10))

# collision loop
def collisions(enemy_x, enemy_y, bullet_x, bullet_y):
  distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
  if distance <  27:
    return True
  else:
    return False


# score
score_value = 0

score_font = pygame.font.Font('freesansbold.ttf', 32)
# download and uplaod new forn to repl later and change the font"freesansbold.ttf" in font vairable to the new font
text_x = 10
text_y = 10

def show_score(x, y):
  score = score_font.render("Score : " + str(score_value), True, (255, 255, 255))
  DISPLAYSURF.blit(score, (x, y))


# game over text


game_over_font = pygame.font.Font('freesansbold.ttf', 64)
# download and uplaod new forn to repl later and change the font"freesansbold.ttf" in font vairable to the new font
text_x = 10
text_y = 10

def game_over_text():
  game_over_text  = game_over_font.render("GAME OVER", True, (255, 255, 255))
  DISPLAYSURF.blit(game_over_text, (200, 250))




# game loop
while True:
  DISPLAYSURF.fill((255, 255, 255))
  # background
  DISPLAYSURF.blit(background_img, (0, 0))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    # player x coord movement
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player_x_change = -5
      if event.key == pygame.K_RIGHT:
        player_x_change = 5
      # bullet stuff
      if event.key == pygame.K_SPACE:
        if bullet_state == 'ready':
          bullet_sound = mixer.sound('laser.wav')
          bullet_sound.play()
          bullet_x = player_x
          bullet_fire(player_x, bullet_y)
        
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        player_x_change = 0
      
    
  player_x += player_x_change
  # if player leaves window border it comes out on the edge of the other border, e.g go to far right then come out on left of screen
  if 0 > player_x:
    player_x = 736
  elif 736 < player_x:
    player_x = 0
  player(player_x, player_y)# paste player on screen


  # enemy movement
  for i in range(num_enemies):

    # game over
    if enemy_y[i] > 440:#change to 440 later 200 is for testing
      for j in range(num_enemies):
        enemy_y[j] = 2000# moves enemies under the screen
      game_over_text()# displays game over text
      break


    
    enemy_x[i] += enemy_x_change[i]
    # enemy cant leave edge boundaries
    if enemy_x[i] < 0:
      enemy_x_change = 4
      enemy_y[i] += enemy_y_change[i]
    elif enemy_x[i] > 736:
      enemy_x_change[i] = -4
      enemy_y[i] += enemy_y_change[i]

      # collisions
    collision = collisions(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
    if collision == True:
      bullet_y = player_y
      bullet_state = 'ready'
      score_value += 1
      enemy_x[i] = random.randint(0,736)
      enemy_y[i] = random.randint(50,150)
      explosion_sound = mixer.sound('explosion.wav')
      explosion_sound.play()


    enemy(enemy_x[i], enemy_y[i], i)# pasting enmey on screen
    
    #this is for trouble shooting
    #print(f"enemy x is {enemy_x} enemy y is {enemy_y}")
    


  # bullet movement
  if bullet_y < 0:
    bullet_y = player_y
    bullet_state = 'ready'
  if bullet_state == 'fired':
    bullet_fire(bullet_x, bullet_y)# paste bullet on screen
    bullet_y -= bullet_y_change

  show_score(text_x, text_y)
  pygame.display.update()