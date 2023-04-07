#code for the demonstration of event driven programming
#onkey events using turtle
# import package
import turtle


def fxn():
	turtle.forward(20)
	
def fxn1():
	turtle.right(90)

def fxn2():
	turtle.left(90)
	

sc=turtle.Screen()
sc.setup(500,300)


turtle.onkey(fxn,'space')
turtle.onkey(fxn1,'Right')
turtle.onkey(fxn2,'Left')



turtle.listen()


