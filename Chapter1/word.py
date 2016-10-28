#**************************************
#* this script counts the words in a 
#*  file and returns to the screen 
#*  the most common word
# 
# cd C:\Users\berni\Documents\PYTHON_LEARNING\Chapter1\words.py
#
#**************************************

# get the name of the file and open it
name = raw_input('Enter file:')
handle = open(name, 'r')
text = handle.read()
words = text.split()

# count words
counts = dict()
for word in words:
	counts[word] = counts.get(word,0) + 1

# find the most common word
bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print bigword,bigcount