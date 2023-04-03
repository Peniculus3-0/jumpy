import tkinter as tk
import math
import time
def setup():

    global root
    root = tk.Tk()

    ## MOTION SETTINGS ##

    global angle_goal_Tibia, angle_goal_Humerus, Height_goal, Overshoot_angle
    angle_goal_Tibia = 20 #degrees
    angle_goal_Humerus = 20  #degrees
    Overshoot_angle = 85 #degrees
    Height_goal = 50 #pixels

    ## REFRESH RATE SETTINGS ##

    global refresh_delay, refresh_rate
    refresh_rate = 60 #Hz
    refresh_delay = 0.01 #seconds

    ## WINDOWS SETTINGS ##

    global canvas
    canvas = tk.Canvas(root, width=500, height=500, bg='white') # Set window width and height
    canvas.pack()
    root.geometry("%dx%d" % (canvas.winfo_width(), canvas.winfo_height()))  # Set the window size to the widget size

    ## ROBOT DEFINITION ##

    global Foot_length, Tibia_length, Tibia_angle, Humerus_angle, Humerus_length, Head_radius
    Foot_Xorigin = 250 #pixels
    Foot_Yorigin = 480 #pixels
    Foot_length = 100 #pixels
    Tibia_length = 150 #pixels
    Tibia_angle = 20 #degrees
    Humerus_angle = 20 #degrees
    Humerus_length = 150 #pixels
    Head_radius = 40 #pixels

    global Foot, Tibia, Humerus, Head

    Foot = canvas.create_line(Foot_Xorigin, Foot_Yorigin, Foot_Xorigin + Foot_length, Foot_Yorigin)
    Tibia = canvas.create_line(Foot_Xorigin + (Foot_length/2), Foot_Yorigin, Foot_Xorigin + (Foot_length/2) - (Tibia_length * math.cos(math.radians(90 - Tibia_angle))), Foot_Yorigin - (Tibia_length * math.sin(math.radians(90 - Tibia_angle))))
    Humerus = canvas.create_line(Foot_Xorigin + (Foot_length/2) - (Tibia_length * math.cos(math.radians(90 - Tibia_angle))), Foot_Yorigin - (Tibia_length * math.sin(math.radians(90 - Tibia_angle))), Foot_Xorigin + (Foot_length/2) - (Tibia_length * math.cos(math.radians(90 - Tibia_angle))) + (Humerus_length * math.cos(math.radians(90 - Humerus_angle))), Foot_Yorigin - (Tibia_length * math.sin(math.radians(90 - Tibia_angle))) - (Humerus_length * math.sin(math.radians(90 - Humerus_angle))))
    Head = canvas.create_oval(Foot_Xorigin + (Foot_length/2) - (Tibia_length * math.cos(math.radians(90 - Tibia_angle))) + (Humerus_length * math.cos(math.radians(90 - Humerus_angle))) - Head_radius, Foot_Yorigin - (Tibia_length * math.sin(math.radians(90 - Tibia_angle))) - (Humerus_length * math.sin(math.radians(90 - Humerus_angle))) - Head_radius, Foot_Xorigin + (Foot_length/2) - (Tibia_length * math.cos(math.radians(90 - Tibia_angle))) + (Humerus_length * math.cos(math.radians(90 - Humerus_angle))) + Head_radius, Foot_Yorigin - (Tibia_length * math.sin(math.radians(90 - Tibia_angle))) - (Humerus_length * math.sin(math.radians(90 - Humerus_angle))) + Head_radius, fill="black")

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

def update():
    x1, y1, x2, y2 = canvas.coords(Foot)
    x3, y3, x4, y4 = canvas.coords(Tibia)
    x5, y5, x6, y6 = canvas.coords(Humerus)
    m3 = (y6-y5)/(x6-x5)

    angle = -math.atan(abs(m3))

    canvas.coords(Tibia, x1 + (x2 - x1)/2, y1, x4, y4)
    canvas.coords(Humerus, x4, y4, x4 + (math.cos(angle)*Humerus_length), y4 + (math.sin(angle)*Humerus_length))
    canvas.coords(Head, x6 - Head_radius, y6 - Head_radius, x6 + Head_radius, y6 + Head_radius)
def routine1(time1, rate):

    w1 = (angle_goal_Tibia - (90 - Tibia_angle)) / time1
    w2 = (angle_goal_Humerus - (90 - Humerus_angle)) / time1

    for theta in range(int(rate*time1)):
        canvas.update()
        rotate(w1 / rate, Tibia)
        rotate(-w2 / rate, Humerus)
        update()
        time.sleep(1/rate - refresh_delay)

def routine2(time1,rate):

    dy = Height_goal/(rate*time1)
    w1 = (Overshoot_angle - 20) / time1
    w2 = (Overshoot_angle - 20) / time1

    for theta in range(int(rate*time1)):
        canvas.update()
        rotate(w1 / rate, Tibia)
        rotate(-w2 / rate, Humerus)

        ## Y-axis MOTION ##
        x1, y1, x2, y2 = canvas.coords(Foot)
        x3, y3, x4, y4 = canvas.coords(Tibia)
        x5, y5, x6, y6 = canvas.coords(Humerus)
        x7, y7, x8, y8 = canvas.coords(Head)
        canvas.coords(Foot, x1, y1 - dy, x2, y2 - dy)
        canvas.coords(Tibia, x3, y3 - dy, x4, y4 - dy)
        canvas.coords(Humerus, x5, y5 - dy, x6, y6 - dy)
        canvas.coords(Head, x7, y7 - dy, x8, y8 - dy)

        update()
        time.sleep(1 / rate - refresh_delay)

def routine3(time1,rate):

    dy = Height_goal/(rate*time1)

    for theta in range(int(rate*time1)):
        canvas.update()

        ## Y-axis MOTION ##
        x1, y1, x2, y2 = canvas.coords(Foot)
        x3, y3, x4, y4 = canvas.coords(Tibia)
        x5, y5, x6, y6 = canvas.coords(Humerus)
        x7, y7, x8, y8 = canvas.coords(Head)
        canvas.coords(Foot, x1, y1 + dy, x2, y2 + dy)
        canvas.coords(Tibia, x3, y3 + dy, x4, y4 + dy)
        canvas.coords(Humerus, x5, y5 + dy, x6, y6 + dy)
        canvas.coords(Head, x7, y7 + dy, x8, y8 + dy)

        update()
        time.sleep(1/rate - refresh_delay)
def animate(time):
    setup()
    routine1(time[0],refresh_rate)
    routine2(time[1],refresh_rate)
    #routine3(time[2],refresh_rate)
    root.mainloop()

# Time of execution of each routine in numerical order
animate([10,0.5,0.5])
