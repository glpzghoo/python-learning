def is_palindrome(word):
    if not word:
        return False
    word = word.strip().lower()
    reverse = word[::-1]
    return reverse == word


user_input = input("Word: ")

print(f"{is_palindrome(user_input)}")