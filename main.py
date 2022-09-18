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
t.pencolor("blue") 
t.fillcolor('red')
#t.stamp()#creates an image of turtle(in this case at the start pos)

#make a heart
t.penup()
t.left(180)
t.forward(115)
t.right(90) 
t.pendown()
t.begin_fill()
for i in range (180):
  t.forward(1)
  t.right(1)
t.right(180)
for i in range (180):
  t.forward(1)
  t.right(1)
t.right(30)
t.forward(230)
t.right(120)
t.forward(230)
t.end_fill()
t.penup()
t.forward(30)














#make a square that is in a radius of 100 from start pos
''' makse a square with side length 200
t.begin_fill()
t.forward(100)
t.right(90)
for i in range(3): 
  t.forward(200) 
  t.right(90) 
t.forward(100)
t.end_fill()
turtle.done()
'''