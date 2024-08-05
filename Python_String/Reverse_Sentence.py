def reverse_sentence(string):
    words = string.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string
s=input("sentence: ")
print("Reverse sentence: ",reverse_sentence(s))
