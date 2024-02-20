from queue import Queue
from collections import deque
import string

# Завдання 1: Система обробки заявок у сервісному центрі

def generate_request(queue, request_number):
    """
    Функція для генерації нових заявок та додавання їх до черги.

    Args:
    queue: черга, до якої потрібно додати заявку.
    request_number: поточний номер заявки.

    Returns:
    Нове значення поточного номера заявки.
    """
    request_number += 1  # Збільшуємо номер заявки
    queue.put(request_number)  # Додаємо заявку до черги
    print(f"Заявка {request_number} додана до черги.")
    return request_number  # Повертаємо нове значення номера заявки

def process_request(queue):
    """
    Функція для обробки заявок з черги.

    Args:
    queue: черга заявок.
    """
    if not queue.empty():  # Перевіряємо, чи черга не порожня
        request = queue.get()  # Видаляємо заявку з черги
        print(f"Заявка {request} оброблена.")
    else:
        print("Черга порожня.")

# Створення черги для заявок
request_queue = Queue()
request_number = 0  # Початковий номер заявки

# Головний цикл програми для завдання 1
while True:
    command = input("Введіть 'gen' для генерації нової заявки або 'proc' для обробки заявки (або 'exit' для виходу): ")
    if command == "gen":
        request_number = generate_request(request_queue, request_number)  # Викликаємо функцію генерації заявки
    elif command == "proc":
        process_request(request_queue)  # Викликаємо функцію обробки заявки
    elif command == "exit":
        break  # Виходимо з циклу, якщо користувач вибрав 'exit'
    else:
        print("Невідома команда.")

# Завдання 2: Визначення паліндрома

def is_palindrome(s):
    """
    Функція для перевірки, чи є рядок паліндромом.

    Args:
    s: рядок для перевірки.

    Returns:
    True, якщо рядок є паліндромом, False - інакше.
    """
    s = s.lower()  # Зниження регістру
    s = ''.join(char for char in s if char.isalnum())  # Вилучення символів пунктуації та пробілів
    char_deque = deque(s)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Вхідний рядок для перевірки
input_string = input("Введіть рядок для перевірки на паліндром: ")

if is_palindrome(input_string):
    print("Рядок є паліндромом.")
else:
    print("Рядок не є паліндромом.")
