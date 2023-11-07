# TODO

# Gets input from user
text = input("Enter a sentence: ")


letters = 0
# counts the number of letters
for i in text:

    if i.isalpha():
        letters += 1

print(letters)


# counts the number of words in a sentence
words = len(text.split())

print(words)


# counts the number of sentences
sentences = text.count("!") or text.count(".") or text.count(",")

print(sentences)

# Calculates Average letters
AverageLetters =  letters / words * 100

# Calculates average sentences
AverageSentences = sentences / words * 100

# Calculates the index
index = 0.0588 * AverageLetters - 0.296 * AverageSentences - 15.8

Grade = round(index)


# Displays any of these depending on the sentence entered
if Grade > 16:
    print("Grade 16+")
elif Grade < 1:
    print("Before Grade 1")
else:
    print("Grade:", Grade)