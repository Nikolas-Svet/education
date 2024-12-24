import tkinter as tk
import math

cell_size = 15

# Инициализация координат пирамиды
pyramid = [
    [0, 0, 0],    # Нижняя точка 1
    [4, 0, 0],    # Нижняя точка 2
    [4, 4, 0],    # Нижняя точка 3
    [0, 4, 0],    # Нижняя точка 4
    [2, 2, 4]     # Вершина пирамиды
]

# Функции для матриц поворота
def rotate_x(point, angle):
    x, y, z = point
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    y_new = y * cos_a - z * sin_a
    z_new = y * sin_a + z * cos_a
    return [x, y_new, z_new]

def rotate_y(point, angle):
    x, y, z = point
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    x_new = x * cos_a + z * sin_a
    z_new = -x * sin_a + z * cos_a
    return [x_new, y, z]

def rotate_z(point, angle):
    x, y, z = point
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    x_new = x * cos_a - y * sin_a
    y_new = x * sin_a + y * cos_a
    return [x_new, y_new, z]

# Проекция 3D в 2D для отрисовки
def project_3d_to_2d(point):
    x, y, z = point
    scale = 50 / (z + 10)  # Простая перспектива
    x_proj = int(500 + scale * x * cell_size)
    y_proj = int(400 - scale * y * cell_size)
    return x_proj, y_proj

# Отрисовка пирамиды
def draw_pyramid(points):
    canvas_area.delete("all")
    create_canvas_grid(canvas_area, 1000, 800, cell_size)

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Основание
        (0, 4), (1, 4), (2, 4), (3, 4)   # Рёбра к вершине
    ]

    for edge in edges:
        start, end = edge
        x1, y1 = project_3d_to_2d(points[start])
        x2, y2 = project_3d_to_2d(points[end])
        canvas_area.create_line(x1, y1, x2, y2, fill="black")

# Обработка вращения
current_angle_x = 0
current_angle_y = 0
current_angle_z = 0

def rotate_pyramid(axis):
    global pyramid, current_angle_x, current_angle_y, current_angle_z

    if axis == 'x':
        current_angle_x += math.radians(10)
        pyramid = [rotate_x(point, math.radians(10)) for point in pyramid]
    elif axis == 'y':
        current_angle_y += math.radians(10)
        pyramid = [rotate_y(point, math.radians(10)) for point in pyramid]
    elif axis == 'z':
        current_angle_z += math.radians(10)
        pyramid = [rotate_z(point, math.radians(10)) for point in pyramid]

    draw_pyramid(pyramid)

# Создание сетки
def create_canvas_grid(canvas, width, height, cell_size):
    for x in range(0, width, cell_size):
        canvas.create_line(x, 0, x, height, fill="gray", dash=(2, 2))

    for y in range(0, height, cell_size):
        canvas.create_line(0, y, width, y, fill="gray", dash=(2, 2))

# Интерфейс приложения
app = tk.Tk()
app.title("3D Pyramid Rotation")
canvas_area = tk.Canvas(app, bg="white", width=1000, height=800)
canvas_area.pack()

create_canvas_grid(canvas_area, 1000, 800, cell_size)

def reset_pyramid():
    global pyramid
    pyramid = [
        [0, 0, 0],
        [4, 0, 0],
        [4, 4, 0],
        [0, 4, 0],
        [2, 2, 4]
    ]
    draw_pyramid(pyramid)

reset_button = tk.Button(app, text="Reset", command=reset_pyramid)
reset_button.pack(side=tk.LEFT, padx=10, pady=10)

rotate_x_button = tk.Button(app, text="Rotate X", command=lambda: rotate_pyramid('x'))
rotate_x_button.pack(side=tk.LEFT, padx=10, pady=10)

rotate_y_button = tk.Button(app, text="Rotate Y", command=lambda: rotate_pyramid('y'))
rotate_y_button.pack(side=tk.LEFT, padx=10, pady=10)

rotate_z_button = tk.Button(app, text="Rotate Z", command=lambda: rotate_pyramid('z'))
rotate_z_button.pack(side=tk.LEFT, padx=10, pady=10)

# Инициализация
draw_pyramid(pyramid)
app.mainloop()