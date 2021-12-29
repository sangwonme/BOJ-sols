import itertools

# input
n, k = map(int, input().split())
learn_num = k-5
words = []

# get words and process each word
except_chars = ['a', 'n', 't', 'c', 'i']
for i in range(n):
    word = input() 
    # delete 'a, n, t, c, i' & other redundancy
    for j in range(len(except_chars)):
        word = word.replace(except_chars[j], '')
    word = ''.join(sorted(set(word), key=word.index))
    # only append for learnable word
    if(len(word) <= learn_num):
        words.append(sorted(list(word)))
# flattern list
all_characters = sorted(list(itertools.chain(*words)))
all_characters = ''.join(sorted(set(all_characters), key=all_characters.index))

# zero-answer condition
if (len(words) == 0):
    print(0)

# all-answer condition
elif (len(all_characters) <= learn_num):
    print(len(words))
    
# else find answer by brute force
else:
    res = 0
    for i in range(2**len(all_characters)):
        indices = list(bin(i)[2:])
        if(sum(map(int, indices)) == learn_num):
            indices = ['0'] * (len(all_characters) - len(indices)) + indices
            learned = []
            for j in range(len(all_characters)):
                learned += all_characters[j] if bool(int(indices[j])) else []
            cnt = 0
            for j in range(len(words)):
                cnt += 1 if all(char in learned for char in words[j]) else 0
            res = max(cnt, res)
    print(res)