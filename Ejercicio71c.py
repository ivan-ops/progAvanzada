
import turtle
ventana=turtle.Screen ()
ventana.bgcolor('white')
ventana.title('mi ventana')

rafael=turtle.Turtle()
rafael.shape('turtle')
rafael.pensize(2)
rafael.speed(1)

i=1
rafael.penup()
while i<6:
    
    rafael.color('blue')
    rafael.forward(i*90)
    rafael.pendown()

    rafael.forward(80)
    rafael.left(90)
    rafael.forward(80)
    rafael.left(90)
    rafael.forward(80)
    rafael.left(90)
    rafael.forward(80)
    rafael.left(90)

    rafael.penup()
    rafael.forward(20)
    rafael.left(90)

    rafael.color('red')
    rafael.pendown()
    rafael.forward(40)
    rafael.right(90)
    rafael.forward(40)
    rafael.right(90)
    rafael.forward(40)
    rafael.left(90)

    rafael.penup()
    rafael.forward(20)
    rafael.left(90)
    rafael.forward(80)

    rafael.color('green')
    rafael.pendown()
    rafael.left(30)
    rafael.forward(80)
    rafael.left(180)

    rafael.penup()
    rafael.forward(80)
    rafael.left(60)
    rafael.left(180)
    rafael.forward(80)

    rafael.pendown()
    rafael.right(120)
    rafael.forward(80)

    rafael.penup()
    rafael.setpos(0,0)
    rafael.right(60)

    i=i+1
    
rafael.setpos(0,-200)

i=1
rafael.penup()
while i<6:
    
    rafael.color('black')
    rafael.forward(i*90)
    rafael.pendown()

    rafael.forward(80)
    rafael.left(90)
    rafael.forward(80)
    rafael.left(90)
    rafael.forward(80)
    rafael.left(90)
    rafael.forward(80)
    rafael.left(90)

    rafael.penup()
    rafael.forward(20)
    rafael.left(90)

    rafael.color('blue')
    rafael.pendown()
    rafael.forward(40)
    rafael.right(90)
    rafael.forward(40)
    rafael.right(90)
    rafael.forward(40)
    rafael.left(90)

    rafael.penup()
    rafael.forward(20)
    rafael.left(90)
    rafael.forward(80)

    rafael.color('green')
    rafael.pendown()
    rafael.left(30)
    rafael.forward(80)
    rafael.left(180)

    rafael.penup()
    rafael.forward(80)
    rafael.left(60)
    rafael.left(180)
    rafael.forward(80)

    rafael.pendown()
    rafael.right(120)
    rafael.forward(80)

    rafael.penup()
    rafael.setpos(0,-200)
    rafael.right(60)

    i=i+1

ventana.mainloop()