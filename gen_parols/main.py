import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from random import choice
import pyperclip
import string

alphabet = list(string.ascii_letters)
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
number_alphabet = [x for x in alphabet] + [x for x in number]
special_characters = list(string.punctuation)
Hard_dificult = number_alphabet + special_characters


password_complexity = {
    1: 'Легкий',
    2: 'Середній',
    3: 'Важкий'
}


def info():
    showinfo('Довідник', '''Для початку потрібно вибрати рівень складності паролю
Легкий - складається тільки з набору цифр;
Середній - з цифр, та букв англійського алфавіту ;
Важкий - з цифр, букв та спец. символів;
    Потім, потрібно ввести к-ть символів, зауважте, їх має бути не менше 0.
    Та натиснути 'Отримати', вам буде підібрано унікальний пароль
    Після чого, зможете його скопіювати за допомогою відповідної кнопки''')

def select_complexity():
    selected_complexity = password_complexity.get(complexity.get())
    complexity_text.set(f'Ви вибрали {selected_complexity} рівень складності паролю')

def copy():
    password = ready_password.get()
    pyperclip.copy(password)

def generate():
    try:
        len_password = int(input_info.get())
    except (UnboundLocalError,ValueError):
        messagebox.showinfo('Помилка', 'Потрібно вводити тільки цифри!! Ви ввели інші символи')
        input_info.delete(0, tk.END)
        input_info.insert(0, '1')
        return

    password = []
    selected_complexity = complexity.get()

    if selected_complexity == 1 and len_password > 0:
        for char_pass in range(0, len_password):
            pass_char = choice(number)
            password.append(str(pass_char))
    elif selected_complexity == 2 and len_password > 0:
        for char_pass in range(0, len_password):
            pass_char = choice(number_alphabet)
            password.append(str(pass_char))
    elif selected_complexity == 3 and len_password > 0:
        for char_pass in range(0, len_password):
            pass_char = choice(Hard_dificult)
            password.append(str(pass_char))
    password_user.set(''.join(password))


win = tk.Tk()
win.geometry('300x250+100+200')
win.title('Генератор паролів')
win.resizable(False, False)
photo = tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)


password_user = tk.StringVar()
complexity_text = tk.StringVar()
complexity = tk.IntVar()

tk.Label(win, text="Виберіть рівень складності").grid(row=0, column=0, stick='we', padx=10, columnspan=2)
for level in password_complexity:
    tk.Radiobutton(win, text=password_complexity[level],
                   variable=complexity, value=level,
                   command=select_complexity).grid(row=level, column=0, stick='we')

tk.Label(win, text="Введіть кількість символів").grid(row=5, column=0, stick='we', padx=10, columnspan=2)

input_info = tk.Entry(win)
input_info.grid(row=6, column=0, sticky='we', padx=10, columnspan=2)

copy_button = tk.Label(win, text="Скопіюйте отриманий пароль тут:")
copy_button.grid(row=7, column=0, stick='we', padx=10, columnspan=2)

ready_password = tk.Entry(win, textvariable=password_user)
ready_password.grid(row=8, column=0, sticky='we', padx=10, columnspan=2)

give = tk.Button(win, text='Отримати', command=generate)
give.grid(row=9, column=0, stick='we', padx=10, columnspan=2)

copy_pass = tk.Button(win, text='Скопіювати пароль', command=copy)
copy_pass.grid(row=10, column=0, sticky='we', padx=10, columnspan=2)

win.columnconfigure(0, minsize=300)

menubar = tk.Menu(win)
win.config(menu=menubar)
setting_menu = tk.Menu(menubar, tearoff=0)
setting_menu.add_command(label='Про підбір', command=info)
menubar.add_cascade(label='Інфо', menu=setting_menu)

win.mainloop()