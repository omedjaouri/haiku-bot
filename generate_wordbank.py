# Generates a word bank from a text file and the CMU dictionary
import argparse
import os

#Local imports
from utils.text_processor import TextProcessor

if __name__ == "__main__":
    #Create parser to enable command-line arguments
    parser = argparse.ArgumentParser()
    #Create command-line arguments
    parser.add_argument("--filepath", help="The filepath of source text file")
    parser.add_argument("--text-type", 
                        help="The type of text that is being processed (screenplay, book)",
                        default="screenplay")


    #Parse arguments
    args = parser.parse_args()

    if args.filepath is None:
        print("Error: User must supply a text file to generate the wordbank from.")
        exit()
    else:
        filepath = os.path.abspath(args.filepath)
    #Read the text file with the text processor
    text_processor = TextProcessor(filepath=filepath, text_type=args.text_type)




