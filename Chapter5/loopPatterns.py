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

#-----------------------------------------------------

# maximum and minimum loops

largest = None    # Note - <None> keyword - marks variable as empty
print 'Before: ', largest
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print 'Loop: ', itervar, largest
print 'Largest: ', largest


smallest = None
print 'Before: ', smallest
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print 'Loop: ', itervar, smallest
print 'Smallest: ', smallest