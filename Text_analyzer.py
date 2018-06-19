import re
import sys
import pandas as pd

def read_file(path):
    ''' Reads file is as a string. '''
    with open(path, 'r') as f:
        return f.read()

def get_words(s):
    ''' Returns a list of words from an inputted string. '''
    s = re.sub('[.!?,:;]', '', s)
    return [word.lower() for word in s.split(' ') if word != '']

def get_sentences(s):
    ''' Returns a list of sentences from an inputted string. '''
    return [sent for sent in re.split('[.!?]', s) if sent != '']

def word_count(s):
    ''' Returns total word count in inputted string. '''
    return len(get_words(s))

def unique_words (s):
    ''' Returns set of unique words from inputted string. '''
    return len(set(get_words(s)))

def avg_word_len(w):
    ''' Returns average word length in inputted string as float. '''
    return sum(len(word) for word in get_words(w)) / len(get_words(w))

def sent_count(s):
    ''' Returns total sentence count in inputted string. '''
    return len(get_sentences(s))

def avg_sent_len(s):
    ''' Returns average sentence length in inputted string as float. '''
    return sum(word_count(sent) for sent in get_sentences(s)) / sent_count(s)

def word_list_desc(s):
    ''' Returns a list in descending order of frequency of words used in inputted string. '''
    word_count_dict = {}
    for w in set(get_words(s)):
        word_count_dict.update({w: get_words(s).count(w)})
    word_count_df = pd.DataFrame.from_dict(word_count_dict, orient='index')
    word_count_df = word_count_df.sort_values(by=[0], ascending=False)
    return list(word_count_df.index)

def word_with_count(s):
    ''' Returns dictionary object from inputted string: keys equal unique words, values equal word count. '''
    word_count_dict = {}
    for w in set(get_words(s)):
        word_count_dict.update({w: get_words(s).count(w)})
    return word_count_dict

def freq_phrases(s):
    '''
    Sets of three or more words used three or more times.
    '''
    pass

assert word_count('These, are words!!') == 3
assert word_count('  will    this     work?') == 3
assert unique_words('how many Words many words?') == 3
assert unique_words('the cat sat the sat cat bat!') == 4
assert avg_word_len("this is this a test,  a test! its test") == 3
assert avg_word_len('One two Three four, fives!') == 4
assert sent_count('One. Two. Three! Four and five and six?') == 4
assert sent_count('Many, many sentences. Some, are long. Some are short!') == 3
assert avg_sent_len('One. Two. Three! Four and five and six?') == 2
assert avg_sent_len('Many, many sentences. Some, long. Some are short! Ha Ha!') == 2.5
# assert word_list_desc('Try these words out. Try again words. Try!') == ['try', 'words', 'again', 'these', 'out']
assert word_with_count('Try these words out. Try again words. Try!') == {'again': 1, 'out': 1, 'these': 1, 'try': 3, 'words': 2}

if __name__ == '__main__':
    text = read_file(sys.argv[1])
    print('Word count: {}'.format(word_count(text)))
    print('Unique words: {}'.format(unique_words(text)))
    print('Average word length: {}'.format(round(avg_word_len(text), 2)))
    print('Sentence count: {}'.format(sent_count(text)))
    print('Average sentence length: {}'.format(round(avg_sent_len(text), 2)))
    if input('Type y to see a list of words in desceding order of frequency.Type p to pass.') == 'y':
        print(word_list_desc(text))
    if input('Type y to see a dictionary of words with their frequency.Type q to quit.') == 'y':
        print(common_word_dict(text))

exit()

