from utils.cmu_utils import *
import random

MAX_SYLLABLES = 5

dataset = load_cmu_dict("data/cmudict")


'''

Generates a haiku using the dictionary

'''

def generate_haiku_basic():
    #Generate each of the lines
    first = generate_line(5)
    middle = generate_line(7)
    last = generate_line(5)

    #Format together
    result = first + "\n" + middle + "\n" + last
    return result


#Generates a line with a specific syllable count
def generate_line(syllable_count):
    #Initialize empty list
    syllables = []
    #Get the first syllable
    syll = random.randint(1, min(syllable_count, MAX_SYLLABLES))
    syllables.append(syll)
    syllable_count = syllable_count - syll
    #Generate the rest of the syllables
    while syllable_count > 0:
        #Generate the rest of the syllables
        syll = random.randint(1, min(syllable_count, MAX_SYLLABLES))
        syllables.append(syll)
        syllable_count = syllable_count - syll
    #Generate the line picking at random.
    line = []
    for syllable in syllables:
        #Get the list of all keys for a specific syllable count and pick at random.
        keys = list(dataset[str(syllable)].keys())
        word = keys[random.randint(0, len(keys)-1)]
        line.append(word)
    return " ".join(line)

#Generate a haiku
print(generate_haiku_basic())
