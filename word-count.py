print('Whats on your mind today?')
Input = input().split(' ')

def wordCounter(words):
    wordCount = 0
    for word in words:
        wordCount += 1
    return wordCount

print(f'COol, you just told me what\'s on your mind in {wordCounter(Input)} words\n')


print('Now, enter a file name to count all the words inside that file')
fileName = input()
try:
    f = open(fileName, 'r')
    wordArray = f.read().split(' ')

    print(f'This text file has {wordCounter(wordArray)} words in it, amazing!')
except FileNotFoundError:
    print('The file {fileName} does not exit, enter a valid file name')

