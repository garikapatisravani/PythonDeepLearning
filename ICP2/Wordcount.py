# Author : Sravani Garikapati
# Program to find the wordcount in a file for each line
inFile = open("sampleinputfile.txt", "r")  # Opening the file in read mode
outFile = open('sampleoutputfile.txt' , 'w') # Opening the file in write mode
d = dict() # Create an empty dictionary
# Loop through each line of the file
for line in inFile:
    line = line.strip()     # Remove the leading spaces and newline character
    line = line.lower()     # Convert the characters in line to lowercase to avoid case mismatch
    words = line.split(" ")     # Split the line into words
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
# Prints and Writes the output to text file
for k, v in d.items():
    print(k,":",v)
    outFile.write(str(k) + ' : ' + str(v) + '\n')
outFile.close()