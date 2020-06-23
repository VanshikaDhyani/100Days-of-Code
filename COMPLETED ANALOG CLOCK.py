#!/usr/bin/env python
# coding: utf-8

# In[1]:



import time
import turtle
import random
#create object named Leo
Leo= turtle.Screen()
Leo.bgcolor("orange")
Leo.setup(width=600, height=600)
Leo.title("Analog Clock")
Leo.tracer(0)


# In[2]:


#creating object to draw the clock
pen =turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


# In[3]:


#create a function to draw the clock

def draw_clock(hour, minute, second, pen):
    #draw clock face
    pen.up()
    pen.setposition(0,210)
    pen.setheading(180)
    pen.color("white")
    pen.down()
    pen.circle(210)
    
    #draw lines on the face of the clock
    pen.up()
    pen.setposition(0,0)
    pen.setheading(90)
    
    for i in range(12):
        pen.forward(190)
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.setposition(0,0)
        pen.right(30)

    #Draw HOUR hand
    pen.penup()
    pen.setposition(0,0)
    pen.color("white")
    pen.pensize(10)
    pen.setheading(90)
    angle = ((hour/12)*360)
    pen.right(angle)
    pen.pendown()
    pen.forward(50)
    
    
    
    #Draw MINUTE hand
    pen.penup()
    pen.setposition(0,0)
    pen.color("white")
    pen.pensize(4)
    pen.setheading(90)
    angle = ((minute/60)*360)
    pen.right(angle)
    pen.pendown()
    pen.forward(100)
    
    #Draw SECOND hand
    pen.penup()
    pen.setposition(0,0)
    pen.color("white")
    pen.pensize(1)
    pen.setheading(90)
    angle = ((second/60)*360)
    pen.right(angle)
    pen.pendown()
    pen.forward(150)


# In[ ]:


#converting time tuple to a string
#%I will give us the hour and int changes the string to integer value

while True:
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))  #this code displays current time
    second = int(time.strftime("%s"))

    draw_clock(hour, minute, second, pen)
    time.sleep(1)
    pen.clear()


# In[ ]:


draw_clock(hour, minute, second, pen)


# In[ ]:


Leo.mainloop()


# In[ ]:




