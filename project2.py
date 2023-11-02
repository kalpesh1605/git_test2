import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor('black')
t.speed(0)

n=200
h=0
for i in range(360):
    c=colorsys.hls_to_rgb(h,1,0.1)
    ht=1/n
    t.color(c)
    t.left(8)
    t.forward(100)
    t.right(175)
    for j in range(4):
        t.forward(i*1)
        t.left(6)

turtle.done()