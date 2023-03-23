import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Draw lines to create the robot
head = canvas.create_line(250, 100, 250, 150)
body = canvas.create_line(250, 150, 250, 300)
left_arm = canvas.create_line(250, 200, 200, 250)
right_arm = canvas.create_line(250, 200, 300, 250)
left_leg = canvas.create_line(250, 300, 200, 350)
right_leg = canvas.create_line(250, 300, 300, 350)

# Move each line independently to animate the robot
def animate():
    canvas.move(head, 0, 1)
    canvas.move(body, 0, 1)
    canvas.move(left_arm, -1, 0)
    canvas.move(right_arm, 1, 0)
    canvas.move(left_leg, -1, 0)
    canvas.move(right_leg, 1, 0)
    canvas.after(50, animate)

animate()

root.mainloop()