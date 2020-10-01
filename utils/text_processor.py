import stanza
from .cmu_utils import *
from .dictionary import *

'''

Takes a sample text and generates a dictonary of the words contained within it.

Constructs a dictionary with entries for each word

'''
class TextProcessor():
    #File path to text
    def __init__(self, filepath, text_type):
        #Create a dictionary for this text file
        self.dictionary = Dictionary()
       
        #Make sure we have an english language model from stanza
        stanza.download('en')
        self.nlp = stanza.Pipeline('en', processors='tokenize,pos', use_gpu=True)

        #Load the cmu dict to generate syllable counts
        cmu_dict = load_cmu_dict("data/cmudict")

        #Load the proper cleaning function based on type of text
        clean_func = None
        if text_type == "screenplay":
            clean_func = self.clean_screenplay
        else:
            print("Error: Unknown text type")
            exit()


        #Open file and process
        with open(filepath, 'r') as text:
            #Iterate through the lines, passing through stanza for PoS
            for line in text.readlines():
                #Check for empty lines
                if len(line) <= 1:
                    continue
                #Clean up the line before parsing
                cleaned_line = clean_func(line)
                proc = self.nlp(cleaned_line)
                #Iterate through all of the words and generate dictionary entries 
                for sentence in proc.sentences:
                    for wd in sentence.words:
                        text = wd.text.lower()
                        #Check if there is an entry in the cmu_dict
                        if not text in cmu_dict.keys():
                            continue
                        entry = cmu_dict[text]
                        #Create a word object
                        word = Word(string=wd.text, syllables=entry.syllables, 
                                    phonemes=entry.phonemes, pos=wd.pos)
                        #Insert word object into dictionary
                        self.dictionary.insert(word.string.lower(), word)

        self.dictionary.summary()
        print("Created a dictionary with {} entries.".format(self.dictionary.size()))

        return

    #Cleans up a line of a screenplay
    def clean_screenplay(self, string):
        #Break apart speaker/speech
        string_toks = string.split(":")
        string = string_toks[-1]
        #Remove new line
        string = string[:-1]
        #Add punctuation if missing.
        if string[-1].isalnum():
            string = string+'.'
        #Remove leading whitespace
        if string[0] == " ":
            string = string[1:]
        return string
