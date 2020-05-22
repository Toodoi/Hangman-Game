import random
import webbrowser
import time
import sys
from urllib.request import urlretrieve

class HangMan:

	hangman_graphic_list = ['', '   o', '   o\n   |', '   o\n   |\n   /', '  \\o\n   |\n   /', '  \\o/\n   |\n   /', '  \\o/\n   |\n   /\\', '  \\:(/\n   |\n   /\\']
	#Gets sowpods list of words from website (word list is pretty bad.. but long)
	url = 'http://norvig.com/ngrams/sowpods.txt'
	urlretrieve(url, 'sowpods.txt')

	# Saves a random word in self.word variable
	def generate_word(self):
		with open('sowpods.txt', 'r') as words:
			word_list = list(words)
		self.word = random.choice(word_list).strip().lower()


	# Main function
	def play(self):
		self.guessed_list = []
		self.guess_count = 7
		self.draw_iteration = 0
		self.generate_word()
		self.word_display = ['_' for i in self.word]
		print('Welcome to hangman. Type \'exit\' to quit.')
		while self.guess_count > 0:
			user_input = self.valid_input()
			if user_input in self.word:
				for i in range(len(self.word)):
					if user_input == self.word[i]:
						self.word_display[i] = user_input
						if '_' not in self.word_display:
							self.win()
			else:
				self.guess_count -= 1
				self.draw_iteration += 1
				print('That letter is not in the word. You have {} more tries.\n'.format(self.guess_count))
		print(self.hangman_graphic_list[self.draw_iteration])
		self.replay = int(input('You ran out of guesses. The word was {word}.\nPress 1 to play again or 0 to exit.\n'.format(word=self.word)))
		if self.replay:
			go.play()
		else:
			sys.exit()

	# Checks whether input is valid and if so, returns the input to main function
	def valid_input(self):
		while 1:
			print(self.hangman_graphic_list[self.draw_iteration])
			print(''.join(self.word_display))
			letter = input("Please choose a letter or guess the word: ")
			if letter == self.word:
				self.win()
			if letter == 'exit':
				print('Exiting game')
				sys.exit()
			if len(letter) != 1:
				print('Input not valid. Please select one letter.\n')
				continue
			else:
				if letter in self.guessed_list:
					print('You have already guessed this letter, choose a different one.\n')
					continue
				else:
					try:
						int(letter)
						print('Input not valid. You must choose a letter.\n')
						continue
					except ValueError:
						self.guessed_list.append(letter)
						return letter

	def win(self):
		print('\nYou did it! {word} was the correct word!'.format(word=self.word.upper()))
		time.sleep(2.5)
		webbrowser.open('https://giphy.com/reactions/featured/congratulations')
		sys.exit()

go = HangMan()
go.play()
