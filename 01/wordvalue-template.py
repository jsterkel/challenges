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


def calc_word_value():
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    pass

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    pass # run unittests to validate


all_the_words = load_words()

print(all_the_words)
