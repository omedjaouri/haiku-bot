from utils.cmu_utils import *
import random
import numpy as np

'''

Loads the dataset and prints out 10 entries.

'''

dataset = load_cmu_dict("data/cmudict")
for i in range(0, 10):
    #Load a random syllable count dict
    syllable_count = random.randint(1, 8)
    keys = list(dataset[str(syllable_count)].keys())
    #Load a random index
    idx = random.randint(0, len(keys))
    print(str(syllable_count)+": "+keys[idx] + " --> " + str(dataset[str(syllable_count)][keys[idx]].phonemes))
