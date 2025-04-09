def vowels(str):
	vowels = "aeiouAEIOU"
	num_vowels = 0
	num_constants = 0
	
	for char in str:
		if char in vowels:
			print(char)
			num_vowels+= 1
		else:
		    print(str)
		    num_constants+= 1
	return num_vowels, num_constants

str = "bowled"
vowels,constants = vowels(str)
print(f"{vowels} and {constants}")
