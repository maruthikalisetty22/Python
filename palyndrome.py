
# Check if a string is a Palindrome or not

def is_palindrome(string):
    """
    Check if the given string is a palindrome.
    
    Args:
    string (str): The string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    length = len(string)
    
    for index in range(length // 2):
        if string[index] != string[length - index - 1]:
            return False
    return True

# Example usage
example_string = "radar"
print(is_palindrome(example_string))
