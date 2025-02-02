#Write a function that accepts string from user, return a sentence with the words reversed.
# We are ready -> ready are We

def reverse_words():
    sentence = input("Enter a sentence: ")
    reversed_sentence = ' '.join(sentence.split()[::-1])
    print("Reversed:", reversed_sentence)

reverse_words()
