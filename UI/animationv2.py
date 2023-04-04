
import customtkinter
import math
import time

class canvas(customtkinter.CTkFrame):
   def __init__(self, *args, header_name="Animation", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name
        canvas = customtkinter.CTkCanvas(self, width=500, height=500, bg='white') # Set window width and height
        canvas.grid(row=0, column=0, padx=10, pady=10)
        
        

        self.angle_goal_Tibia = 20 #degrees
        self.angle_goal_Humerus = 20  #degrees
        self.Overshoot_angle = 85 #degrees
        self.Height_goal = 50 #pixels

        Foot_Xorigin = 250 #pixels
        Foot_Yorigin = 480 #pixels
        Foot_length = 100 #pixels
        self.Tibia_length = 150 #pixels
        self.Tibia_angle = 20 #degrees
        self.Humerus_angle = 20 #degrees
        self.Humerus_length = 150 #pixels
        self.Head_radius = 40 #pixels

    #     self.Foot = canvas.create_line(Foot_Xorigin, Foot_Yorigin, Foot_Xorigin + Foot_length, Foot_Yorigin)
    #     self.Tibia = canvas.create_line(Foot_Xorigin + (Foot_length/2), Foot_Yorigin, Foot_Xorigin + (Foot_length/2) - (Tibia_length * math.cos(math.radians(90 - Tibia_angle))), Foot_Yorigin - (Tibia_length * math.sin(math.radians(90 - Tibia_angle))))
    #     self.Humerus = canvas.create_line(Foot_Xorigin + (Foot_length/2) - (Tibia_length * math.cos(math.radians(90 - Tibia_angle))), Foot_Yorigin - (Tibia_length * math.sin(math.radians(90 - Tibia_angle))), Foot_Xorigin + (Foot_length/2) - (Tibia_length * math.cos(math.radians(90 - Tibia_angle))) + (Humerus_length * math.cos(math.radians(90 - Humerus_angle))), Foot_Yorigin - (Tibia_length * math.sin(math.radians(90 - Tibia_angle))) - (Humerus_length * math.sin(math.radians(90 - Humerus_angle))))
    #     self.Head = canvas.create_oval(Foot_Xorigin + (Foot_length/2) - (Tibia_length * math.cos(math.radians(90 - Tibia_angle))) + (Humerus_length * math.cos(math.radians(90 - Humerus_angle))) - Head_radius, Foot_Yorigin - (Tibia_length * math.sin(math.radians(90 - Tibia_angle))) - (Humerus_length * math.sin(math.radians(90 - Humerus_angle))) - Head_radius, Foot_Xorigin + (Foot_length/2) - (Tibia_length * math.cos(math.radians(90 - Tibia_angle))) + (Humerus_length * math.cos(math.radians(90 - Humerus_angle))) + Head_radius, Foot_Yorigin - (Tibia_length * math.sin(math.radians(90 - Tibia_angle))) - (Humerus_length * math.sin(math.radians(90 - Humerus_angle))) + Head_radius, fill="black")

    # def rotate(goal_angle, line):
    #     rad = math.radians(goal_angle)
    #     x1, y1, x2, y2 = canvas.coords(line)
    #     dx = x2 - x1
    #     dy = y2 - y1
    #     new_dx = dx * math.cos(rad) - dy * math.sin(rad)
    #     new_dy = dx * math.sin(rad) + dy * math.cos(rad)
    #     new_x2 = x1 + new_dx
    #     new_y2 = y1 + new_dy

    # def update(self):
    #     x1, y1, x2, y2 = canvas.coords(self.Foot)
    #     x3, y3, x4, y4 = canvas.coords(self.Tibia)
    #     x5, y5, x6, y6 = canvas.coords(self.Humerus)
    #     m3 = (y6-y5)/(x6-x5)

    #     angle = -math.atan(abs(m3))

    #     canvas.coords(self.Tibia, x1 + (x2 - x1)/2, y1, x4, y4)
    #     canvas.coords(Humerus, x4, y4, x4 + (math.cos(angle)*Humerus_length), y4 + (math.sin(angle)*Humerus_length))
    #     canvas.coords(Head, x6 - Head_radius, y6 - Head_radius, x6 + Head_radius, y6 + Head_radius)
def print():
        print("Hello")