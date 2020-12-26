import tkinter as tk  # Импорт библиотеки Tkinter для работы с GUI (сокращенно tk)

win = tk.Tk()  # Создаём окно
win.geometry("240x270+800+200")  # Задём размеры окна и размещение на экране
win.title("Калькулятор")  # Указываем название
win["bg"] = "#876E94"  # Задаём цвет бекграунда
calc = tk.Entry(win, justify=tk.RIGHT, font=("Arial", 15), width=15)  # Переменная для ввода данных расчёта
calc.insert(0, "0")  # Указываем 0 в качестве начальной цифры
calc.grid(row=0, column=0, columnspan=4, stick="we", padx=5)  # Размещаем переменную ввода

"""Функция добавления цифры в окно ввода"""


def add_digit(digit):
    value = calc.get()  # Переменная принимающая данные из окна ввода
    if value[0] == "0" and len(value) == 1:  # Проверка и удаление 0
        value = value[1:]
    calc.delete(0, tk.END)  # Очищаем поле ввода
    calc.insert(0, value + digit)  # Вводим данные в поле


"""Функция очищения окна ввода"""


def clear():
    calc.delete(0, tk.END)  # Очищаем поле ввода
    calc.insert(0, 0)  # Вводим данные в поле


"""Функция создания кнопки очищения окна ввода"""


def make_del_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), fg="red", command=clear)


"""Функция добавления знака вычисления в окно ввода"""


def add_operation(operation):
    value = calc.get()  # Переменная принимающая данные из окна ввода
    if value[-1] in "-+/*":  # Проверка ввода данных
        value = value[:-1]  # Выборка последнего ввода
    elif "+" in value or "-" in value or "/" in value or "*" in value:  #
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)  # Очищаем поле ввода
    calc.insert(0, value + operation)  # Вводим последние данные


"""Функция вычисления"""


def calculate():
    value = calc.get()  # Переменная принимающая данные из окна ввода
    if value[-1] in "-+/*":  # Проверка на отсутствие второго оператора
        value = value + value[:-1]  # Если отсутствует второй оператор, производим действие с первым
    calc.delete(0, tk.END)  # Очищаем поле ввода
    calc.insert(0, eval(value))  # Делаем расчёт функцией eval() и вводим последние данные


"""Функция создания кнопок ввода цифр"""


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=("Arial", 13), command=lambda: add_digit(digit))


"""Функция создания кнопок операций"""


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), fg="red", command=lambda: add_operation(operation))


"""Функция создания кнопки вычисления операций"""


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), fg="red", command=calculate)


"""Создаём и оформляем кнопки 0-9"""
make_digit_button("1").grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_digit_button("2").grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_digit_button("3").grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_digit_button("4").grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_digit_button("5").grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_digit_button("6").grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_digit_button("7").grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_digit_button("8").grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_digit_button("9").grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_digit_button("0").grid(row=4, column=0, stick="wens", padx=5, pady=5)

"""Создаём и оформляем кнопки операций"""

make_operation_button("+").grid(row=1, column=3, stick="wens", padx=5, pady=5)
make_operation_button("-").grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_operation_button("/").grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_operation_button("*").grid(row=4, column=3, stick="wens", padx=5, pady=5)

"""Создаём и оформляем кнопку вычисления операций"""

make_calc_button("=").grid(row=4, column=2, stick="wens", padx=5, pady=5)

"""Создаём и оформляем кнопку удаления операций"""

make_del_button("С").grid(row=4, column=1, stick="wens", padx=5, pady=5)

"""Устанавливаем размер колонок"""
win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)
"""Устанавливаем размер рядов"""
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
