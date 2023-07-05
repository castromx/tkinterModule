import tkinter as tk
from tkinter.messagebox import showinfo, showerror

condition = {
    1: 'Знайти % від числа',
    2: 'Знайти число а, коли відомо що % від нього = b',
    3: 'Знайти % відносно числа'
}

message_error = 'В підрахунках цієї операції сталася помилка! Перевірте вхідні данні, на їх правильність, на відсутність 0, та букв'

def ok():
    selected_condition = condition.get(umova_var.get())
    win_conditions = tk.Toplevel(win)
    photo = tk.PhotoImage(file='icon.png')
    win_conditions.iconphoto(False, photo)
    win_conditions.resizable(False, False)
    if selected_condition == 'Знайти % від числа':
        win_conditions.wm_title(selected_condition)
        tk.Label(win_conditions, text='Введіть число від якого потрібно знайти %:').grid(row=0, column=0)
        first_char = tk.Entry(win_conditions)
        first_char.grid(row=0, column=1, padx=20, pady=20)

        tk.Label(win_conditions, text='Введіть %:').grid(row=1, column=0)
        second_char = tk.Entry(win_conditions)
        second_char.grid(row=1, column=1, padx=20, pady=20)

        def calculate():
        	try:
        		a = int(first_char.get())
        		b = int(second_char.get())
        		result = a / 100 * b
        		first_condition.config(text=f'Результат: {result}')
        	except (ValueError,UnboundLocalError):
        		showerror('Помилка', 'Потрібно вводити тільки цифри!')

        tk.Button(win_conditions, text='Ок', command=calculate).grid(row=2, column=0, columnspan=2)

        first_condition = tk.Label(win_conditions)
        first_condition.grid(row=3, column=0, columnspan=2)

    elif selected_condition == 'Знайти число а, коли відомо що % від нього = b':
        win_conditions.wm_title(selected_condition)
        tk.Label(win_conditions, text='Введіть %:').grid(row=0, column=0)
        first_char = tk.Entry(win_conditions)
        first_char.grid(row=0, column=1, padx=20, pady=20)

        tk.Label(win_conditions, text='Введіть число b:').grid(row=1, column=0)
        second_char = tk.Entry(win_conditions)
        second_char.grid(row=1, column=1, padx=20, pady=20)

        def calculate():
        	try:
        		a = int(first_char.get())
        		b = int(second_char.get())
        		result = b/a*100
        		second_condition.config(text=f'Результат: {result}')
        	except (ValueError,UnboundLocalError, ZeroDivisionError):
        		showerror('Помилка', message_error)

        tk.Button(win_conditions, text='Ок', command=calculate).grid(row=2, column=0, columnspan=2)

        second_condition = tk.Label(win_conditions)
        second_condition.grid(row=3, column=0, columnspan=2)

    elif selected_condition == 'Знайти % відносно числа':
        win_conditions.wm_title(selected_condition)
        tk.Label(win_conditions, text='Введіть число a:').grid(row=0, column=0)
        first_char = tk.Entry(win_conditions)
        first_char.grid(row=0, column=1, padx=20, pady=20)

        tk.Label(win_conditions, text='Введіть число b:').grid(row=1, column=0)
        second_char = tk.Entry(win_conditions)
        second_char.grid(row=1, column=1, padx=20, pady=20)


        def calculate():
        	try:
        		a = int(first_char.get())
        		b = int(second_char.get())
        		result = (a/b)*100
        		third_condition.config(text=f'Результат: {result}')
        	except (ValueError,UnboundLocalError, ZeroDivisionError):
        		showerror('Помилка', message_error)

        tk.Button(win_conditions, text='Ок', command=calculate).grid(row=2, column=0, columnspan=2)

        third_condition = tk.Label(win_conditions)
        third_condition.grid(row=3, column=0, columnspan=2)

win = tk.Tk()
win.geometry(f'320x150+100+200')
win.title('Проценти V2.0')
photo = tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)
win.resizable(False, False)

label_1 = tk.Label(win, text='Виберіть умову задачі')
label_1.pack()

umova_var = tk.IntVar()

for cond in condition:
    tk.Radiobutton(win, text=condition[cond], variable=umova_var, value=cond).pack()

tk.Button(win, text='Ок', command=ok, padx=15, pady=2).pack()

win.mainloop()