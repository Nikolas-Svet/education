import random

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Operator:
    def __init__(self):
        self.current_call = None
        self.time_remaining = 0

    def tick(self):
        if self.current_call:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_call = None

    def busy(self):
        return self.current_call is not None

    def start_next(self, call):
        self.current_call = call
        self.time_remaining = call.duration

class Call:
    def __init__(self, time):
        self.timestamp = time
        self.duration = random.randint(3, 10)

    def wait_time(self, current_time):
        return current_time - self.timestamp

def simulation(num_minutes, num_operators):
    call_queue = Queue()
    operators = [Operator() for _ in range(num_operators)]
    waiting_times = []

    for current_minute in range(num_minutes):
        if new_call():
            call = Call(current_minute)
            call_queue.enqueue(call)

        for operator in operators:
            operator.tick()
            if not operator.busy() and not call_queue.is_empty():
                next_call = call_queue.dequeue()
                waiting_times.append(next_call.wait_time(current_minute))
                operator.start_next(next_call)

    average_wait = sum(waiting_times) / len(waiting_times) if waiting_times else 0
    print(f"Среднее время ожидания: {average_wait:.2f} минут. Звонков в очереди осталось: {call_queue.size()}")

def new_call():
    return random.random() < 0.5

