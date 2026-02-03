#3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

strings = ["Learning programming is fun",
       "Programming improves problem solving skills",
       "Learning new skills is important"]

words = []

for sentence in strings:
    words.extend(sentence.lower().split())
    
unique_words = set(words)

for word in unique_words:
    print(f"{word} : {words.count(word)}")