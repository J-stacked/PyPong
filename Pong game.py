from tkinter import *
import random
import time

mode=input("What mode would you like to do, easy(1), meduim(2), hard(3), expert(4), intense(5), super intense(6), or random(7)?")
if mode=="7":
    mode=["1","2","3","4","5","6"]
    random.shuffle(mode)
    mode=mode[0]
if mode=="1":
    k=0.02
elif mode=="2":
    k=0.015
elif mode=="3":
    k=0.01
elif mode=="4":
    k=0.005
elif mode=="5":
    k=0.0025
else:
    k=0.00125
c=input("What color would you like your paddle to be, red(1), blue(2), yellow(3), lime(4), or orange(5)?")
if c=="1":
    c='red'
elif c=="2":
    c='blue'
elif c=="3":
    c='orange'
elif c=="4":
    c='lime green'
else:
    c='orange red'
c2=input("What color would you like your ball to be, red(1), blue(2), yellow(3), lime(4), or orange(5)?")
if c2=="1":
    c2='red'
elif c2=="2":
    c2='blue'
elif c2=="3":
    c2='orange'
elif c2=="4":
    c2='lime green'
else:
    c2='orange red'
print("Please click the pong window.")
hits=0
time.sleep(3)
tk = Tk()
tk.title("Pong v3.2")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=600, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
canvas.configure(background='black')
hit=0
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
            self.x=-1
        if self.hit_paddle(pos) == True:
            self.y = -3
            self.x=-1
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = 3
            self.y=1
        if pos[2] >= self.canvas_width:
            self.x = -3
            
    def hit_paddle(self, pos):
        global hit
        global k
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                hit=hit+1
                if k<.001:
                    k=k
                else:
                    k=k-0.0005
                return True
        return False

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 500)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        
    def turn_left(self, evt):
        self.x = -2
        
    def turn_right(self, evt):
        self.x = 2
        
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
     
paddle = Paddle(canvas, c)
ball = Ball(canvas, paddle, c2)
ball.draw()
paddle.draw()
tk.update_idletasks()
tk.update()
time.sleep(2)
msg=0
while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        break
    font = ("Arial", 24, "bold")
    hits=str(hit)
    m = hits+" hits"
    canvas.delete(msg)
    msg=canvas.create_text(350, 550, text=m, font=font, fill="white")
    tk.update_idletasks()
    tk.update()
    time.sleep(k)
    hits=str(hit)
strk=str(k)
print("You hit the ball "+hits+" time(s) at a delay of "+strk+" seconds between frame updates!")
time.sleep(5)

