#programme interactive
#Andrew sommative
print("hello")
print("do you want to play a game")
y = input()# input is for when you want the user to imput something from their keyboard
yes = "ok"
no = "bye"

if y == "yes":#start 
  print("then lets begin")
elif y == "no":
 print("bye")

if y == "yes":
  print("ok then question 1")# 1st question
  print("who is batman A)little wayne B)big wayne C)bruce wayne")
  answer = input().lower()# lower aloyes you to put lowercase letter as an answer if everything was uppercase
  if answer == "a":
    print("no thats a talentless rapper")
  elif answer == "b":
    print("close but not quite")
elif answer == "c":
    print(" yes that is correct ")

if answer == "c":
  print("good answer question 2")# 2nd question
  print("who is bruce waynes butler D)alfred dimetime E) afred pennyworth F) alfred nickelback")
  answer = input().lower()
  if answer == "d":
    print("no try again")
  elif answer == "e":
    print ("good anakin good")
  elif answer == "f":
    print("ha funny")

  if answer == "e":
    print ("ok question 3")# 3rd question
    print("who took andre's porridge A)mother B)mom C)mammy")
    answer = input().lower()
  if answer == "a":
    print("i hope you run into a creeper at night")
  elif answer == "b":
    print ("get destroyed pleb")
  elif answer == "c":
    print("correct")

  if answer == "c":
    print ("you won")