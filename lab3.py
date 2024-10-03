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

# Алгоритм Брезенхэма для рисования линии
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

line_coords = {'start_x': 2, 'start_y': 5, 'end_x': 30, 'end_y': 30}
circle_coords = {'center_x': 45, 'center_y': 35, 'radius': 10}

def draw_line():
    draw_line_bresenham(line_coords['start_x'], line_coords['start_y'],
                        line_coords['end_x'], line_coords['end_y'])

def draw_circle():
    draw_circle_bresenham(circle_coords['center_x'], circle_coords['center_y'],
                          circle_coords['radius'])

def move_line(dx, dy):
    canvas_area.delete("all")
    create_canvas_grid(canvas_area, 1000, 800, cell_size)

    line_coords['start_x'] += dx
    line_coords['start_y'] += dy
    line_coords['end_x'] += dx
    line_coords['end_y'] += dy

    draw_line()
    draw_circle()

def move_circle(dx, dy):
    canvas_area.delete("all")
    create_canvas_grid(canvas_area, 1000, 800, cell_size)

    circle_coords['center_x'] += dx
    circle_coords['center_y'] += dy

    draw_circle()
    draw_line()

line_button = tk.Button(app, text="Draw Line", command=draw_line)
line_button.pack(side=tk.LEFT, padx=10, pady=10)

circle_button = tk.Button(app, text="Draw Circle", command=draw_circle)
circle_button.pack(side=tk.LEFT, padx=10, pady=10)

# Кнопки для перемещения линии
move_line_up_button = tk.Button(app, text="Move Line Up", command=lambda: move_line(0, -1))
move_line_up_button.pack(side=tk.LEFT, padx=10, pady=10)

move_line_down_button = tk.Button(app, text="Move Line Down", command=lambda: move_line(0, 1))
move_line_down_button.pack(side=tk.LEFT, padx=10, pady=10)

move_line_left_button = tk.Button(app, text="Move Line Left", command=lambda: move_line(-1, 0))
move_line_left_button.pack(side=tk.LEFT, padx=10, pady=10)

move_line_right_button = tk.Button(app, text="Move Line Right", command=lambda: move_line(1, 0))
move_line_right_button.pack(side=tk.LEFT, padx=10, pady=10)

# Кнопки для перемещения окружности
move_circle_up_button = tk.Button(app, text="Move Circle Up", command=lambda: move_circle(0, -1))
move_circle_up_button.pack(side=tk.LEFT, padx=10, pady=10)

move_circle_down_button = tk.Button(app, text="Move Circle Down", command=lambda: move_circle(0, 1))
move_circle_down_button.pack(side=tk.LEFT, padx=10, pady=10)

move_circle_left_button = tk.Button(app, text="Move Circle Left", command=lambda: move_circle(-1, 0))
move_circle_left_button.pack(side=tk.LEFT, padx=10, pady=10)

move_circle_right_button = tk.Button(app, text="Move Circle Right", command=lambda: move_circle(1, 0))
move_circle_right_button.pack(side=tk.LEFT, padx=10, pady=10)

app.mainloop()
