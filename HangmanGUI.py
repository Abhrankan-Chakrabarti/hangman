from tkinter import *
from random import choice

class Hangman:

	def __init__(self):

		self.turns = 11
		self.photos = [PhotoImage(file = f"images/hang{i}.png") for i in range(self.turns)]

	def new_game(self):

		self.turns = 11

		with open("dictionary.txt") as f:

			self.word, self.guesses, self.failed = choice(f.read().split('\n')), [], 1
		hang["image"] = ""

		self.generate("", True, f"Guess the {len(self.word)} letter word. Good luck!", "yellow")

	def draw_hang(self):

		hang["image"] = self.photos[self.turns]

	def generate(self, guess, init = False, txt = "Good job! Keep it up.", bg = "lightgreen"):

		if init or self.failed and self.turns and guess not in self.guesses:

			self.guesses.append(guess)

			if guess not in self.word:

				self.turns -= 1
				self.draw_hang()
				info["text"], info["bg"] = f"Wrong! You have {self.turns} more guess{'es'if self.turns-1 else ''}.", "red"

			else:

				self.failed, info["text"], info["bg"], txt = 0, txt, bg, ""

				for char in self.word:

					if char in self.guesses:

						txt += f" {char} "

					else:

						txt += " _ "
						self.failed += 1

				code["text"] = txt

		elif self.failed:

			info["text"], info["bg"] = f"You have already guessed {guess}", "red"

		if not (self.failed and self.turns):

			if self.failed:

				txt, bg = f"Game over! The word was {self.word}", "red"

			else:

				txt = "Congratulations, you win!"

			info["text"], info["bg"] = txt, bg

root = Tk()
root.title("Hangman")
root.minsize(width = 400, height = 400)
root.geometry("600x500")
Canvas1 = Canvas(bg = "yellow")
Canvas1.pack(expand = True, fill = BOTH)
x, y = 0.1, 0.55
Label(text = "Welcome to Hangman!", bg = "lightblue", font = "Times 12 bold").place(relx = x, rely = x / 2, relwidth = 8 * x, relheight = x)
hang = Label(bg = "yellow")
hang.place(relx = x, rely = 3 * x / 2, relwidth = 8 * x, relheight = 5 * x / 2)
code = Label(bg = "yellow", font = "Times 12 bold")
code.place(relx = x, rely = 4 * x, relwidth = 8 * x, relheight = x / 2)
info = Label(bg = "yellow", font = "Times 8 bold")
info.place(relx = x, rely = y - x / 2, relwidth = 8 * x, relheight = x / 2)
MyApp = Hangman()
MyApp.new_game()

for c in [chr(i + 65) for i in range(26)]:

	Button(text = c, command = lambda c = c: MyApp.generate(c), font = "Times 12 bold", bg = "lightblue").place(relx = x, rely = y, relwidth = 0.1, relheight = 0.1)
	x += 0.1

	if 10 * x % 9 == 0:

		x = 0.1
		y += x

Button(text = "New Game", command = MyApp.new_game, font = "Times 12 bold", bg = "lightblue").place(relx = x, rely = y, relwidth = x, relheight = x / 3)
Button(text = "Quit Game", command = root.destroy, font = "Times 12 bold", bg = "lightblue").place(relx = 2 * x, rely = y, relwidth = x, relheight = x / 3)
root.mainloop()