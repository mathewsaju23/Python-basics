file = open("sampletext.txt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))