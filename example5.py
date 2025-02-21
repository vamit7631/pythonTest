input = "My name is Amit"

input = input.split()[::-1]
input = " ".join(input)
print(input)



##################### list comprehension ######################################
input2 = "My name is Amit verma"
words = input2.split()
reversr_words = " ".join([word for word in reversed(words)])
print(reversr_words)
