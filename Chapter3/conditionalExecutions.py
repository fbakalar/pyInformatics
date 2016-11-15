# Chapter 3 from PyInformatics
# All about conditional executions

x = 11
y = 11

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



# Chained conditionals

if x < y :
	print 'x is less than y'
elif x > y :
	print 'x is greater than y'
else :
	print 'x and y are equal'