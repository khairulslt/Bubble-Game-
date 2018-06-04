import os
import sys
import string
import random
import time
from time import sleep #to get program to "sleep" to simulate loading
import pyperclip #to copy paste from terminal

# Used to simulate loading progress of the main program
start_loading = '\n\n\n\nLoading'
loading = '.' * 120 + '\n\n'

#clears the IDLE
os.system('cls') #for windows

# use the next line if you are on linux
# os.system('clear') 

#use input() so user has to type enter for next line to appear
userInput = ''
input("Welcome to the password generator! Hit <enter> to continue!")
input("You have two options for your password:")
input("1) Pick a word of your choice, your password will be based on the word you choose.")
input("2) Use a completely randomized password chosen by this application. (Note: Safer Choice)")


while(userInput != '1' or '2'):
	userInput = input("Type in '1' or '2' without the quotation marks - followed by <enter> to continue \n\n")
	os.system('cls')
	if(userInput == '2'):
		#user selects input length of password
		pwlength = int(input("How many characters do you want your password to be: "))

		os.system('cls')

		# Used to simulate loading progress of the main program
		print(start_loading)
		for c in loading:
		    print(c, end = '')
		    sys.stdout.flush()
		    sleep(0.025)

		#Clear the IDE...
		os.system('cls')

		#initialize full range of characters on keyboard
		pwchar = string.ascii_letters + string.punctuation + string.digits

		#initialize "password" as empty string to use in for loop
		password2 = ""

		#for loop - add random characters to create password
		for x in range(pwlength):
		    char = random.choice(pwchar)
		    password2 += char

		print("Your password is:")
		print(password2 + "\n\n")
		pyperclip.copy(password2)
		pyperclip.paste()
		print("Password has been copied to your clipboard... Hit <ctrl-v> to show!")
		input("Hit <enter> to end this program")
		break

	elif(userInput == '1'):
		while True: # use while true loop to force user to input value
			userChoice = input("Enter your word of choice here: \n")
			if userChoice: break
		endword = ""

		os.system('cls')

		# Used to simulate loading progress of the main program
		print(start_loading)
		for c in loading:
		    print(c, end = '')
		    sys.stdout.flush()
		    sleep(0.025)

		os.system('cls')

		for k in userChoice:
		  endword+="".join(random.choice([k.upper(), k]))

		password1 = endword + random.choice(string.digits) + random.choice(string.digits)
		print("Your password is: \n" + password1 + "\n\n")
		pyperclip.copy(password1)
		pyperclip.paste()
		print("Password has been copied to your clipboard... Hit <ctrl-v> to show!")
		input("Hit <enter> to end this program")
		break
	else:
		print("You have entered an invalid option")
	
		


