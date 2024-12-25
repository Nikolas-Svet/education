import tkinter as tk
import numpy as np
import math

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=600, bg='white')
canvas.pack()

center_x, center_y = 300, 300
scale = 100
pixel_size = 10

#коорд пирамиды
pyramid = np.array([
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [0, 0, 1]
])

#ребра пирамиды (индексы вершин)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  #основ
    (0, 4), (1, 4), (2, 4), (3, 4)   #рёбра
]

# из 3D в 2D
def project(point):
    x, y, z = point
    projected_x = int(center_x + x * scale)
    projected_y = int(center_y - y * scale)
    return projected_x, projected_y

def draw_line(start, end, color='black'):
    x0, y0 = start
    x1, y1 = end
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    #напправление
    sx, sy = (1 if x0 < x1 else -1), (1 if y0 < y1 else -1)
    err = dx - dy

    while True:
        canvas.create_rectangle(
            x0 * pixel_size, y0 * pixel_size,  #верхний левый угол
            (x0 + 1) * pixel_size, (y0 + 1) * pixel_size,  #нижний правый угол
            fill=color, outline=color
        )
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        #шаги по х
        if e2 > -dy:
            err -= dy
            x0 += sx
        # шаги по у
        if e2 < dx:
            err += dx
            y0 += sy

def draw_grid():
    for x in range(0, 600, pixel_size):
        canvas.create_line(x, 0, x, 600, fill='gray', width=1)
    for y in range(0, 600, pixel_size):
        canvas.create_line(0, y, 600, y, fill='gray', width=1)

def draw_pyramid():
    canvas.delete('all')
    draw_grid()
    #цикл для ребер
    for edge in edges:
        start = project(pyramid[edge[0]])
        end = project(pyramid[edge[1]])
        start_pixel = (start[0] // pixel_size, start[1] // pixel_size)
        end_pixel = (end[0] // pixel_size, end[1] // pixel_size)
        draw_line(start_pixel, end_pixel)


def rotate_x(angle):
    rotation_matrix = np.array([
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ])
    return np.dot(pyramid - center_of_mass, rotation_matrix) + center_of_mass

def rotate_y(angle):
    rotation_matrix = np.array([
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ])
    return np.dot(pyramid - center_of_mass, rotation_matrix) + center_of_mass

def rotate_z(angle):
    rotation_matrix = np.array([
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ])
    return np.dot(pyramid - center_of_mass, rotation_matrix) + center_of_mass

#центр масс
center_of_mass = np.mean(pyramid, axis=0)

def handle_key(event):
    global pyramid
    if event.keysym == 'Up':
        pyramid = rotate_x(math.radians(5))
    elif event.keysym == 'Down':
        pyramid = rotate_x(math.radians(-5))
    elif event.keysym == 'Left':
        pyramid = rotate_y(math.radians(-5))
    elif event.keysym == 'Right':
        pyramid = rotate_y(math.radians(5))
    elif event.keysym == '0':
        pyramid = rotate_z(math.radians(5))
    draw_pyramid()

draw_pyramid()

root.bind('<Key>', handle_key)

root.mainloop()
