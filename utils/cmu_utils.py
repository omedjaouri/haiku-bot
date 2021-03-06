import os

'''

Contains various useful functions for handling the CMU Phoneme Dictionary

'''

#Object representation of each word in the dataset
class Entry():
    #Basic initialization function
    def __init__(self, phonemes, syllables):
        self.phonemes = phonemes
        self.syllables = syllables


def load_cmu_dict(dict_path):
    syllable_dict = {}
    dict_path = os.path.abspath(dict_path)
    #Open the dictionary
    with open(dict_path, encoding="ISO-8859-1") as cmu_dict:
        #Iterate through the lines, extracting the valid entries
        for line in cmu_dict:
            #Skip commented lines
            if line[0:3] == ";;;":
                continue
            #Split the line into the word and phonemes
            word, phonemes = line.strip().split('  ')
            phonemes = phonemes.split(' ')
            #Check if the word is an alternative pronunciation
            if word[-1] == ")":
                continue

            #Add the word and associated phonemes to the dict.
            syllable_count = count_syllables(phonemes)
            entry = Entry(phonemes, syllable_count)
            syllable_dict[word.lower()] = entry

    #Return the dicts
    return syllable_dict

#Count the number of stresses and unstresses in a phoneme list.
def count_syllables(phonemes):
    syllables = 0
    for phoneme in phonemes:
        if phoneme[-1] == "0" or phoneme[-1] == "1" or phoneme[-1] == "2":
            syllables = syllables + 1
    return syllables
