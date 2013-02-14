""" 
~   nailpolish.py
~	Writes a little piece of poetry stirring Essie beautiful nail colors.
~	Created by Sabrina Matrullo on 2013-02-14 
~ 	Happy valentine's day :)
~
"""

import urllib2, sys, random, re
from bs4 import BeautifulSoup

try:
	person = sys.argv[1]
except IndexError :
	person = str(raw_input("Please enter someone to nailpolish : "))

# get essie html 
url = "http://www.essie.com/nail-colors"
response = urllib2.urlopen(url)
html = response.read()

# making the soup
soup = BeautifulSoup(html)
soup = soup.find_all('option')

# fetching colors
colors = []
for option in soup[1:]:
	if str(option).find('colors'):	
		colors.append(option.string.encode('utf8', 'replace').strip().lower())

repeat = False
for key, char in enumerate(person):
	
	# just wrote two sentences from a character that's gonna repeat itself
	if repeat and char == person[key-1]: continue

	if key == len(person)-1: 
		repeat = False
	else: 
		repeat = False if char != person[key+1] else True

	# picking up colors
	charColorMatch = []
	p = re.compile('^'+char.lower())
	for color in colors: 
		if p.match(color): 
			charColorMatch.append(color)
	lColor = len(charColorMatch)

	if lColor > 1:  
		# how many colors do we need and can we use at a time ?
		rand = []
		if lColor == 2: lRand = 2			
		elif lColor > 3 and not repeat: lRand = 3
		else: lRand = 6

		if lColor < lRand:
			for i in range(0,lColor): 
				rand.append(i)
		else:
			while len(rand) < lRand :
				number = random.randint(0, lColor-1)
				if rand.count(number) == 0:	
					rand.append(number)
	
		# generating essie poetry 
		if lRand == 3:
			print char.upper() + charColorMatch[rand[0]][1:] + ' ' + charColorMatch[rand[1]] + ', ' + charColorMatch[rand[2]]
		elif lRand == 2:
			if not repeat:
				print charColorMatch[rand[0]][:1].upper() + charColorMatch[rand[0]][1:] + ' ' + charColorMatch[rand[1]]	
			else:  # two colors only match this repeating char, pretty boring : let's just invert colors for the second sentence
				print char.upper() + charColorMatch[rand[0]][1:] + ' ' + charColorMatch[rand[1]] 
				print char.upper() + charColorMatch[rand[1]][1:] + ', ' + char.upper() + charColorMatch[rand[0]][1:]
 		else:
			print char.upper() + charColorMatch[rand[0]][1:] + ' ' + charColorMatch[rand[1]] + ', ' + charColorMatch[rand[2]]
			print char.upper() + charColorMatch[rand[3]][1:] + ' ' + charColorMatch[rand[4]] + ', ' + charColorMatch[rand[5]]
	elif lColor == 1:  
		if not repeat:
			print char.upper() + charColorMatch[0][1:] 
		else: 	# pff come on, not gonna happen, who's name has a double 'u' inside ?
			print char.upper() + charColorMatch[0][1:] 
			j = len(charColorMatch[0])-1
			while j >= 0:
				sys.stdout.write(charColorMatch[0][j]) if not j == len(charColorMatch[0])-1 else sys.stdout.write(charColorMatch[0][j].upper()) 
				j -= 1
			sys.stdout.write('\n')
	else: continue 	
