# open file
file = open("Sentence_Analyser\Text_file", "r")

# Vowel list
vowels = {"a", "e", "o", "u", "i"}

# Word counter
word_count = 1

# Make vowel count 0
vowel_count = 0

# Variable that checks if continue running program
run = True
while run is True:
    # Make sentence the file
    sentence = str(file.readline())

