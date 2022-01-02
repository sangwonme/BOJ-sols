# input
l, c = list(map(int, input().split()))
letters = input().split()
letters.sort()

# pick c letters
words = []
for i in range(2**c):
    indices = list(bin(2**c-i)[2:])
    indices = ['0']*(c - len(indices)) + indices
    # if c letters are selected
    if sum(list(map(int, indices))) == l:
        word = ''
        for j in range(len(indices)):
            if bool(int(indices[j])):
                word += letters[j]
        # find num of vowels
        vowel_cnt = 0
        for v in 'aeiou':
            vowel_cnt += word.count(v)
        consonant_cnt = len(word) - vowel_cnt
        # push word to the words list
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            words.append(word)

# print ans
for word in words:
    print(word)