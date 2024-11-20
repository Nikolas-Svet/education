import hashlib
import secrets
import json
import os

def register(username, password):
    salt = secrets.token_bytes(32)
    hashed_password = hashlib.scrypt(password.encode('utf-8'), salt=salt, n=16384, r=8, p=1)
    user_data = {
        'salt': salt.hex(),
        'hashed_password': hashed_password.hex()
    }

    if not os.path.exists('users.json'):
        with open('users.json', 'w') as file:
            json.dump({}, file)

    with open('users.json', 'r+') as file:
        try:
            users = json.load(file)
        except json.JSONDecodeError:
            users = {}
        users[username] = user_data
        file.seek(0)
        json.dump(users, file, indent=4)
    print(f"Пользователь {username} успешно зарегистрирован.")

def login(username, password):
    if not os.path.exists('users.json'):
        print("База данных пользователей не найдена.")
        return False

    with open('users.json', 'r') as file:
        try:
            users = json.load(file)
        except json.JSONDecodeError:
            print("Ошибка чтения базы данных пользователей.")
            return False

    if username not in users:
        print("Пользователь не найден.")
        return False

    user_data = users[username]
    salt = bytes.fromhex(user_data['salt'])
    stored_hashed_password = bytes.fromhex(user_data['hashed_password'])
    hashed_password = hashlib.scrypt(password.encode('utf-8'), salt=salt, n=16384, r=8, p=1)

    if hashed_password == stored_hashed_password:
        print(f"Пользователь {username} успешно вошел в систему.")
        return True
    else:
        print("Неверный пароль.")
        return False

register('user1', 'my_secure_password')
login('user1', 'my_secure_password')
login('user1', 'wrong_password')
