#programme interactive
#Andrew sommative
print("hello")
print("do you want to play a game")
y = input()
yes = "ok"
no = "bye"
if y == "yes":
  print("then lets begin")
import random
import radiant
correct = random.radiant(1, 10)
guess = input("Enter your guess: ")
while guess != correct:
	if guess > correct:
		print("You've guessed too high. Try guessing lower.")
else:
	print("You've guessed too low. Try guessing higher.")
guess = int(input("Enter your guess: "))
print("Congratulations! You've guessed correctly.")
