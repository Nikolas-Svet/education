class HashTable:
    DELETED = object()

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)

        if self.slots[hashvalue] is None or self.slots[hashvalue] is HashTable.DELETED:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:

                i = 1
                nextslot = self.rehash(hashvalue, i)
                while (self.slots[nextslot] is not None and self.slots[nextslot] is not HashTable.DELETED) and self.slots[nextslot] != key:
                    i += 1
                    nextslot = self.rehash(hashvalue, i)
                    if nextslot == hashvalue:
                        raise Exception("Таблица переполнена")
                if self.slots[nextslot] is None or self.slots[nextslot] is HashTable.DELETED:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

        if self.get_load_factor() > 0.7:
            self.resize(self.get_next_prime(self.size * 2))

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, oldhash, i):
        return (oldhash + i ** 2) % self.size

    def get(self, key):
        startslot = self.hashfunction(key)
        position = startslot
        data = None
        found = False
        stop = False
        i = 1
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(startslot, i)
                i += 1
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        result = self.get(key)
        if result is None:
            raise KeyError("Ключ не найден")
        return result

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        count = 0
        for slot in self.slots:
            if slot is not None and slot is not HashTable.DELETED:
                count += 1
        return count

    def __contains__(self, key):
        return self.get(key) is not None

    def get_load_factor(self):
        return len(self) / self.size

    def resize(self, new_size):
        old_slots = self.slots
        old_data = self.data
        self.size = new_size
        self.slots = [None] * self.size
        self.data = [None] * self.size

        for i in range(len(old_slots)):
            if old_slots[i] is not None and old_slots[i] is not HashTable.DELETED:
                self.put(old_slots[i], old_data[i])

    def get_next_prime(self, n):
        while True:
            n += 1
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    break
            else:
                return n

    def __delitem__(self, key):
        startslot = self.hashfunction(key)
        position = startslot
        found = False
        stop = False
        i = 1
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                self.slots[position] = HashTable.DELETED
                self.data[position] = None
            else:
                position = self.rehash(startslot, i)
                i += 1
                if position == startslot:
                    stop = True
        if not found:
            raise KeyError("Ключ не найден")

        if self.get_load_factor() < 0.2 and self.size > 11:
            new_size = max(11, self.get_previous_prime(self.size // 2))
            self.resize(new_size)

    def get_previous_prime(self, n):
        while n > 2:
            n -= 1
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    break
            else:
                return n
        return 2

    def __str__(self):
        result = "{"
        for i in range(len(self.slots)):
            if self.slots[i] is not None and self.slots[i] is not HashTable.DELETED:
                result += f"{self.slots[i]}: {self.data[i]}, "
        result = result.rstrip(", ") + "}"
        return result


H = HashTable()

H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"

print("Слоты:", H.slots)
print("Данные:", H.data)

print("H[20]:", H[20])
print("H[17]:", H[17])

H[20] = 'duck'
print("H[20] после обновления:", H[20])

print("99 в H?", 99 in H)

try:
    print(H[99])
except KeyError as e:
    print(e)

del H[31]
print("Слоты после удаления 31:", H.slots)
print("Данные после удаления 31:", H.data)

print("Длина H:", len(H))

print("Загрузочный фактор:", H.get_load_factor())

for i in range(100, 120):
    H[i] = f"number{i}"

print("Новый размер таблицы после увеличения:", H.size)

for i in range(100, 120):
    del H[i]

print("Размер таблицы после уменьшения:", H.size)
