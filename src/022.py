# Name scores
with open('./Resources/p022_names.txt') as f:
    names = f.readline().split('","')
    names[0] = "MARY"
    names[-1] = "ALONSO"
    names.sort()
    result = 0
    for i in range(len(names)):
        result += sum(ord(c)-64 for c in names[i]) * (i+1)
    print(result)