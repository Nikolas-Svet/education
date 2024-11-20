import os
import hashlib

def find_duplicates(directory):
    hash_dict = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            with open(filepath, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            if file_hash in hash_dict:
                hash_dict[file_hash].append(filepath)
            else:
                hash_dict[file_hash] = [filepath]
    duplicates_found = False
    for file_list in hash_dict.values():
        if len(file_list) > 1:
            duplicates_found = True
            print("Дубликаты найдены:")
            for file in file_list:
                print(file)
            print("-" * 40)
    if not duplicates_found:
        print("Дубликаты не найдены.")

directory = input("Введите путь до директории: ")
find_duplicates(directory)