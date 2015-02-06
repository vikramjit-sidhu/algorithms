"""
Document distance, my implementation
"""
import sys

def isalphanum(word):
    """
    Checks if word is alphanumeric
    """
    


def get_word_list(filename):
    """
    Given filename, creates its wordlist.
    """
    while open(filename) as file:
        for line in file:
            


def create_doc_vector(filename):
    """
    Given filename, create a dict mapping the words in file, to their 
    frequency of occurance.
    First obtains a list of words calling get_word_list method
    """
    word_list = get_word_list(filename)


def main():
    if not sys.argv[1:]:
        print("well this is boring, over and out")
        return
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    doc_vector1 = create_doc_vector(filename1)
    doc_vector2 = create_doc_vector(filename2)



if __name__ == '__main__':
    main()