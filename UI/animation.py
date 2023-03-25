import tkinter as tk
import math
import time

root = tk.Tk()

# Set window width and height
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

############# Initial conditions ################

Foot_Xorigin = 250
Foot_Yorigin = 480

Foot_length = 50
Bottom_length = 150
Top_length = 150
r = 50

Foot = canvas.create_line(Foot_Xorigin, Foot_Yorigin, Foot_Xorigin + Foot_length, Foot_Yorigin)
Bottom = canvas.create_line(Foot_Xorigin + 35, Foot_Yorigin, Foot_Xorigin + 30, Foot_Yorigin - Bottom_length)
Top = canvas.create_line(Foot_Xorigin + 30, Foot_Yorigin - Bottom_length, Foot_Xorigin + 50, Foot_Yorigin - 350)
Head = canvas.create_oval(300 - r,150 - r,300 + r,150 + r, fill = "black")

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

def crouch(angle, x, y):
    rotate(angle, Bottom)
    rotate(angle,Top)
    update(Bottom, Top, x, y)
    update(Top, Head, x, y)

def jump(dx, dy):
    x1, y1, x2, y2 = canvas.coords(Foot)
    x3, y3, x4, y4 = canvas.coords(Bottom)
    x5, y5, x6, y6 = canvas.coords(Top)
    x7, y7, x8, y8 = canvas.coords(Head)

    canvas.coords(Foot, x1 + dx, y1 + dy, x2 + dx, y2 + dy)
    canvas.coords(Bottom, x3 + dx, y3 + dy, x4 + dx, y4 + dy)
    canvas.coords(Top, x5 + dx, y5 + dy, x6 + dx, y6 + dy)
    canvas.coords(Head, x7 + dx, y7 + dy, x8 + dx, y8 + dy)

angle_range_down = 45
angle_range_up = 55
angle_speed_down = -0.25
angle_speed_up = 10
canvas.create_rectangle(0, 500, 500, 482, fill="blue")
i = 0
for theta in range(abs(int(angle_range_down/angle_speed_down))):
    canvas.update()
    deltaX = Top_length * math.cos(math.radians(-angle_speed_down * i - 60))
    deltaY = Top_length * math.sin(math.radians(-angle_speed_down * i - 60))
    canvas.after(5,crouch(angle_speed_down, deltaX, deltaY))
    i = i + 1

i = 0
for theta in range(abs(int(angle_range_up/angle_speed_up))):
    canvas.update()
    deltaX = Top_length * math.cos(math.radians(-angle_speed_up * i - 30))
    deltaY = Top_length * math.sin(math.radians(-angle_speed_up * i - 30))
    canvas.after(30,crouch(angle_speed_up, deltaX, deltaY))
    i = i + 1
    canvas.after(5, jump(-0.5, -12))


i = 0
for theta in range(abs(int(15/-2))):
    canvas.update()
    deltaX = Top_length * math.cos(math.radians(-angle_speed_down * i -70))
    deltaY = Top_length * math.sin(math.radians(-angle_speed_down * i -70))
    canvas.after(30,crouch(-3, deltaX, deltaY))
    i = i + 1
    canvas.after(5, jump(-0.5, 8.5))

root.mainloop()
