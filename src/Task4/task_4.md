# Завдання 4

Доробіть консольного бота-помічника з попереднього домашнього завдання та додайте обробку помилок за допомогою декораторів.

---

### Вимоги до завдання

- Всі помилки введення користувача повинні оброблятися за допомогою декоратора `input_error`.
- Декоратор `input_error` відповідає за повернення повідомлень на зразок:
  - `"Enter user name"`
  - `"Give me name and phone please"`
  - та інші, залежно від типу помилки.
- Декоратор повинен обробляти винятки:
  - `KeyError`
  - `ValueError`
  - `IndexError`
- Винятки не мають зупиняти виконання програми.

---

### Рекомендації для виконання

Приклад базового декоратора для `ValueError`:

```python
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
    return inner
```

Обгортання функції:

```python
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
```

> Вам необхідно додати аналогічну обробку для інших команд і обробити інші винятки.

---

### Критерії оцінювання

- Наявність декоратора `input_error`, який обробляє всі три типи помилок.
- Усі команди бота мають бути захищені декоратором.
- Повідомлення користувачу повинні бути інформативними та відповідати типу помилки.
- Бот не має завершувати роботу через помилки введення.

---

### Приклад використання

```
Enter a command: add
Enter the argument for the command

Enter a command: add Bob
Enter the argument for the command

Enter a command: add Jime 0501234356
Contact added.

Enter a command: phone
Enter the argument for the command

Enter a command: all
Jime: 0501234356

Enter a command:
```