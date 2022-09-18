#this is me pplaying with the turtle function
#it runs in repl.it but not gitpod
#importing relevant packages
import turtle 
import random 

#making a screen for turtle to draw onto
screen = turtle.Screen()
screen.title("Playing with Turtle")
screen.bgcolor('lightblue') #background is lightblue
screen.setup(width = 500, height = 500)



t = turtle.Turtle() 
t.shape("turtle") 
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest 
t.pencolor("red") 
t.stamp()# 
x = random.randint(1,200) 
y = random.randint(1,200) 
turns = 0 
placeh = 0 
for i in range(75): 
  t.forward(100) 
  t.right(200) 
  turns +=1 
x_pos = t.pos()[0]
y_pos = t.pos()[1]
print(x_pos)
turtle.done()
