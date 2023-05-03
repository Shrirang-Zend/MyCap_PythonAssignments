def most_frequent(string):
    # create an empty dictionary to store the frequency of each character
    freq = {}
    
    # iterate over the characters in the string
    for char in string:
        # if the character is already in the dictionary, increment its count
        if char in freq:
            freq[char] += 1
        # otherwise, add the character to the dictionary with a count of 1
        else:
            freq[char] = 1
    
    # create a list of (count, char) tuples and sort it in reverse order
    sorted_freq = sorted([(count, char) for char, count in freq.items()], reverse=True)
    
    # iterate over the sorted list and print the characters and their counts
    for count, char in sorted_freq:
        print(char, '=', count, end=' ')
