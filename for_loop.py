words = ["Hello", "Dude", "how", "are", "you"]

print("Total words in list:", len(words))         # Length of list
print("Reversed list:", list(reversed(words)))    # Reverse the list
print("Sorted list:", sorted(words))              # Sorted list alphabetically

print("\n--- Looping through each word and showing string functions ---")
for word in words:
    print(f"\n📘 Word: {word}")
    
    # Basic info
    print("Length:", len(word))                   # Length of the string
    print("First char:", word[0])
    print("Last char:", word[-1])
    
    # Case functions
    print("Upper:", word.upper())
    print("Lower:", word.lower())
    print("Title case:", word.title())
    print("Swapcase:", word.swapcase())
    print("Is upper?", word.isupper())
    print("Is lower?", word.islower())

    # String analysis
    print("Starts with 'h'?", word.startswith('h'))
    print("Ends with 'e'?", word.endswith('e'))
    print("Count of 'o':", word.count('o'))
    print("Index of 'e' (if exists):", word.find('e'))  # Returns -1 if not found
    print("All alphabets?", word.isalpha())

    # Join and replace
    print("Joined with '-':", "-".join(word))
    print("Replace 'o' with '0':", word.replace('o', '0'))

    # Loop through characters
    print("Characters in word:")


# String to list and vice versa conversion
for i in words:
    for j in i:
        print(j)  # print each character
    k = "".join(i)  # join the characters with space
    l = list(k)
    print(f"This is {k}")
    print(f"This is lis of k: {l}")

#Enumerate
for i, j in enumerate(words):
    print(f"Index: {i}, Word: {j}")


#Print list no of times how many words are present
for i in words:
    k = []
    for j in i:
        k.append(words)
print(k)
    for char in word:
        print(char, end=" ")
    print()
