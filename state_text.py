from turtle import Turtle

class StateText(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def show_state(self, x, y, text_input):
        self.goto(x, y)
        self.write(text_input, align="center", font=("Arial", 10, "bold"))
