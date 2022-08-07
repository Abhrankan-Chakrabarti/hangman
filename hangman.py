from getch import getch
from random import choice
name=input('What is your name? :\t')
print(f'Good Luck, {name}!\nGuess the word:')
with open(f"{'/'.join(__file__.split('/')[:-1])}/dictionary.txt")as file:
	word,guesses,failed,turns=choice(file.read().upper().splitlines()),'',1,7
while failed and turns:
	failed=0
	for char in word:
		if char in guesses:
			print(end=f' {char} ')
		else:
			print(end=' _ ')
			failed+=1
	print(end='\nGuess a letter :\t'if failed else '\n',flush=True)
	guess=getch().upper()if failed else ''
	print(guess if guess.isalpha()else 'Invalid character!'if failed else '')
	if guess not in guesses and guess.isalpha()and failed:
		guesses+=guess
		if guess not in word:
			turns-=1
			print(f"Wrong!\nYou have {turns} more guess{'es'if turns-1 else ''}.")
print(f'The word was: {word}.\nGame Over!')
if failed:
	print(f'Sorry {name}! You Lose! Better Luck next time')
else:
	print(f'Congratulations {name}! You Win! Keep it up!')