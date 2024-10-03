import tkinter as tk


cell_size = 15

def create_canvas_grid(canvas, width, height, cell_size):
    for x in range(0, width, cell_size):
        canvas.create_line(x, 0, x, height, fill="black")

    for y in range(0, height, cell_size):
        canvas.create_line(0, y, width, y, fill="black")

app = tk.Tk()
app.title("Canvas Grid")
canvas_area = tk.Canvas(app, bg="white", width=1000, height=800)
canvas_area.pack()

create_canvas_grid(canvas_area, 1000, 800, cell_size)

def grid_coordinates(x, y):
    return x * cell_size, y * cell_size

def fill_square(x, y):
    x1, y1 = grid_coordinates(x, y)
    canvas_area.create_rectangle(x1, y1, x1 + cell_size, y1 + cell_size, fill="black")

#использование алгоритма Брезенхэма


def draw_line_bresenham(x_start, y_start, x_end, y_end):
    delta_x = abs(x_end - x_start)
    delta_y = abs(y_end - y_start)
    step_x = 1 if x_start < x_end else -1
    step_y = 1 if y_start < y_end else -1
    error = delta_x - delta_y

    while True:
        fill_square(x_start, y_start)
        if x_start == x_end and y_start == y_end:
            break
        double_error = 2 * error
        if double_error > -delta_y:
            error -= delta_y
            x_start += step_x
        if double_error < delta_x:
            error += delta_x
            y_start += step_y

def draw_circle_bresenham(center_x, center_y, radius):
    x = 0
    y = radius
    decision_parameter = 3 - 2 * radius

    while x <= y:
        fill_square(center_x + x, center_y + y)
        fill_square(center_x - x, center_y + y)
        fill_square(center_x + x, center_y - y)
        fill_square(center_x - x, center_y - y)
        fill_square(center_x + y, center_y + x)
        fill_square(center_x - y, center_y + x)
        fill_square(center_x + y, center_y - x)
        fill_square(center_x - y, center_y - x)

        x += 1
        if decision_parameter > 0:
            y -= 1
            decision_parameter += 4 * (x - y) + 10
        else:
            decision_parameter += 4 * x + 6

def draw_circle():
    draw_circle_bresenham(45, 35, 15)

def draw_line():
    draw_line_bresenham(2, 5, 30, 30)

line_button = tk.Button(app, text="Draw Line", command=draw_line)
line_button.pack(side=tk.LEFT, padx=10, pady=10)

circle_button = tk.Button(app, text="Draw Circle", command=draw_circle)
circle_button.pack(side=tk.LEFT, padx=10, pady=10)

app.mainloop()
