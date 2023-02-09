# Define the number to be devided by 3
print ("please enter a number and pres ENTER")
numinator_start = int(input())
denuminator = 3
numinator = numinator_start

# As long as result is larger than zero:​
while numinator > 0:

    # Subtract three​
    numinator = numinator- denuminator


# Check if is zero or not​
if numinator == 0: 
    # print result​
    print (f'{numinator_start} is devisable by {denuminator}')
else:
    print (f'{numinator_start} is not devisable by {denuminator}')   