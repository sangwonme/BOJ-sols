# input
n = int(input())
words = [input() for i in range(n)]

# encode each word to series of new-alphabet index
new_alpha = ['a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'ng', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y']
encoded_words = []
for i in range(n):
    code = []
    for j in range(len(words[i])):
        if j != len(words[i])-1 and words[i][j] == 'n' and words[i][j+1] == 'g':
            j += 1
            code.append(new_alpha.index('ng'))
        else:
            code.append(new_alpha.index(words[i][j]))
    encoded_words.append((code, words[i]))

# result 
encoded_words.sort(key=lambda x: x[0])
for i in range(n):
    print(encoded_words[i][1])