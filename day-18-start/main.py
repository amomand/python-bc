from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("dark green")

<<<<<<< HEAD
for i in range(4):
    tim.forward(100)
    tim.right(90)
=======
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


for i in range(300):
    tim.color(random_colour())
    tim.pensize(10)
    random_walk()

def draw_circles(number):
    for i in range(number):
        # tim.color((random_colour()))
        tim.circle(100)
        tim.left(360/number)

# draw_circles(100)
>>>>>>> hurst-painting


screen = Screen()
screen.exitonclick()

import heroes
print(heroes.gen())