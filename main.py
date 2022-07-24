__author__ = "Benjamin Mickler"
__copyright__ = "Copyright 2022, Benjamin Mickler"
__credits__ = ["Benjamin Mickler"]
__license__ = "GPLv3 or later"
__version__ = "230720222"
__maintainer__ = "Benjamin Mickler"
__email__ = "ben@benmickler.com"

"""
Hangman is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

Hangman is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
Hangman. If not, see <https://www.gnu.org/licenses/>.
"""

import sys
import random
import tkinter as tk
import tkinter.messagebox
from tkinter import simpledialog
from help_message import HELP_MESSAGE
import stages

class cli_game:
    def __init__(self):
        self.name = input("Name: ")
        self.word = input("Word: ")
        self.guessed_letters = []
        self.stage = -1
    def start(self):
        while True:
            self.guessed = True
            if self.stage == 7:
                print(f"\033[91mYou have run out of attempts. The man is dead.\033[0m")
                break
            guess = input("Guess a letter: ")
            if guess == "exit":
                break
            if len(guess) != 1:
                print("You must guess one letter")
                continue
            if guess not in self.word:
                self.stage += 1
            print(getattr(stages, f"s{self.stage}"))
            for i in self.word:
                if i in self.guessed_letters:
                    print("\033[4m"+i+"\033[0m", end="")
                elif i == guess:
                    self.guessed_letters.append(guess)
                    print("\033[4m"+i+"\033[0m", end="")
                else:
                    print("_", end="")
                    self.guessed = False
            print()
            if self.guessed == True:
                print(f"\033[92mCongratulations {self.name}, you guessed the word!\033[0m")
                break
class gui_game:
    def __init__(self):
        self.game_done = False
        self.guessed_letters = []
        self.stage = -1
        self.window = tk.Tk()
        self.window.title("Hangman")
        self.window.tk.call('wm', 'iconphoto', self.window._w, tk.PhotoImage(file='logo.png'))
        self.window.minsize(400, 200)
        self.window.bind('<Return>', self.guess)
        guess_label = tk.Label(text="Guess:")
        self.guess_entry = tk.Entry()
        guess_label.pack()
        self.guess_entry.pack()
        self.guess_button = tk.Button(text="Guess")
        self.guess_button.pack()
        self.help_button = tk.Button(text="Help", command=self.show_help_dialog)
        self.help_button.pack()
        self.guess_button.bind("<Button-1>", self.guess)
        self.label = tk.Text()
        self.label.pack()
        self.name = simpledialog.askstring(title="Hangman", prompt="What's your name?")
        if self.name == None:
            raise SystemExit
        self.word = simpledialog.askstring(title="Hangman", prompt="Word:")
        if self.word == None:
            raise SystemExit
        lbl_txt = ""
        for i in self.word:
            lbl_txt += "_ "
        self.label.config(state='normal')
        self.label.delete(0.0, 'end')
        self.label.insert('end', lbl_txt)
        self.label.config(state='disabled')
        self.guess_entry.focus()
        self.window.mainloop()
    def guess(self, event):
        if self.game_done == True:
            self.guessed_letters = []
            self.stage = -1
            self.label.config(state='normal')
            self.label.delete(0.0, 'end')
            self.label.insert('end', "")
            self.label.config(state='disabled')
            self.guess_entry["state"] = "normal"
            self.guess_entry.delete(0, 'end')
            self.guess_button.config(text="Guess")
            self.game_done = False
            self.word = simpledialog.askstring(title="Hangman", prompt="Word:")
            if self.word == None:
                raise SystemExit
            lbl_txt = ""
            for i in self.word:
                lbl_txt += "_ "
            self.label.config(state='normal')
            self.label.delete(0.0, 'end')
            self.label.insert('end', lbl_txt)
            self.label.config(state='disabled')
        else:
            self.guessed = True
            lbl_txt = ""
            if self.stage == 7:
                lbl_txt += f"You have run out of attempts. The man is dead."
                self.label.config(state='normal')
                self.label.delete(0.0, 'end')
                self.label.insert('end', lbl_txt)
                self.label.config(state='disabled')
                self.guess_entry.delete(0, 'end')
                self.guess_entry["state"] = "disabled"
                self.guess_button.config(text="Reset")
                self.game_done = True
            else:
                guess = self.guess_entry.get()
                if len(guess) != 1:
                    tkinter.messagebox.showerror("Invalid guess", "You must guess one letter")
                    self.guess_entry.delete(0, 'end')
                else:
                    if guess not in self.word:
                        self.stage += 1
                    if self.stage != -1:
                        lbl_txt += getattr(stages, f"s{self.stage}")+"\n"
                    for i in self.word:
                        if i in self.guessed_letters:
                            lbl_txt += f"{i} "
                        elif i == guess:
                            self.guessed_letters.append(guess)
                            lbl_txt += f"{i} "
                        else:
                            lbl_txt += "_ "
                            self.guessed = False
                    if self.guessed == True:
                        lbl_txt += f"\n\nCongratulations {self.name}, you guessed the word!"
                        self.guess_button.config(text="Reset")
                        self.guess_entry.delete(0, 'end')
                        self.guess_entry["state"] = "disabled"
                        self.game_done = True
                    self.label.config(state='normal')
                    self.label.delete(0.0, 'end')
                    self.label.insert('end', lbl_txt)
                    self.label.config(state='disabled')
                    self.guess_entry.delete(0, 'end')
    def show_help_dialog(self):
        aboutdialog = AboutDialog(self.window)
        self.window.wait_window(aboutdialog.top)

class AboutDialog:
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        self.about_text = tk.Text(top)
        self.about_text.pack()
        self.about_text.config(state='normal')
        self.about_text.insert('end', HELP_MESSAGE)
        self.about_text.config(state='disabled')
        self.close_button = tk.Button(top, text='Close', command=self.top.destroy)
        self.close_button.pack()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1].lower() in ["-h", "--help", "help"]:
            print(HELP_MESSAGE)
            raise SystemExit
        elif sys.argv[1].lower() in ["-g", "--gui", "gui"]:
            gui_game()
        elif sys.argv[1].lower() in ["-c", "--cli", "cli"]:
            cli_game().start()
        else:
            print("Invalid arguments, use --help for help")
    else:
        print("Not enough arguments, use --help for help")