import tkinter
import time

Window_Width = 1000

Window_Height = 600

Ball_Start_XPosition = 50

Ball_Start_YPosition = 50

Ball_Radius = 30

Ball_min_movement = 5

Refresh_Sec = 0.01

head_coord_x1
head_coord_x2

def create_animation_window():
    Window = tkinter.Tk()
    Window.title("Animation")

    Window.geometry(f'{Window_Width}x{Window_Height}')
    return Window


def create_animation_canvas(Window):
    canvas = tkinter.Canvas(Window)
    canvas.configure(bg="Blue", height=500, width=500)
    canvas.pack(side="bottom")
    canvas.create_line(100, 200, 200, 35, fill="green", width=25)
    canvas.create_line(100, 200, 50, 35, fill="green", width=25)
    return canvas


def animate_ball(Window, canvas, xinc, yinc):
    ball = canvas.create_rectangle(Ball_Start_XPosition - Ball_Radius,
                              Ball_Start_YPosition - Ball_Radius,
                              Ball_Start_XPosition + Ball_Radius,
                              Ball_Start_YPosition + Ball_Radius,
                              fill="Red", outline="Black", width=4)
    while True:
        canvas.move(ball, xinc, yinc)
        Window.update()
        time.sleep(Refresh_Sec)
        ball_pos = canvas.coords(ball)
        # unpack array to variables
        al, bl, ar, br = ball_pos
        if al < abs(xinc) or ar > 500 - abs(xinc):
            xinc = -xinc
        if bl < abs(yinc) or br > 500 - abs(yinc):
            yinc = -yinc


Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)
animate_ball(Animation_Window, Animation_canvas, Ball_min_movement, Ball_min_movement)