import tkinter as tk
from tkinter import messagebox


# логіка програми
def add_digit(digit):
	value = calc.get()
	if value[0]=='0' and len(value)==1:
		value = value[1:]
	calc.delete(0, 'end')
	calc.insert('end', value+digit)

def add_operation(operation):
	value = calc.get()
	if value[-1] in '-+/*':
		value = value[:-1]
	elif '+' in value or '-' in value or '*' in value or '/' in value:
		calculate()
		value=calc.get()
	calc.delete(0, 'end')
	calc.insert(0, value+operation)

def calculate():
	value = calc.get()
	if value[-1] in '+-*/':
		value = value+value[:-1]
	calc.delete(0, 'end')
	try:
		calc.insert(0, eval(value))
	except (NameError, SyntaxError):
		messagebox.showinfo('Помилка', 'Потрібно вводити тільки цифрии!! Ви ввели інші символи')
		calc.insert(0, 0)
	except ZeroDivisionError:
		messagebox.showinfo('Помилка', 'На нуль ділити неможна!!')
		calc.insert(0, 0)

def clear():
	calc.delete(0, 'end')
	calc.insert(0,0)

def make_digit_buttom(digit):
	return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit), activebackground='#397ECD')

def make_operation_buttom(operation):
	return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_operation(operation), activebackground='orange')

def make_calc_button(operation):
	return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=calculate, activebackground='orange')

def make_clear_button(operation):
	return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=clear, activebackground='orange')

def press_key(event):
	if event.char.isdigit():
		add_digit(event.char)
	elif event.char in '+-*/':
		add_operation(event.char)
	elif event.char == '\r':
		calculate()
	elif event.char == '.':
		calc.insert('end', '.')

# вікно, та віджети
win = tk.Tk()
win.geometry(f'245x280+100+200')
win.resizable(False, False)
win['bg'] = 'grey'
photo = tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)
win.title('Калькулятор')
win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0,0)
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5, pady=5)
make_digit_buttom('1').grid(row=1, column=0, stick='wens', padx=2, pady=2)
make_digit_buttom('2').grid(row=1, column=1, stick='wens', padx=2, pady=2)
make_digit_buttom('3').grid(row=1, column=2, stick='wens', padx=2, pady=2)
make_digit_buttom('4').grid(row=2, column=0, stick='wens', padx=2, pady=2)
make_digit_buttom('5').grid(row=2, column=1, stick='wens', padx=2, pady=2)
make_digit_buttom('6').grid(row=2, column=2, stick='wens', padx=2, pady=2)
make_digit_buttom('7').grid(row=3, column=0, stick='wens', padx=2, pady=2)
make_digit_buttom('8').grid(row=3, column=1, stick='wens', padx=2, pady=2)
make_digit_buttom('9').grid(row=3, column=2, stick='wens', padx=2, pady=2)
make_digit_buttom('0').grid(row=4, column=0, stick='wens', padx=2, pady=2)


make_operation_buttom('+').grid(row=1, column=3, stick='wens', padx=2, pady=2)
make_operation_buttom('-').grid(row=2, column=3, stick='wens', padx=2, pady=2)
make_operation_buttom('*').grid(row=3, column=3, stick='wens', padx=2, pady=2)
make_operation_buttom('/').grid(row=4, column=3, stick='wens', padx=2, pady=2)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=2, pady=2)
make_clear_button('C').grid(row=4, column=1, stick='wens', padx=2, pady=2)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)

win.grid_columnconfigure(3, minsize=60)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.mainloop()