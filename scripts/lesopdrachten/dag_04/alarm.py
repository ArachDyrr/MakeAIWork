import time

# Define a counter and set to five​
secunds = 5


# As long as counter is not zero:​
while secunds > 0:

    print ('tick')

    # Decrement counter​
    secunds = secunds -1

    # Sleep for one second​
    time.sleep(1)


# Make beep sound
print ("Beep")
print ('\a')