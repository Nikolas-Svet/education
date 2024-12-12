import random

def first_fit(items, capacity=1.0):
    boxes = []
    for item in items:
        placed = False
        for box in boxes:
            if sum(box)+item <= capacity:
                box.append(item)
                placed = True
                break
        if not placed:
            boxes.append([item])
    return boxes

def best_fit(items, capacity=1.0):
    boxes = []
    for item in items:
        best_idx = -1
        best_space = capacity+1
        for i, box in enumerate(boxes):
            free = capacity - sum(box)
            if free >= item and free - item < best_space:
                best_space = free - item
                best_idx = i
        if best_idx == -1:
            boxes.append([item])
        else:
            boxes[best_idx].append(item)
    return boxes

def next_fit(items, capacity=1.0):
    boxes = []
    current_box = []
    current_sum = 0.0
    for item in items:
        if current_sum + item <= capacity:
            current_box.append(item)
            current_sum += item
        else:
            boxes.append(current_box)
            current_box = [item]
            current_sum = item
    if current_box:
        boxes.append(current_box)
    return boxes

def worst_fit(items, capacity=1.0):
    # Наименее подходящий ящик: будет выбирать ящик с максимальным остатком
    boxes = []
    for item in items:
        worst_idx = -1
        worst_space = -1
        for i, box in enumerate(boxes):
            free = capacity - sum(box)
            if free >= item and free > worst_space:
                worst_space = free
                worst_idx = i
        if worst_idx == -1:
            boxes.append([item])
        else:
            boxes[worst_idx].append(item)
    return boxes

if __name__ == "__main__":
    for n in [50,100,200,500]:
        items = [round(random.uniform(0.1,0.9),2) for _ in range(n)]
        ff_boxes = first_fit(items)
        bf_boxes = best_fit(items)
        nf_boxes = next_fit(items)
        wf_boxes = worst_fit(items)
        print(f"Количество предметов={n}:")
        print("Первый подходящий ящик:", len(ff_boxes))
        print("Наиболее подходящий ящик:", len(bf_boxes))
        print("Следующий подходящий ящик:", len(nf_boxes))
        print("Наименее подходящий ящик:", len(wf_boxes))
        print("-"*30)
