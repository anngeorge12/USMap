import pandas
import turtle
screen = turtle.Screen()
s = 0
screen.title("US Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
info = pandas.read_csv("50_states.csv")
an = info.state.to_list()
an1 = []
while s != 50:
    ans = turtle.textinput(title=f"Score: {s}/50", prompt="Whats another state?")
    if ans == "Exit":
        break
    c = info[info.state == ans]
    x = c.x
    y = c.y
    if ans in an and ans not in an1:
        an1.append(ans)
        s = s + 1
        new = turtle.Turtle()
        new.ht()
        new.penup()
        new.goto(int(x), int(y))
        new.write(ans)
s = [i for i in an if i not in an1]
print("the states you missed:\n", s)
    

