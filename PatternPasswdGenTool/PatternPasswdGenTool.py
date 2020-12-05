import turtle
import time


class DrawPasswd:
    def __init__(self, passwd, pen):
        self.pen = pen
        self.passwd = passwd
        self.pen.speed(0)

    def reset(self):
        self.pen.clear()
        self.pen.reset()

    def draw(self):
        self.pen.fd(50)
        self.pen.fd(500)

    def done(self):
        ts = turtle.getscreen()
        print(ts.getcanvas().postscript(file="test.eps"))


drawPasswd = DrawPasswd([1, 2, 3, 4, 5, 6, 7, 8, 9], turtle.Turtle())
drawPasswd.draw()
time.sleep(1)
drawPasswd.done()
