def is_palindrome(text):
    return (normalized := ''.join(char.lower() for char in text if char.isalnum())) == normalized[::-1]

print(is_palindrome("oko"))
print(is_palindrome("radar"))
print(is_palindrome("witaj"))