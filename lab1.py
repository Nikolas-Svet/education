import tkinter as tk

def create_rectangle(cnv, x, y, length, color="black"):
    coords = [(x, y), (x + length, y), (x + length, y + length), (x, y + length)]
    for i in range(4):
        cnv.create_line(coords[i][0], coords[i][1], coords[(i + 1) % 4][0], coords[(i + 1) % 4][1], fill=color)

def create_polygon(cnv, p1, p2, p3, width = 2, color="black"):
    cnv.create_line(p1[0], p1[1], p2[0], p2[1], fill=color, width=width)
    cnv.create_line(p2[0], p2[1], p3[0], p3[1], fill=color, width=width)
    cnv.create_line(p3[0], p3[1], p1[0], p1[1], fill=color, width=width)

def create_ellipse(cnv, tl, br, width = 2, color="black"):
    cnv.create_oval(tl[0], tl[1], br[0], br[1], outline=color, width=width)

shapes = {
    "rect": False,
    "poly": False,
    "oval": False
}

def render_shapes(shape_type):
    if shape_type == "rect":
        remove_rectangle()
        if shapes["oval"]:
            draw_oval()
        if shapes["poly"]:
            draw_polygon()
    elif shape_type == "poly":
        remove_polygon()
        if shapes["oval"]:
            draw_oval()
        if shapes["rect"]:
            draw_rectangle()
    elif shape_type == "oval":
        remove_oval()
        if shapes["rect"]:
            draw_rectangle()
        if shapes["poly"]:
            draw_polygon()

def draw_rectangle():
    global shapes
    create_rectangle(cnv, 60, 60, 100)
    shapes["rect"] = True

def draw_polygon():
    global shapes
    create_polygon(cnv, (130, 60), (250, 150), (100, 80))
    shapes["poly"] = True

def draw_oval():
    global shapes
    create_ellipse(cnv, (30, 30), (140, 140))
    shapes["oval"] = True

app = tk.Tk()
app.title("Shape Drawer")

cnv = tk.Canvas(app, bg="white", width=400, height=300)
cnv.pack()

tk.Button(app, text="Add Rectangle", command=draw_rectangle).pack()
tk.Button(app, text="Add Trinagle", command=draw_polygon).pack()
tk.Button(app, text="Add Circle", command=draw_oval).pack()

def remove_rectangle():
    global shapes
    create_rectangle(cnv, 60, 60, 100, color="white")
    shapes["rect"] = False

def remove_polygon():
    global shapes
    create_polygon(cnv, (130, 60), (250, 150), (100, 80), width=4, color="white")
    shapes["poly"] = False

def remove_oval():
    global shapes
    create_ellipse(cnv, (30, 30), (140, 140), width=4, color="white")
    shapes["oval"] = False

tk.Button(app, text="Remove Rectangle", command=lambda: render_shapes("rect")).pack()
tk.Button(app, text="Remove Triangle", command=lambda: render_shapes("poly")).pack()
tk.Button(app, text="Remove Circle", command=lambda: render_shapes("oval")).pack()

app.mainloop()
