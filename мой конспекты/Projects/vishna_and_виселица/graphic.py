import tkinter as tk

class Graphic:
    def __init__(self, root):
        self.root = root
        self.word_label = None
        self.attempts_label = None
        self.canvas = None
        self.guess_entry = None
        self.guess_button = None
        self.play_again_button = None
        self.exit_button = None
        self.play_button = None
        self.category_label = None
        self.category_frame_buttons = None
        self.main_frame = None
        self.category_frame = None
        self.game_frame = None

        self.create_widgets()
        self.display_main_screen()

    def create_widgets(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

        self.title_label = tk.Label(self.main_frame, text="Виселица", font=("Helvetica", 24))
        self.title_label.pack()

        self.play_button = tk.Button(self.main_frame, text="Играть", font=("Helvetica", 18))
        self.play_button.pack()

        self.exit_button = tk.Button(self.main_frame, text="Выход", font=("Helvetica", 18))
        self.exit_button.pack()

        self.category_frame = tk.Frame(self.root)
        self.category_frame.pack_forget()

        self.category_label = tk.Label(self.category_frame, text="Выберите категорию:", font=("Helvetica", 18))
        self.category_label.pack()

        self.category_frame_buttons = tk.Frame(self.category_frame)
        self.category_frame_buttons.pack()

        self.animals_button = tk.Button(self.category_frame_buttons, text="Животные", font=("Helvetica", 18))
        self.animals_button.pack(side=tk.LEFT, padx=10)

        self.fruits_button = tk.Button(self.category_frame_buttons, text="Фрукты", font=("Helvetica", 18))
        self.fruits_button.pack(side=tk.LEFT, padx=10)

        self.cities_button = tk.Button(self.category_frame_buttons, text="Города", font=("Helvetica", 18))
        self.cities_button.pack(side=tk.LEFT, padx=10)

        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack_forget()

        self.word_label = tk.Label(self.game_frame, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=10)

        self.attempts_label = tk.Label(self.game_frame, text="", font=("Helvetica", 18))
        self.attempts_label.pack()

        self.canvas = tk.Canvas(self.game_frame, width=200, height=200)
        self.canvas.pack()

        self.guess_entry = tk.Entry(self.game_frame, font=("Helvetica", 18))
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.game_frame, text="Угадать", font=("Helvetica", 18))
        self.guess_button.pack()

        self.play_again_button = tk.Button(self.game_frame, text="Играть снова", font=("Helvetica", 18))
        self.play_again_button.pack_forget()

    def display_main_screen(self):
        self.main_frame.pack()
        self.category_frame.pack_forget()
        self.game_frame.pack_forget()

    def display_category_screen(self):
        self.main_frame.pack_forget()
        self.category_frame.pack()
        self.game_frame.pack_forget()

    def display_game_screen(self):
        self.main_frame.pack_forget()
        self.category_frame.pack_forget()
        self.game_frame.pack()

    def display_word(self, word, guessed_letters):
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        self.word_label.config(text=display)

    def display_attempts(self, attempts):
        self.attempts_label.config(text="Осталось попыток: " + str(attempts))
        self.canvas.delete("all")
        if attempts <= 6:
            self.canvas.create_line(50, 150, 150, 150)  # основа
        if attempts <= 5:
            self.canvas.create_line(100, 150, 100, 50)  # столб
        if attempts <= 4:
            self.canvas.create_line(100, 50, 150, 50)  # перекладина
        if attempts <= 3:
            self.canvas.create_line(150, 50, 180, 70)  # голова
        if attempts <= 2:
            self.canvas.create_line(150, 70, 150, 120)  # тело
        if attempts <= 1:
            self.canvas.create_line(150, 120, 130, 140)  # левая рука
            self.canvas.create_line(150, 120, 170, 140)  # правая рука
            self.canvas.create_line(150, 140, 130, 160)  # левая нога
            self.canvas.create_line(150, 140, 170, 160)  # правая нога