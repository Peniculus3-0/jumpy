import customtkinter
#import tkinter as tk
import math
import time


class animation(customtkinter.CTkFrame):

    def __init__(self, *args, header_name="Animation", **kwargs):
        super().__init__(*args, **kwargs)

        #self.root = tk.Tk()
        self.header_name = header_name
        self.canvas = customtkinter.CTkCanvas(self, width=500, height=500, bg='white')  # Set window width and height
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        #self.canvas.pack()

        self.angle_goal_Tibia = 20  # degrees
        self.angle_goal_Humerus = 20  # degrees
        self.Overshoot_angle = 85  # degrees
        self.Height_goal = 50  # pixels
        self.refresh_rate = 60  # Hz
        self.refresh_delay = 0.01  # seconds

        Foot_Xorigin = 250  # pixels
        Foot_Yorigin = 480  # pixels
        Foot_length = 100  # pixels
        self.Tibia_length = 150  # pixels
        self.Tibia_angle = 20  # degrees
        self.Humerus_angle = 20  # degrees
        self.Humerus_length = 150  # pixels
        self.Head_radius = 40  # pixels

        self.Foot = self.canvas.create_line(Foot_Xorigin, Foot_Yorigin, Foot_Xorigin + Foot_length, Foot_Yorigin)
        self.Tibia = self.canvas.create_line(Foot_Xorigin + (Foot_length / 2), Foot_Yorigin,
                                        Foot_Xorigin + (Foot_length / 2) - (
                                                    self.Tibia_length * math.cos(math.radians(90 - self.Tibia_angle))),
                                        Foot_Yorigin - (self.Tibia_length * math.sin(math.radians(90 - self.Tibia_angle))))
        self.Humerus = self.canvas.create_line(
            Foot_Xorigin + (Foot_length / 2) - (self.Tibia_length * math.cos(math.radians(90 - self.Tibia_angle))),
            Foot_Yorigin - (self.Tibia_length * math.sin(math.radians(90 - self.Tibia_angle))),
            Foot_Xorigin + (Foot_length / 2) - (self.Tibia_length * math.cos(math.radians(90 - self.Tibia_angle))) + (
                        self.Humerus_length * math.cos(math.radians(90 - self.Humerus_angle))),
            Foot_Yorigin - (self.Tibia_length * math.sin(math.radians(90 - self.Tibia_angle))) - (
                        self.Humerus_length * math.sin(math.radians(90 - self.Humerus_angle))))
        self.Head = self.canvas.create_oval(
            Foot_Xorigin + (Foot_length / 2) - (self.Tibia_length * math.cos(math.radians(90 - self.Tibia_angle))) + (
                        self.Humerus_length * math.cos(math.radians(90 - self.Humerus_angle))) - self.Head_radius,
            Foot_Yorigin - (self.Tibia_length * math.sin(math.radians(90 - self.Tibia_angle))) - (
                        self.Humerus_length * math.sin(math.radians(90 - self.Humerus_angle))) - self.Head_radius,
            Foot_Xorigin + (Foot_length / 2) - (self.Tibia_length * math.cos(math.radians(90 - self.Tibia_angle))) + (
                        self.Humerus_length * math.cos(math.radians(90 - self.Humerus_angle))) + self.Head_radius,
            Foot_Yorigin - (self.Tibia_length * math.sin(math.radians(90 - self.Tibia_angle))) - (
                        self.Humerus_length * math.sin(math.radians(90 - self.Humerus_angle))) + self.Head_radius, fill="black")

    def rotate(self, goal_angle, line):
        rad = math.radians(goal_angle)
        #x1, y1, x2, y2 = self.canvas.coords(line)
        coords = self.canvas.coords(line)
        dx = coords[2] - coords[0]
        dy = coords[3] - coords[1]
        new_dx = dx * math.cos(rad) - dy * math.sin(rad)
        new_dy = dx * math.sin(rad) + dy * math.cos(rad)
        new_x2 = coords[0] + new_dx
        new_y2 = coords[1] + new_dy

    def updateRobot(self):
        x1, y1, x2, y2 = canvas.coords(self.Foot)
        x3, y3, x4, y4 = canvas.coords(self.Tibia)
        x5, y5, x6, y6 = canvas.coords(self.Humerus)
        m3 = (y6 - y5) / (x6 - x5)

        angle = -math.atan(abs(m3))

        canvas.coords(self.Tibia, x1 + (x2 - x1) / 2, y1, x4, y4)
        canvas.coords(Humerus, x4, y4, x4 + (math.cos(angle) * Humerus_length), y4 + (math.sin(angle) * Humerus_length))
        canvas.coords(Head, x6 - Head_radius, y6 - Head_radius, x6 + Head_radius, y6 + Head_radius)

    def routine1(self, time1, rate):

        w1 = (self.angle_goal_Tibia - (90 - self.Tibia_angle)) / time1
        w2 = (self.angle_goal_Humerus - (90 - self.Humerus_angle)) / time1

        for theta in range(int(rate * time1)):
            self.canvas.update()
            animation.rotate(self, w1 / rate, self.Tibia)
            animation.rotate(self, -w2 / rate, self.Humerus)
            animation.updateRobot(self)
            time.sleep(1 / rate - refresh_delay)

    def routine2(self, time1, rate):

        dy = Height_goal / (rate * time1)
        w1 = (Overshoot_angle - 20) / time1
        w2 = (Overshoot_angle - 20) / time1

        for theta in range(int(rate * time1)):
            self.canvas.update(self)
            animation.rotate(self, w1 / rate, Tibia)
            animation.rotate(self, -w2 / rate, Humerus)

            ## Y-axis MOTION ##
            x1, y1, x2, y2 = canvas.coords(Foot)
            x3, y3, x4, y4 = canvas.coords(Tibia)
            x5, y5, x6, y6 = canvas.coords(Humerus)
            x7, y7, x8, y8 = canvas.coords(Head)
            self.canvas.coords(Foot, x1, y1 - dy, x2, y2 - dy)
            self.canvas.coords(Tibia, x3, y3 - dy, x4, y4 - dy)
            self.canvas.coords(Humerus, x5, y5 - dy, x6, y6 - dy)
            self.canvas.coords(Head, x7, y7 - dy, x8, y8 - dy)

            animation.updateRobot(self)
            time.sleep(1 / rate - refresh_delay)

    def routine3(self, time1, rate):

        dy = Height_goal / (rate * time1)

        for theta in range(int(rate * time1)):
            self.canvas.update(self)

            ## Y-axis MOTION ##
            x1, y1, x2, y2 = canvas.coords(Foot)
            x3, y3, x4, y4 = canvas.coords(Tibia)
            x5, y5, x6, y6 = canvas.coords(Humerus)
            x7, y7, x8, y8 = canvas.coords(Head)
            self.canvas.coords(Foot, x1, y1 + dy, x2, y2 + dy)
            self.canvas.coords(Tibia, x3, y3 + dy, x4, y4 + dy)
            self.canvas.coords(Humerus, x5, y5 + dy, x6, y6 + dy)
            self.canvas.coords(Head, x7, y7 + dy, x8, y8 + dy)

            animation.updateRobot(self)
            time.sleep(1 / rate - refresh_delay)

    def animate(self, time):
        #canvas.setup()
        animation.routine1(self, time[0], self.refresh_rate)
        animation.routine2(self, time[1], self.refresh_rate)
        animation.routine3(self, time[2], self.refresh_rate)
        root.mainloop()

    def execution(self):
        animation.animate(self, [10, 0.5, 0.5])