
'''

Contains the word itself, the syllable count, the phonemes, and the part of speech

'''
class Word():
    def __init__(self, string="", syllables=0, phonemes=[], pos=None):
        self.string = string
        self.syllables = syllables
        self.phonemes = phonemes
        self.pos = pos
        return

'''

Dictionary class which maintains a dictionary of all possible words

'''
class Dictionary():
    def __init__(self):
        #Initialize member variables
        self.dictionary = {}

    #Attempts to insert a new entry into the dictionary
    def insert(self, key, value):
        #For now just insert into dictionary
        if key in self.dictionary.keys():
            return False
        else:
            self.dictionary[key] = value
            return True

    #Reports the size of the dictionary
    def size(self):
        return len(self.dictionary.keys())

    #Print out the pairs in the dictionary
    def summary(self):
        keys = self.dictionary.keys()
        for key in keys:
            word = self.dictionary[key]
            print("{} -> Syllable Count: {}, Part of Speech: {}".format(key, word.syllables, 
                                                                        word.pos))

