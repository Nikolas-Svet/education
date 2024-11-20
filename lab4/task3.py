from UnorderedList import *

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [UnorderedList() for _ in range(self.size)]

    def hashfunction(self, key):
        return sum(ord(char) for char in key) % self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)
        slot = self.slots[hashvalue]

        found = False
        for i in range(slot.size()):
            current_key, current_data = slot.pop(0)
            if current_key == key:
                slot.add((key, data))
                found = True
                break
            else:
                slot.add((current_key, current_data))
        if not found:
            slot.add((key, data))

        if self.get_load_factor() > 0.7:
            self.resize(self.get_next_prime(self.size * 2))

    def get(self, key):
        hashvalue = self.hashfunction(key)
        slot = self.slots[hashvalue]
        for i in range(slot.size()):
            current_key, current_data = slot.pop(0)
            if current_key == key:
                slot.add((current_key, current_data))
                return current_data
            else:
                slot.add((current_key, current_data))
        return None

    def __getitem__(self, key):
        result = self.get(key)
        if result is None:
            raise KeyError("Ключ не найден")
        return result

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        total = 0
        for slot in self.slots:
            total += slot.size()
        return total

    def __contains__(self, key):
        return self.get(key) is not None

    def get_load_factor(self):
        return len(self) / self.size

    def resize(self, new_size):
        old_slots = self.slots
        self.size = new_size
        self.slots = [UnorderedList() for _ in range(self.size)]
        for slot in old_slots:
            while not slot.isEmpty():
                key, data = slot.pop(0)
                self.put(key, data)

    def get_next_prime(self, n):
        def is_prime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

        while True:
            n += 1
            if is_prime(n):
                return n

    def __delitem__(self, key):
        hashvalue = self.hashfunction(key)
        slot = self.slots[hashvalue]
        found = False
        temp_list = UnorderedList()
        while not slot.isEmpty():
            current_key, current_data = slot.pop(0)
            if current_key == key:
                found = True
            else:
                temp_list.add((current_key, current_data))
        self.slots[hashvalue] = temp_list
        if not found:
            raise KeyError("Ключ не найден")

        if self.get_load_factor() < 0.2 and self.size > 11:
            new_size = max(11, self.get_previous_prime(self.size // 2))
            self.resize(new_size)

    def get_previous_prime(self, n):
        def is_prime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

        n -= 1
        while n > 2:
            if is_prime(n):
                return n
            n -= 1
        return 2

    def __str__(self):
        result = "{"
        for i, slot in enumerate(self.slots):
            if not slot.isEmpty():
                result += f"{i}: {slot}, "
        result = result.rstrip(", ") + "}"
        return result


H = HashTable()
H["apple"] = "fruit"
H["table"] = "furniture"
print(H["apple"])
print(H["table"])