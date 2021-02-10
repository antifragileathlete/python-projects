print('Whats on your mind today?')
userInput = input()
wordList = userInput.split(' ')

wordCount = 0
for words in wordList:
    wordCount += 1

print(f'COol, you just told me what\'s on your mind in {wordCount} words')
