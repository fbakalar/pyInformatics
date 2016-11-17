###################################################################
#
#  file holds examples from Chapter 5 of Python Informatics
#
# -------- Looping Patterns Keywords -----------
#
#      While vs IF
#      Continue
#      For
#      True
#
###################################################################


# n is our iteration variable - 
# which controls how many times the loop runs
# note - this would be an infinite loop if i change 
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
    print line
print 'Done!'

