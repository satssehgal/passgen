import string, random

while True:
	try:
		passwordlength=int(input('Desired Password Length: '))
		break
	except ValueError:
		print('Please Enter a Number')

while True:
	try:
		yourchoice = int(input('1 - Text Only \n2 - Numbers Only \n3 - Alphanumeric \n4 - Alphanumeric with special characters\n\nPlease select a choice: '))
		if yourchoice ==1:
			pw=''.join(random.choice(string.ascii_letters) for _ in range(passwordlength))
			break
		elif yourchoice ==2:
			pw=''.join(random.choice(string.digits) for _ in range(passwordlength))
			break
		elif yourchoice ==3:
			pw=''.join(random.choice(string.ascii_letters+string.digits) for _ in range(passwordlength))
			break
		elif yourchoice ==4:
			pw=''.join(random.choice(string.ascii_letters+string.digits+string.punctuation) for _ in range(passwordlength))
			break
		else:
			print('\nWrong Selection. Please select a number from the list \n')
	except ValueError: 
		print('\nPlease Enter a Number\n')
print('Here is a password for you: ',pw)

