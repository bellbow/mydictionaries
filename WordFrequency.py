'''
Write a program that reads the contents of a text file (you can use this file - sometext.txt Download sometext.txt). 
The program should create a dictionary in which the keys are the individual words found in the file 
    and the values are the number of times each word appears. 
For example, if the word “the” appears 128 times, the dictionary would contain an element with 'the' as the key and 128 as the value. 
The program should display the frequency of each word.
'''
infile = open(r'sometext-1.txt','r')
text = infile.read()

punc = [',','.']
words = {}

for word in text.split():
    for i in word:
        if i in punc:
            word = word.replace(i,'')
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
