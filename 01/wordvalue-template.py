# Basic Template for the program.

from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    list_of_words = []
    dict_file = open(DICTIONARY,"r")
    for line in dict_file: 
        next_line = dict_file.readline()
        list_of_words.append(next_line.strip())
    return(list_of_words)


def calc_word_value(list_of_words):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_scores = {}
    for word in list_of_words:
        this_word_score = 0
        for letter in word:
            if letter.isalpha():
                this_word_score = this_word_score + LETTER_SCORES[letter.upper()]
        word_scores[word] = this_word_score
    return(word_scores)
            

def max_word_value(dict_of_all_words):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    current_high_score = 0
    current_highest_word = ""
    for item in dict_of_all_words:
        if dict_of_all_words[item] > current_high_score:
            current_high_score = dict_of_all_words[item]
            current_highest_word = item
    return(current_highest_word)

if __name__ == "__main__":
    pass # run unittests to validate


all_the_words = load_words()
word_score_dict = calc_word_value(all_the_words)
high_score_word = max_word_value(word_score_dict)

print(high_score_word)