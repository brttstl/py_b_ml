######################
#### Assignment 1 ####
######################

# This assignment is based on day 1, day 2 and day 3 study material and has problems that will inspire you to apply
# the concepts learned during first three days, of list operations, list comprehension, bitwise operator and string
# manipulation. Students are expected to write all the codes in PyCharm IDE  and when required should explore the
# debugging tool to find a logical flaw in their code or to understand the flow of their code.

##################
#### Problems ####
##################


# 1. Given a list like myList=[1,2,3,4] your task is to find sum of each number with another number,
# i.e. 1+2,1+3,1+4,2+3,2+4,3+4 . Write two codes, one using list comprehension and other using for loop.

# Given list
myList = [1,2,3,4]

# a. Using list comprehension
myListComp = [ x + y for x in myList for y in myList[x:] ]
print '\n1a. List comprehension results:', myListComp

# b. Using a for loop
print('\n1b. For loop results:')
for x in myList:
    for y in myList[x:]:
        sums = x + y
        print sums

# 2. Given a list write a code to detect if there is a duplicate element present in the list or not.
# Print yes or no. Write two codes, one using '==' operator and other using exclusive or operator '^'.

# Given List
myList2 = [1,2,3,4]

# a. Using '==' operator
for x in myList2:
    dupes = []
    for y in myList2[x:]:
        if x == y:
            dupes.append(int(1))
        else:
            dupes.append(int(0))
if sum(dupes) > 0:
    print "\n2a. '==' operator results: yes"
else:
    print "\n2a. '==' operator results: no"

# b. Using '^' operator
for x in myList2:
    dupes = []
    for y in myList2[x:]:
        if int(x) ^ int(y):
            dupes.append(int(0))
        else:
            dupes.append(int(1))
if sum(dupes) > 0:
    print "\n2b. '^' operator results: yes"
else:
    print "\n2b. '^' operator results: no"

# 3. Given below is a 2D matrix, create a list of all the odd numbers present in the matrix.
# Also sort the list in descending order.

# Given matrix
myMatrix = [[1, 2, 3, 4],
            [5, 6, 7],
            [8, 9, 10]]

# Create a flat list of the matrix
matrixList = [ i for row in myMatrix for i in row ]

# Filter odd numbers
odds = [ x for x in matrixList if x % 2 > 0 ]

# Sort in descending order
odds.sort(reverse = True)
print "\n3. Odd numbers results:", odds

# 4. Given below is a 2D matrix, create a list of squares of all the even numbers present in the matrix.

myMatrix = [[1, 2, 'aa',3, 4],
            ['dd',5, 6, 7],
            [8, 9, 10,'cc']]

# Create a flat list of the matrix
matrixList = [ i for row in myMatrix for i in row ]

# Filter out numerical values
numVals = [ x for x in matrixList if isinstance(x, int) ]

# Squares of even numbers
sqrs = [ x*x for x in numVals if x % 2 == 0 ]
print "\n4. Squares results:", sqrs


# 5. Given below is a 2D matrix, create a list of squares of all the prime numbers present in the matrix.
# (Hint: use 6k+1 or 6k-1 formula)

# Given matrix
myMatrix = [[21, 22, 23, 4, 16, 17, 18, 19],
            [5, 6, 7, 14, 15, 20, 1, 2, 3],
            [8, 9, 10, 11, 12, 13]]

# Transform Matrix to list and filter strings
matrixList = [ i for row in myMatrix for i in row ]

# Create list of squares of primes
prmeSqrs = [ x*x for x in range(2, max(matrixList)+1) if all(x % y != 0 for y in range(2, int(x ** 0.5) + 1)) ]
print "\n5. Prime squares results:", prmeSqrs


# 6. Make a dictionary of all those words, from the given paragraph, which are having 4 or more letters in it .
# Key of the dictionary should be word and value should be the number of times that word has appeared in the paragraph.
# eg. {"feminist":3,"part":2,"campaign":1}

# Given string
mySentence = "It's the Spice Girls but not as you know them. Twenty years after it was " \
             "first released, this famous girl power anthem has been given a 21st century " \
             "feminist makeover. The new video is part of Project Everyone's campaign to " \
             "improve the lives of women and girls everywhere, calling for an end to violence " \
             "against girls, quality education for all and equal pay for equal work."

# Split words on space
myWordList = mySentence.split(" ")

# Filter words with four or more characters
myWordFilter = [ w for w in myWordList if len(w) >= 4 ]

# Count instances
myWordFreq = [ myWordFilter.count(w) for w in myWordFilter ]

# Create dictionary
myWordDict = dict(zip(myWordFilter, myWordFreq))
print "\n6. Four letter word results:", myWordDict


# 7. Given a list, multiply all the elements of the list by 2 without using any arithmetic operator.
# Hint: use bitwise operator

# Given list
myList7=[32,5,6,47]

# Create new list
newList = []

# Append using bitwise operator
for x in myList7:
    newList.append(x << 1)
print "\n7. Double element results:", newList


# 8. Given below are two 2D matrix, add them element wise to form a third 2D matrix and print the resultant matrix.

# Given matrices
myMatrix1 = [[1, 2, 3, 4],
            [5, 6, 7,6],
            [8, 9, 10,4]]

myMatrix2 = [[3, 1, 1, 4],
            [7, 7, 7,7],
            [8, 9, 10,11]]

# Create blank matrix
myMatrix3 = []

# Cycle through matrix rows & columns to append elementwise additions
for i in range(len(myMatrix1)):
    row = []
    for j in range(len(myMatrix1[0])):
        row.append(myMatrix1[i][j]+myMatrix2[i][j])
    myMatrix3.append(row)
print "\n8. Resultant matrix results:", myMatrix3