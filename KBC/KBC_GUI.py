import tkinter as tk
from tkinter import messagebox
import random

class KBCGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaun Banega Crorepati")
        self.root.geometry("800x600")
        
        self.main_menu()

    def main_menu(self):
        self.clear_frame()
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        tk.Label(self.frame, text="Kaun Banega Crorepati", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.frame, text="Start Game", command=self.start_game, width=20).pack(pady=10)
        tk.Button(self.frame, text="Exit", command=self.root.quit, width=20).pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_game(self):
        self.clear_frame()
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.level = 1
        self.wrong_attempts = 0
        self.rand_list = []

        self.question_label = tk.Label(self.frame, text="", font=("Arial", 18), wraplength=600)
        self.question_label.pack(pady=20)

        self.options = []
        for i in range(4):
            button = tk.Button(self.frame, text="", font=("Arial", 16), width=20, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.options.append(button)

        self.next_question()

    def next_question(self):
        if self.level == 1:
            self.correct_answer = self.EASY_QUESTION_BANK()
        elif self.level == 2:
            self.correct_answer = self.INTERMEDIATE_QUESTION_BANK()
        else:
            self.correct_answer = self.ULTIMATE_QUESTION_BANK()

    def check_answer(self, selected_option):
        if selected_option == ord(self.correct_answer) - ord('a'):
            self.level += 1
            if self.level > 3:
                messagebox.showinfo("Congratulations!", "You've won the game!")
                self.main_menu()
            else:
                self.next_question()
        else:
            self.wrong_attempts += 1
            if self.wrong_attempts >= 3:
                self.game_over_func()
            else:
                self.next_question()

    def EASY_QUESTION_BANK(self):
        questions = [
            "What is the capital of France?",
            "What is 2 + 2?",
            "What is the color of the sky?",
            "Which animal is known as the King of the Jungle?",
            "What is the primary ingredient in bread?"
        ]
        options = [
            ["London", "Berlin", "Paris", "Madrid"],  # Correct: Paris
            ["3", "4", "5", "6"],  # Correct: 4
            ["Blue", "Green", "Red", "Yellow"],  # Correct: Blue
            ["Elephant", "Tiger", "Lion", "Giraffe"],  # Correct: Lion
            ["Flour", "Sugar", "Salt", "Water"]  # Correct: Flour
        ]
        correct_option = [
            "c",  # Paris
            "b",  # 4
            "a",  # Blue
            "c",  # Lion
            "a"  # Flour
        ]

        _rand = random.randrange(0, len(questions))
        while _rand in self.rand_list:
            _rand = random.randrange(0, len(questions))
        self.rand_list.append(_rand)

        self.question_label.config(text=questions[_rand])
        for i, option in enumerate(options[_rand]):
            self.options[i].config(text=option)

        return correct_option[_rand]

    def INTERMEDIATE_QUESTION_BANK(self):
        questions = [
            "Which country is known as the Land of the Rising Sun?",
            "What is the smallest country in the world?",
            "Who wrote 'Romeo and Juliet'?",
            "Which is the hardest natural substance on Earth?",
            "Which planet is known as the Red Planet?",
            "What is the capital of Australia?",
            "Who painted the Mona Lisa?",
            "What is the longest river in the world?",
            "What is the largest mammal in the world?",
            "What is the square root of 64?",
            "What is the chemical symbol for gold?",
            "Which country is the largest by area?",
            "Who is known as the Father of Computers?",
            "What is the main ingredient in guacamole?",
            "Which element has the atomic number 1?",
            "What is the tallest mountain in the world?",
            "Who developed the theory of relativity?",
            "What is the capital of Canada?",
            "Who is known as the Iron Lady?",
            "What is the largest ocean on Earth?"
        ]
        options = [
            ["China", "Japan", "South Korea", "India"],  # Correct: Japan
            ["Monaco", "Vatican City", "San Marino", "Liechtenstein"],  # Correct: Vatican City
            ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],  # Correct: William Shakespeare
            ["Diamond", "Gold", "Iron", "Platinum"],  # Correct: Diamond
            ["Earth", "Venus", "Mars", "Jupiter"],  # Correct: Mars
            ["Sydney", "Melbourne", "Canberra", "Perth"],  # Correct: Canberra
            ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],  # Correct: Leonardo da Vinci
            ["Amazon", "Nile", "Yangtze", "Mississippi"],  # Correct: Nile
            ["Elephant", "Blue Whale", "Giraffe", "Orca"],  # Correct: Blue Whale
            ["6", "7", "8", "9"],  # Correct: 8
            ["Au", "Ag", "Pb", "Fe"],  # Correct: Au
            ["Canada", "Russia", "China", "USA"],  # Correct: Russia
            ["Alan Turing", "Charles Babbage", "John von Neumann", "Bill Gates"],  # Correct: Charles Babbage
            ["Tomato", "Avocado", "Potato", "Carrot"],  # Correct: Avocado
            ["Oxygen", "Hydrogen", "Nitrogen", "Helium"],  # Correct: Hydrogen
            ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],  # Correct: Mount Everest
            ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"],  # Correct: Albert Einstein
            ["Toronto", "Vancouver", "Ottawa", "Montreal"],  # Correct: Ottawa
            ["Margaret Thatcher", "Angela Merkel", "Indira Gandhi", "Golda Meir"],  # Correct: Margaret Thatcher
            ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"]  # Correct: Pacific Ocean
        ]
        correct_option = [
            "b",  # Japan
            "b",  # Vatican City
            "a",  # William Shakespeare
            "a",  # Diamond
            "c",  # Mars
            "c",  # Canberra
            "a",  # Leonardo da Vinci
            "b",  # Nile
            "b",  # Blue Whale
            "c",  # 8
            "a",  # Au
            "b",  # Russia
            "b",  # Charles Babbage
            "b",  # Avocado
            "b",  # Hydrogen
            "a",  # Mount Everest
            "b",  # Albert Einstein
            "c",  # Ottawa
            "a",  # Margaret Thatcher
            "d"  # Pacific Ocean
        ]

        _rand = random.randrange(0, len(questions))
        while _rand in self.rand_list:
            _rand = random.randrange(0, len(questions))
        self.rand_list.append(_rand)

        self.question_label.config(text=questions[_rand])
        for i, option in enumerate(options[_rand]):
            self.options[i].config(text=option)

        return correct_option[_rand]

    def ULTIMATE_QUESTION_BANK(self):
        questions = [
            "What is the speed of light?",
            "Who is the author of 'War and Peace'?",
            "What is the capital of Iceland?",
            "What is the most abundant gas in the Earth's atmosphere?",
            "Which country is known for the martial art of Taekwondo?",
            "What is the largest organ in the human body?",
            "Who discovered penicillin?",
            "What is the main ingredient in traditional Japanese miso soup?",
            "Who is the current CEO of Tesla, Inc.?",
            "What is the smallest bone in the human body?",
            "Which planet is known for its rings?",
            "Who was the first President of the United States?",
            "What is the chemical formula for water?",
            "What is the primary language spoken in Brazil?",
            "Who wrote 'To Kill a Mockingbird'?",
            "What is the currency of Japan?",
            "What is the main component of the sun?",
            "Who is known as the 'Queen of Pop'?",
            "What is the largest desert in the world?",
            "What is the primary function of red blood cells?"
        ]
        options = [
            ["299,792,458 meters per second", "150,000,000 meters per second", "1,000,000 meters per second", "300,000 meters per second"],  # Correct: 299,792,458 meters per second
            ["Leo Tolstoy", "Fyodor Dostoevsky", "Anton Chekhov", "Ivan Turgenev"],  # Correct: Leo Tolstoy
            ["Reykjavik", "Oslo", "Helsinki", "Stockholm"],  # Correct: Reykjavik
            ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],  # Correct: Nitrogen
            ["China", "Japan", "South Korea", "Thailand"],  # Correct: South Korea
            ["Heart", "Liver", "Skin", "Lungs"],  # Correct: Skin
            ["Alexander Fleming", "Marie Curie", "Louis Pasteur", "Gregor Mendel"],  # Correct: Alexander Fleming
            ["Soybean paste", "Tofu", "Seaweed", "Fish"],  # Correct: Soybean paste
            ["Elon Musk", "Jeff Bezos", "Bill Gates", "Tim Cook"],  # Correct: Elon Musk
            ["Femur", "Stapes", "Ulna", "Tibia"],  # Correct: Stapes
            ["Mercury", "Venus", "Earth", "Saturn"],  # Correct: Saturn
            ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"],  # Correct: George Washington
            ["H2O", "CO2", "O2", "H2"],  # Correct: H2O
            ["Portuguese", "Spanish", "English", "French"],  # Correct: Portuguese
            ["Harper Lee", "J.D. Salinger", "Mark Twain", "Ernest Hemingway"],  # Correct: Harper Lee
            ["Yuan", "Yen", "Won", "Ringgit"],  # Correct: Yen
            ["Helium", "Hydrogen", "Oxygen", "Carbon"],  # Correct: Hydrogen
            ["Madonna", "Whitney Houston", "Celine Dion", "Mariah Carey"],  # Correct: Madonna
            ["Sahara", "Gobi", "Kalahari", "Antarctic"],  # Correct: Antarctic
            ["Transport oxygen", "Fight infections", "Clot blood", "Regulate temperature"]  # Correct: Transport oxygen
        ]
        correct_option = [
            "a",  # 299,792,458 meters per second
            "a",  # Leo Tolstoy
            "a",  # Reykjavik
            "b",  # Nitrogen
            "c",  # South Korea
            "c",  # Skin
            "a",  # Alexander Fleming
            "a",  # Soybean paste
            "a",  # Elon Musk
            "b",  # Stapes
            "d",  # Saturn
            "b",  # George Washington
            "a",  # H2O
            "a",  # Portuguese
            "a",  # Harper Lee
            "b",  # Yen
            "b",  # Hydrogen
            "a",  # Madonna
            "d",  # Antarctic
            "a"  # Transport oxygen
        ]

        _rand = random.randrange(0, len(questions))
        while _rand in self.rand_list:
            _rand = random.randrange(0, len(questions))
        self.rand_list.append(_rand)

        self.question_label.config(text=questions[_rand])
        for i, option in enumerate(options[_rand]):
            self.options[i].config(text=option)

        return correct_option[_rand]

    def game_over_func(self):
        self.clear_frame()
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        tk.Label(self.frame, text="Game Over", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.frame, text="Return to Main Menu", command=self.main_menu, width=20).pack(pady=10)
        tk.Button(self.frame, text="Exit", command=self.root.quit, width=20).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    game = KBCGame(root)
    root.mainloop()
