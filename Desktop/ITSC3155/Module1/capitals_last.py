#Jina Butkovic
# Used https://codeigo.com/python/sort-letters-in-a-string-alphabetically to learn how to sort 
# Sort a phrase in capital letter order. First it uses the ' '.join to bring the space to the front, 
# Then, it uses the sorted() and set() functions to bring the capital letters to the front. The last thing I utilized
# Was ordering the phrase to print in reverse order. 

phrase = input("Enter a string: ")
sorted_phrase = (''.join(sorted(set(phrase))))
phraseBackwards = sorted_phrase[::-1]
print(phraseBackwards)
