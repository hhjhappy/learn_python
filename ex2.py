def break_words(aaa):
    """This function will break up workds for us."""
    workds = aaa.split(' ')
    return workds

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after poping is off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Print the last word after poping if off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Print the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


sentence = "All good things come to those who wait."

print(break_words(sentence))