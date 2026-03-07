def word_count(sentence):
    words = sentence.split()
    WORDS = {}

    for word in words:
        if word not in WORDS:
            WORDS[word] = 1
        else:
            WORDS[word] += 1

sentence = "fastapi is fast and python is fun"

print(word_count(sentence))