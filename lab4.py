import tkinter as tk
import math

cell_size = 15
window_width = 1400
window_height = 900

clip_window = {
    'x_min': 10, 'y_min': 10,
    'x_max': 50, 'y_max': 50
}

triangle_coords = [
    {'x': 25, 'y': 40},
    {'x': 35, 'y': 20},
    {'x': 45, 'y': 40}
]

def create_canvas_grid(canvas, width, height, cell_size):
    for x in range(0, width, cell_size):
        canvas.create_line(x, 0, x, height, fill="black")
    for y in range(0, height, cell_size):
        canvas.create_line(0, y, width, y, fill="black")

def grid_coordinates(x, y):
    return x * cell_size, y * cell_size

def fill_square(x, y, color="black"):
    x1, y1 = grid_coordinates(x, y)
    canvas_area.create_rectangle(x1, y1, x1 + cell_size, y1 + cell_size, fill=color)

def draw_line_bresenham(x_start, y_start, x_end, y_end, color="black"):
    delta_x = abs(x_end - x_start)
    delta_y = abs(y_end - y_start)
    step_x = 1 if x_start < x_end else -1
    step_y = 1 if y_start < y_end else -1
    error = delta_x - delta_y

    while True:
        if clip_window['x_min'] < x_start < clip_window['x_max'] and clip_window['y_min'] < y_start < clip_window['y_max']:
            fill_square(x_start, y_start, color)
        if x_start == x_end and y_start == y_end:
            break
        double_error = 2 * error
        if double_error > -delta_y:
            error -= delta_y
            x_start += step_x
        if double_error < delta_x:
            error += delta_x
            y_start += step_y

def draw_triangle():
    draw_line_bresenham(triangle_coords[0]['x'], triangle_coords[0]['y'],
                        triangle_coords[1]['x'], triangle_coords[1]['y'])
    draw_line_bresenham(triangle_coords[1]['x'], triangle_coords[1]['y'],
                        triangle_coords[2]['x'], triangle_coords[2]['y'])
    draw_line_bresenham(triangle_coords[2]['x'], triangle_coords[2]['y'],
                        triangle_coords[0]['x'], triangle_coords[0]['y'])

def move_triangle(dx, dy):
    canvas_area.delete("all")
    create_canvas_grid(canvas_area, window_width, window_height, cell_size)
    draw_clip_window()

    for coord in triangle_coords:
        coord['x'] += dx
        coord['y'] += dy

    draw_triangle()

def rotate_triangle(angle):
    canvas_area.delete("all")
    create_canvas_grid(canvas_area, window_width, window_height, cell_size)
    draw_clip_window()

    angle = math.radians(angle)
    cx = sum(point['x'] for point in triangle_coords) / 3
    cy = sum(point['y'] for point in triangle_coords) / 3

    for coord in triangle_coords:
        x_new = (coord['x'] - cx) * math.cos(angle) - (coord['y'] - cy) * math.sin(angle) + cx
        y_new = (coord['x'] - cx) * math.sin(angle) + (coord['y'] - cy) * math.cos(angle) + cy
        coord['x'], coord['y'] = round(x_new), round(y_new)

    draw_triangle()

def scale_triangle(factor):
    canvas_area.delete("all")
    create_canvas_grid(canvas_area, window_width, window_height, cell_size)
    draw_clip_window()

    cx = sum(point['x'] for point in triangle_coords) / 3
    cy = sum(point['y'] for point in triangle_coords) / 3

    for coord in triangle_coords:
        coord['x'] = round(cx + (coord['x'] - cx) * factor)
        coord['y'] = round(cy + (coord['y'] - cy) * factor)

    draw_triangle()

def draw_clip_window():
    for x in range(clip_window['x_min'], clip_window['x_max'] + 1):
        for y in [clip_window['y_min'], clip_window['y_max']]:
            fill_square(x, y, "blue")
    for y in range(clip_window['y_min'], clip_window['y_max'] + 1):
        for x in [clip_window['x_min'], clip_window['x_max']]:
            fill_square(x, y, "blue")

app = tk.Tk()
app.title("Canvas Grid")
canvas_area = tk.Canvas(app, bg="white", width=window_width, height=window_height)
canvas_area.pack()

create_canvas_grid(canvas_area, window_width, window_height, cell_size)
draw_clip_window()
draw_triangle()

move_up_button = tk.Button(app, text="Move Up", command=lambda: move_triangle(0, -1))
move_up_button.pack(side=tk.LEFT, padx=5, pady=5)

move_down_button = tk.Button(app, text="Move Down", command=lambda: move_triangle(0, 1))
move_down_button.pack(side=tk.LEFT, padx=5, pady=5)

move_left_button = tk.Button(app, text="Move Left", command=lambda: move_triangle(-1, 0))
move_left_button.pack(side=tk.LEFT, padx=5, pady=5)

move_right_button = tk.Button(app, text="Move Right", command=lambda: move_triangle(1, 0))
move_right_button.pack(side=tk.LEFT, padx=5, pady=5)

rotate_left_button = tk.Button(app, text="Rotate Left", command=lambda: rotate_triangle(-10))
rotate_left_button.pack(side=tk.LEFT, padx=5, pady=5)

rotate_right_button = tk.Button(app, text="Rotate Right", command=lambda: rotate_triangle(10))
rotate_right_button.pack(side=tk.LEFT, padx=5, pady=5)

scale_up_button = tk.Button(app, text="Scale Up", command=lambda: scale_triangle(1.1))
scale_up_button.pack(side=tk.LEFT, padx=5, pady=5)

scale_down_button = tk.Button(app, text="Scale Down", command=lambda: scale_triangle(0.9))
scale_down_button.pack(side=tk.LEFT, padx=5, pady=5)

app.mainloop()
