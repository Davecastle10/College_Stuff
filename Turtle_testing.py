#this is me pplaying with the turtle function

#importing relevant packages
import turtle 
import random 

#making a screen for turtle to draw onto
screen = turtle.Screen()
screen.title("Playing with Turtle")
screen.bgcolor('lightblue') #background is lightblue
screen.setup(width = 800, height = 800)
turtle.done()



t = turtle.Turtle() 

t.shape("turtle") 

t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest 

t.color("red") 

t.stamp()# 

x = random.randint(1,200) 

y = random.randint(1,200) 

turns = 0 

placeh = 0 

for i in range(75): 

  t.forward(100) 

  t.right(200) 

  turns +=1 

