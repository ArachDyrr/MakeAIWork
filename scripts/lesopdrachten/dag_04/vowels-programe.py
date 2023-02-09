# Define the string “paard”
word = input('Please provide the word to have its number of checked.')

# define counter
counter = 0

# Loop over each letter in string:
for char in word:

	# Check if character is vowel:
	## loop gata door tot eer geen characters meer in het woord zitten waar naar gekeken moet worden.
	if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':

		# If so then increment counter
		counter = counter +1

# Print result
print (f'{word} contains {counter} vowels.')