import tkinter as tk
import math
import time

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

############# Initial conditions ################

Foot_Xorigin = 250
Foot_Yorigin = 500

Foot_length = 50
Bottom_length = 150
Top_length = 150
r = 50

Foot = canvas.create_line(Foot_Xorigin, Foot_Yorigin, Foot_Xorigin + Foot_length, Foot_Yorigin)
Bottom = canvas.create_line(Foot_Xorigin + 35, Foot_Yorigin, Foot_Xorigin + 30, Foot_Yorigin - Bottom_length)
Top = canvas.create_line(Foot_Xorigin + 30, Foot_Yorigin - Bottom_length, Foot_Xorigin + 50, Foot_Yorigin - 350)
Head = canvas.create_oval(300 - r,150 - r,300 + r,150 + r)

def rotate(goal_angle, line):
    rad = math.radians(goal_angle)
    x1, y1, x2, y2 = canvas.coords(line)
    dx = x2 - x1
    dy = y2 - y1
    new_dx = dx * math.cos(rad) - dy * math.sin(rad)
    new_dy = dx * math.sin(rad) + dy * math.cos(rad)
    new_x2 = x1 + new_dx
    new_y2 = y1 + new_dy

    canvas.coords(line, x1, y1, new_x2, new_y2)

def update(line, line2, x, y):
    x1, y1, x2, y2 = canvas.coords(line)
    x3, y3, x4, y4 = canvas.coords(line2)

    if canvas.type(line2) == 'oval':
        canvas.coords(line2, x2 - r, y2 - r, x2 + r, y2 + r)
    else:
        canvas.coords(line2, x2, y2, x2 + x, y2 + y)
        #canvas.coords(line2, x2, y2, x4, y4)

def animate(angle, x, y):
    rotate(angle, Bottom)
    rotate(-angle,Top)
    update(Bottom, Top, x, y)
    update(Top, Head, x, y)

angle_range = 35.0
angle_speed = -0.5

i = 0
for theta in range(abs(int(angle_range/angle_speed))):
    canvas.update()
    deltaX = Top_length * math.cos(math.radians(-angle_speed * i - 60))
    deltaY = Top_length * math.sin(math.radians(-angle_speed * i - 60))
    canvas.after(30,animate(angle_speed, deltaX, deltaY))
    i = i + 1

root.mainloop()
