# Coded triangle numbers
with open('./Resources/p042_words.txt') as f:
    text = f.read()
words = text.split('","')
max_len = len(max(words, key=len))
d = {c:i for (c, i)}
