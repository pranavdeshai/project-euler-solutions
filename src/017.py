# Number letter counts
num_to_word = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}


def num_to_word(n):
    if n == 1000:
        return 'onethousand'
    hundreds = n // 100
    tens = (n % 100) // 10
    ones = (n % 100) % 10
    word = []
    if ones:
        if not (n % 100 in range(11, 20)):
            word.append(num_to_word[ones])
    if tens:
        if n % 100 < 20:
            word.append(num_to_word[n % 100])
        else:
            word.append(num_to_word[10 * tens])
    if hundreds:
        if ones or tens:
            word.append('and')
        word.append(num_to_word[hundreds] + 'hundred')
    return ''.join(word[::-1])


total = 0
for i in range(1, 1001):
    total += len(num_to_word(i))
    print(num_to_word(i))
print(total)
