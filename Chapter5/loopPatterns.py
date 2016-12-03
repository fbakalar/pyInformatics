#---------------------------------------
#
#  from Chapter 5 of pyInformatics
#
#  Loop Patterns
#
#----------------------------------------


# counting and summing

# Note Python has a built in function to count a list
# len()

count = 0
for itervar in [3,41,12,9,74,15]:
    count = count + 1
print 'Count:   ',  count



#  Note Python has a built in function to sum a list
#   sum()

total = 0
for itervar in [3,41,12,9, 74, 15]:
    total = total + itervar     # sometimes variable is caaled an accumulator
print 'Total: ', total