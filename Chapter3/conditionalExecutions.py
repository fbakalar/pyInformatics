# Chapter 3 from PyInformatics
# All about conditional executions

x = 11
y = 14

if x > 0: 
    print 'x is positive'


if x%2==0:
    print 'x is divisible by 2'
else :
	print 'x is an odd number'

if x%3==0:
	print 'x is divisible by 3'
else :
	print 'x is NOT divisible by 3'

if x < 0:
	pass    #need to handle negative values???


# using <and>

if 0 < x and x < y :
    print 'x is a positive number and less than y'


# -----------------------------------------------------------------
# Chained conditionals

if x < y :
	print 'x is less than y'
elif x > y :
	print 'x is greater than y'
else :
	print 'x and y are equal'


print '\n'

prompt = '?>>'

print 'what letter am I thinking of? \n '
letter = raw_input(prompt)

if letter == 'a' :
    print 'nope'
elif letter == 'b' :
    print 'no sir'
elif letter == 'c' :
	print 'BINGO!!'

#-------------------------------------------------------------------
# Nested Conditionals

if x == y:
    print 'x and y are equal'
else:
    if x < y:
        print 'x is less than y'
    else:
        print 'x is greater than y'







