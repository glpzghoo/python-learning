def reverse_words(sentence):
    words = sentence.split(" ")
    reverse = words[::-1]

    return " ".join(reverse)

user_input = input(f"Өгүүлбэр~ ")

print(reverse_words(user_input))