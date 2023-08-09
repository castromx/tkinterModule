import tkinter as tk
from random import shuffle
from tkinter.messagebox import showinfo, showerror

# Словник використовується для визначення кольорів тексту, 
# який відображається на кнопках гри залежно від кількості мін, що оточують цю кнопку
colors = {
    1: 'blue',
    2: 'green',
    3: 'red',
    4: 'yellow',
    5: 'purple',
    6: 'orange',
    7: '#003366',
    8: '#FF66FF',
}

# Переоприділив створення внопки Button, щоб розширити певну функціональність (відображення __str__)
# та оптимізувати код
class MyButton(tk.Button):
    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0
        self.is_open = False

    def __repr__(self):
        return f'MyButton {self.x} {self.y} {self.number} {self.is_mine}'


class MineSweeper:
    window = tk.Tk()
    photo = tk.PhotoImage(file='icon.png')
    window.iconphoto(False, photo)
    window.title('Сапер')
    ROW = 12
    COLUMNS = 16
    MINES = 25
    IS_GAME_OVER = False
    IS_FIRST_CLICK = True
    marked_mines = 0
    elapsed_time = 0 # Час гри, що змінюється кожну секунду у методі start_timer

    def __init__(self):
        self.buttons = []
        self.marked_mines = 0
        self.elapsed_time = 0
        
        # Створення кнопок
        for i in range(MineSweeper.ROW + 2):
            temp = []
            for j in range(MineSweeper.COLUMNS + 2):
                btn = MyButton(MineSweeper.window, x=i, y=j)
                btn.config(command=lambda button=btn: self.click(button))
                btn.bind('<Button-3>', self.right_click)
                temp.append(btn)
            self.buttons.append(temp)

    def update_marked_mines_label(self):
        self.marked_mines_label.config(text=f"Відмічені міни: {self.marked_mines}")

    def update_elapsed_time_label(self):
        self.elapsed_time_label.config(text=f"Час: {self.elapsed_time} сек")

    # Обробка правого кліку мишки (додає прапорець, або знімає якщо він там був)
    def right_click(self, event):
        if MineSweeper.IS_GAME_OVER:
            return
        cur_btn = event.widget
        if cur_btn['state'] == 'normal':
            cur_btn['state'] = 'disabled'
            cur_btn['text'] = '🚩'
            cur_btn['disabledforeground'] = 'red'
            self.marked_mines += 1
        elif cur_btn['text'] == '🚩':
            cur_btn['text'] = ''
            cur_btn['state'] = 'normal'
            self.marked_mines -= 1
        self.update_marked_mines_label()

    def start_timer(self):
        if not MineSweeper.IS_GAME_OVER:
            self.elapsed_time += 1
            self.update_elapsed_time_label()
            self.window.after(1000, self.start_timer)


    # Обробка кліків:
    # Для початку, якщо гра закінчена, то нічого не відбувається

    # Якщо це перший клік, то генерується поле так, щоб перший клік 'не попав' на бомбу

    # Якщо кнопка, яка нажав гравець була міною, то гра закінчується

    # В противному випадку, якщо нажата кнопка не є міною, то застосовується алгоритм обходу в ширину
    # який показує к-ть мін, поблизу, якщо вони є, та робить кнопку неактиввною для нажаття, та врешті решт 
    # перевіряє чи гравець виграв після цього коду, якщо ні, то гра продовжується
    def click(self, clicked_button: MyButton):
        if MineSweeper.IS_GAME_OVER:
            return

        if MineSweeper.IS_FIRST_CLICK:
            self.insert_mines(clicked_button.number)
            self.count_mines_in_buttons()
            self.print_buttons()
            MineSweeper.IS_FIRST_CLICK = False

        if clicked_button.is_mine:
            clicked_button.config(text='*', background='red', disabledforeground='black')
            clicked_button.is_open = True
            MineSweeper.IS_GAME_OVER = True
            showinfo('Game over', 'Ви програли')
            for i in range(1, MineSweeper.ROW + 1):
                for j in range(1, MineSweeper.COLUMNS + 1):
                    btn = self.buttons[i][j]
                    if btn.is_mine:
                        btn['text'] = '*'
        else:
            color = colors.get(clicked_button.count_bomb, 'black')
            clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
            if clicked_button.count_bomb:
                clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
                clicked_button.is_open = True
            else:
                self.breadth_first_search(clicked_button)
        clicked_button.config(state='disabled')
        clicked_button.config(relief=tk.SUNKEN)
        self.check_game_finished()

    # Алгоритм обходу в ширину
    def breadth_first_search(self, btn: MyButton):
        # Створюємо чергу для збереження кнопок, які потрібно обробити
        quene = [btn]
        while quene:
        # Виймаємо перший елемент з черги
            cur_btn = quene.pop()
        
            # Визначаємо колір для тексту кнопки в залежності від кількості мін навколо
            color = colors.get(cur_btn.count_bomb, 'black')
        
            # Встановлюємо текст на кнопці відповідно до кількості мін навколо
            if cur_btn.count_bomb:
                cur_btn.config(text=cur_btn.count_bomb, disabledforeground=color)
            else:
                cur_btn.config(text='', disabledforeground=color)
        
            # Позначаємо кнопку як відкриту
            cur_btn.is_open = True
        
            # Вимикаємо кнопку (робимо її неактивною)
            cur_btn.config(state='disabled')
        
            # Змінюємо стиль кнопки для візуального ефекту
            cur_btn.config(relief=tk.SUNKEN)

            # Якщо навколо поточної кнопки немає мін, розглядаємо її сусідів
            if cur_btn.count_bomb == 0:
                x, y = cur_btn.x, cur_btn.y
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        next_btn = self.buttons[x + dx][y + dy]
                        # Перевіряємо, чи сусідня кнопка ще не відкрита і не перебуває за межами ігрового поля
                        if not next_btn.is_open and 1 <= next_btn.x <= MineSweeper.ROW and \
                                1 <= next_btn.y <= MineSweeper.COLUMNS and next_btn not in quene:
                            # Додаємо сусідню кнопку в чергу для подальшої обробки
                            quene.append(next_btn)

    # Метод викликається при нажатті копнки 'Грати' у меню
    def reload(self):
        # Тут викликається метод destroy() для видалення всіх елементів вікна
        [child.destroy() for child in self.window.winfo_children()]
        self.__init__()
        # Та переоприділяється вікно, створюється нове
        self.create_widgets()
        MineSweeper.IS_FIRST_CLICK = True
        MineSweeper.IS_GAME_OVER = False

    # Меню налаштування гри
    def create_settings_window(self):
        win_settings = tk.Toplevel(self.window)
        win_settings.wm_title('Налаштування')

        tk.Label(win_settings, text='Кількість рядів').grid(row=0, column=0)
        row_entry = tk.Entry(win_settings)
        row_entry.insert(0, MineSweeper.ROW)
        row_entry.grid(row=0, column=1, padx=20, pady=20)

        tk.Label(win_settings, text='Кількість колонок').grid(row=1, column=0)
        column_entry = tk.Entry(win_settings)
        column_entry.insert(0, MineSweeper.COLUMNS)
        column_entry.grid(row=1, column=1, padx=20, pady=20)
        
        tk.Label(win_settings, text='Кількість мін').grid(row=2, column=0)
        mines_entry = tk.Entry(win_settings)
        mines_entry.insert(0, MineSweeper.MINES)
        mines_entry.grid(row=2, column=1, padx=20, pady=20)

        save_btn = tk.Button(win_settings, text='Застосувати',
                             command=lambda: self.change_settings(row_entry, column_entry, mines_entry))
        save_btn.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

    # Так як введені значення будуть строковими, перетворюємо їх в int,
    # а якщо це не можливо, то виводимо помилку
    # після успішного перетворення значень в числа,
    # вставляючи у відповідні атрибути класу MineSweeper значення, перемальовуємо гру
    def change_settings(self, row: tk.Entry, column: tk.Entry, mines: tk.Entry):
        try:
            int(row.get()), int(column.get()), int(mines.get())
        except ValueError:
            showerror('Помилка', 'Ви ввели неправильне значення')
            return

        MineSweeper.ROW = int(row.get())
        MineSweeper.COLUMNS = int(column.get())
        MineSweeper.MINES = int(mines.get())
        self.reload()

    # Основні віджети гри
    def create_widgets(self):
        
        # Меню
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)

        setting_menu = tk.Menu(menubar, tearoff=0)
        setting_menu.add_command(label='Грати', command=self.reload)
        setting_menu.add_command(label='Налаштування', command=self.create_settings_window)
        setting_menu.add_command(label='Вихід', command=self.window.destroy)
        menubar.add_cascade(label='Меню', menu=setting_menu)

        # Розташовування кнопок
        count = 1

        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                btn.number = count
                btn.grid(row=i, column=j, stick='NWES')
                count += 1

        for i in range(1, MineSweeper.ROW + 1):
            tk.Grid.rowconfigure(self.window, i, weight=1)

        for i in range(1, MineSweeper.COLUMNS + 1):
            tk.Grid.columnconfigure(self.window, i, weight=1)
        
        # Був створений Фрейм (нижня полоска під кнопками), як окремий відділ вікна, щоб текст впливав на ширину самого вікна
        self.info_frame = tk.Frame(self.window)
        self.info_frame.grid(row=MineSweeper.ROW + 2, column=1, columnspan=MineSweeper.COLUMNS, padx=10, pady=10, sticky='w')

        self.marked_mines_label = tk.Label(self.info_frame, text="Ви поки що не відмічали міни")
        self.marked_mines_label.grid(row=0, column=0, padx=10)

        self.elapsed_time_label = tk.Label(self.info_frame, text="Час: 0 сек")
        self.elapsed_time_label.grid(row=0, column=1, padx=10)

    
    # Проходимось по всіх кнопках, та робимо їх відкритими, у разі виграшу, або програшу
    def open_all_buttons(self):
        for i in range(MineSweeper.ROW + 2):
            for j in range(MineSweeper.COLUMNS + 2):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    btn.config(text='*', background='red', disabledforeground='black')
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, 'black')
                    btn.config(text=btn.count_bomb, fg=color)

    # Метод перевіряє, чи гра завершена, тобто були відкриті всі кнопки, окрім мін
    def check_game_finished(self):
        all_opened = True
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                if not btn.is_mine and not btn.is_open:
                    all_opened = False
                    break
        if all_opened:
            self.open_all_buttons()
            showinfo('Game Over', 'Ви виграли! Вітаємо!')
            MineSweeper.IS_GAME_OVER = True

    def start(self):
        self.create_widgets()
        self.start_timer()
        MineSweeper.window.mainloop()

    # Консольний вивід ігрового поля
    def print_buttons(self):
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    print('B', end=' ')
                else:
                    print(btn.count_bomb, end=' ')
            print()

    # Метод реалізовує 'вставку' мін на ігрове поле після першого кліку,
    # та записує в атрибут is_mine інформацію про кнопку MyButton
    def insert_mines(self, number: int):
        index_mines = self.get_mines_places(number)
        print(index_mines)
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                if btn.number in index_mines:
                    btn.is_mine = True

    # Метод реалізує розрахунок кількості мін, які оточують кожну кнопку на ігровому полі, та зберігає в атрибут count_bomb класу MyButton
    def count_mines_in_buttons(self):
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                count = 0
                btn = self.buttons[i][j]
                # Тут проходимось по сусідам зі всіх сторін
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if self.buttons[i + dx][j + dy].is_mine:
                            count += 1
                btn.count_bomb = count

    # Генерація індексів для розташування мін на полі (зокрема для того, що не була накладка мін)
    def get_mines_places(self, number: int) -> list:
        lst = [i for i in range(1, MineSweeper.ROW * MineSweeper.COLUMNS + 1)]
        lst.remove(number)
        shuffle(lst)
        return lst[:MineSweeper.MINES]


if __name__ == '__main__':
    minesweeper = MineSweeper()
    minesweeper.start()
