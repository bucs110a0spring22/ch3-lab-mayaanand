import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
leonardo.speed(1)
michelangelo.speed(1)

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
michel_random = random.randrange(1,100)
michelangelo.forward(michel_random)
print(michel_random)
leo_random = random.randrange(1,100)
leonardo.forward(leo_random)
print(leo_random)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(10):
  distance = random.randrange(1,10)
  length = random.randrange(1,10)
  michelangelo.forward(distance)
  leonardo.forward(length)
 
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
# Part B - complete part B here


side = [3, 4, 6, 9, 12] 
length = 10
for i in side:
  angle = (360/side)
    


window.exitonclick()
