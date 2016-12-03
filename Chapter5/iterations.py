###################################################################
#
#  file holds examples from Chapter 5 of Python Informatics
#
# -------- Looping Patterns Keywords -----------
#
#      
#      while loop:  generally is an indefinite loop
#                   executes until a condition is FALSE
#      
#      for loop:  is a definite loop
#        - executes through a definite set
#      True key word:   ...
#
#      break key word: use break to exit a loop when you have
#                      reached the exit condition
#      continue key word: ends the current iteration and jumps...
#
###################################################################


# n is our iteration variable - 
# which controls how many times the loop runs
# note - this would be an infinite loop if I change 
# n = n - 1   to  n = n + 1
# or if I didn't change the iteration variable

n = 5

while n >0:
    print n
    n = n - 1

print 'Blastoff!'
print n

#-----------------------

n = 25
x = 1

while x > n:
    print n
    x = x+1

print 'Blastoff!'
print n

#----------------------

while True:
    line = raw_input('>')
    if line == 'done':
        break
    print line  # this line does not execute if break
print 'Done!'

#------------------------
# the <continue> statement ends the current iteration and jumps to the 
# top of the loop and starts the next iteration
# don't stop this loop - advance to the next iteration
# so pattern can be - while True - if...continue - else - finish loop via if.. break
# continue skips the second if

while True:
    line = raw_input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print line
print 'Done!'

#---------------------------

for i in [5,4,3,2,1]:
    print i

print 'Blastoff!'

#-------------------------------

friends = ['Joseph', 'Glenn', 'Sally']
for x in friends:                      # note 'x' is called the iteration variable
    print 'Happy New Year:', x
print 'All Done with Friends2'




