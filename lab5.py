import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import math

# DMC палитра (пример сокращенной палитры)
DMC_COLORS = [
    {'code': '310', 'name': 'Black', 'rgb': (0, 0, 0)},
    {'code': '321', 'name': 'Red', 'rgb': (208, 0, 48)},
    {'code': '445', 'name': 'Lemon Light', 'rgb': (255, 251, 139)},
    {'code': '703', 'name': 'Chartreuse', 'rgb': (123, 181, 71)},
    {'code': '820', 'name': 'Royal Blue Dark', 'rgb': (14, 54, 92)},
    {'code': '970', 'name': 'Pumpkin Light', 'rgb': (247, 139, 19)},
    {'code': 'B5200', 'name': 'Snow White', 'rgb': (255, 255, 255)},
    # Добавьте больше цветов по необходимости
]

SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class CrossStitchPattern:
    def __init__(self, master):
        self.master = master
        self.master.title("Конвертер в схему для вышивки крестиком")
        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self.master, text="Загрузить изображение", command=self.load_image)
        self.load_button.pack()

        self.color_label = tk.Label(self.master, text="Максимальное количество цветов:")
        self.color_label.pack()
        self.color_entry = tk.Entry(self.master)
        self.color_entry.pack()
        self.color_entry.insert(0, "5")

        self.size_label = tk.Label(self.master, text="Максимальный размер схемы (крестиков):")
        self.size_label.pack()
        self.size_entry = tk.Entry(self.master)
        self.size_entry.pack()
        self.size_entry.insert(0, "50")

        self.convert_button = tk.Button(self.master, text="Конвертировать", command=self.convert_image)
        self.convert_button.pack()

        self.canvas = tk.Canvas(self.master)
        self.canvas.pack()

    def load_image(self):
        self.filename = filedialog.askopenfilename(title='Выберите изображение')
        if self.filename:
            self.original_image = Image.open(self.filename)
            self.display_image(self.original_image)

    def display_image(self, img):
        img.thumbnail((400, 400))
        self.tk_image = ImageTk.PhotoImage(img)
        self.canvas.config(width=self.tk_image.width(), height=self.tk_image.height())
        self.canvas.create_image(0, 0, anchor='nw', image=self.tk_image)

    def convert_image(self):
        max_colors = int(self.color_entry.get())
        max_size = int(self.size_entry.get())
        if not hasattr(self, 'original_image'):
            return

        # Преобразование изображения
        img = self.original_image.convert('RGB')
        width, height = img.size
        aspect_ratio = width / height

        if width > height:
            new_width = min(width, max_size)
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = min(height, max_size)
            new_width = int(new_height * aspect_ratio)

        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Разбиение на крестики
        img_array = np.array(img)
        stitch_height, stitch_width = img_array.shape[0], img_array.shape[1]
        stitches = img_array.reshape(-1, 3)

        # Сопоставление цветов с палитрой DMC
        dmc_colors = np.array([color['rgb'] for color in DMC_COLORS])
        indices = self.match_colors(stitches, dmc_colors, max_colors)
        pattern = indices.reshape(stitch_height, stitch_width)

        # Генерация схемы
        self.generate_pattern(pattern, dmc_colors, new_width, new_height)

    def match_colors(self, stitches, dmc_colors, max_colors):
        from sklearn.cluster import KMeans

        # Кластеризация цветов
        kmeans = KMeans(n_clusters=min(max_colors, len(DMC_COLORS)))
        kmeans.fit(stitches)
        cluster_centers = kmeans.cluster_centers_

        # Поиск ближайших цветов в палитре DMC
        indices = []
        for center in cluster_centers:
            distances = np.sqrt(np.sum((dmc_colors - center) ** 2, axis=1))
            index = np.argmin(distances)
            indices.append(index)

        # Назначение цветов кластерам
        labels = kmeans.labels_
        mapped_indices = np.array([indices[label] for label in labels])

        return mapped_indices

    def generate_pattern(self, pattern, dmc_colors, width, height):
        # Создание изображения схемы
        cell_size = 20
        img_width = width * cell_size
        img_height = height * cell_size
        pattern_image = Image.new('RGB', (img_width, img_height), 'white')
        draw = ImageDraw.Draw(pattern_image)

        # Назначение символов цветам
        unique_indices = np.unique(pattern)
        symbol_dict = {}
        for i, index in enumerate(unique_indices):
            symbol_dict[index] = SYMBOLS[i % len(SYMBOLS)]

        # Рисование клеток
        for y in range(height):
            for x in range(width):
                index = pattern[y, x]
                color = tuple(dmc_colors[index])
                symbol = symbol_dict[index]
                x0 = x * cell_size
                y0 = y * cell_size
                x1 = x0 + cell_size
                y1 = y0 + cell_size

                # Рисование квадрата цвета
                draw.rectangle([x0, y0, x1, y1], fill=color)

                # Рисование символа
                draw.text((x0 + cell_size / 2, y0 + cell_size / 2), symbol, fill='black', anchor='mm')

                # Рисование линий сетки
                draw.rectangle([x0, y0, x1, y1], outline='gray')

        # Отображение схемы
        self.display_image(pattern_image)

        # Создание легенды
        self.create_legend(symbol_dict, unique_indices)

    def create_legend(self, symbol_dict, unique_indices):
        legend_window = tk.Toplevel(self.master)
        legend_window.title("Легенда")
        for index in unique_indices:
            symbol = symbol_dict[index]
            color_info = DMC_COLORS[index]
            legend_label = tk.Label(legend_window, text=f"Символ: {symbol} - DMC {color_info['code']} {color_info['name']}")
            legend_label.pack()

if __name__ == "__main__":
    import sys
    from PIL import ImageDraw
    from sklearn.cluster import KMeans

    root = tk.Tk()
    app = CrossStitchPattern(root)
    root.mainloop()
