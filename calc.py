import tkinter as tk

def on_click(button_value):
    current = entry.get()
    if button_value == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    elif button_value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_value)

# Создание графического интерфейса
root = tk.Tk()
root.title("Калькулятор")

# Поле ввода
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Кнопки
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row_num, col_num = 1, 0
for button_value in buttons:
    tk.Button(root, text=button_value, width=10, command=lambda value=button_value: on_click(value)).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Запуск основного цикла приложения
root.mainloop()
