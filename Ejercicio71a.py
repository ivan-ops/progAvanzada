#Figura de casa de colores


import turtle
ventana=turtle.Screen ()
ventana.bgcolor('white')
ventana.title('mi ventana')

ivan = turtle.Turtle()
ivan.shape('turtle')
ivan.color('blue')
ivan.pensize(2)
ivan.speed(1)



ivan.pendown()

ivan.forward(80)
ivan.left(90)
ivan.forward(80)
ivan.left(90)
ivan.forward(80)
ivan.left(90)
ivan.forward(80)
ivan.left(90)


ivan.penup()
ivan.forward(20)
ivan.left(90)


ivan.color('red')
ivan.pendown()
ivan.forward(40)
ivan.right(90)
ivan.forward(40)
ivan.right(90)
ivan.forward(40)
ivan.left(90)

ivan.penup()
ivan.forward(20)
ivan.left(90)
ivan.forward(80)

ivan.color('green')
ivan.pendown()
ivan.left(30)
ivan.forward(80)
ivan.left(180)

ivan.penup()
ivan.forward(80)
ivan.left(60)
ivan.left(180)
ivan.forward(80)

ivan.pendown()
ivan.right(120)
ivan.forward(80)
ventana.mainloop()
