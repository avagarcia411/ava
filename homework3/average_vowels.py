# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

# 1
def vowels_and_consonants(text):
    vowels = 0
    consonants = 0
    vowel_list = "aeiouAEIOU"

    for char in text:
        if char.isalpha():
            if char in vowel_list:
                vowels += 1
            else:
                consonants += 1
    
    return (vowels, consonants)

print(vowels_and_consonants(    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."))

# 2
def average_vowels_and_consonants(paragraph):
    vowel_counts = []
    consonant_counts = []

    sentences = paragraph.split('.')
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    for sentence in sentences:
        vowels, consonants, = vowels_and_consonants(sentence)
        vowel_counts.append(vowels)
        consonant_counts.append(consonants)

    num_sentences = len(sentences)
    if num_sentences == 0:
        return (0, 0, 0)
    avg_vowels = sum(vowel_counts) / num_sentences
    avg_consonants = sum(consonant_counts) / num_sentences

    return (num_sentences, avg_vowels, avg_consonants)

paragraph = """
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
"""

num_sentences, avg_vowels, avg_consonants = average_vowels_and_consonants(paragraph)

print(f"The paragraph has {num_sentences} sentences.")
print(f"The average number of vowels per sentence is {avg_vowels:.2f}.")
print(f"The average number of consonants per sentnece is {avg_consonants:2f}.")