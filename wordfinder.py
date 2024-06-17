"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Class to find random words from a dictionary file.

    >>> wf = WordFinder("C:\Users\Seventy280 Client Pc\OneDrive\Desktop\python-oo-practice\words.txt")
    3 words read
    
    >>> isinstance(wf.random(), str)
    True
    """

    def __init__(self, path):
        """Initialize the WordFinder with a path to a file containing words.
        
        Args:
            path (str): The path to the file containing words.
        """
        self.path = path
        self.words = self.read_words()
        print(f"{len(self.words)} words read")

    def read_words(self):
        """Read the words from the file and store them in a list.
        
        Returns:
            list: A list of words read from the file.
        """
        with open(self.path, 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def random(self):
        """Return a random word from the list of words.
        
        Returns:
            str: A random word from the list.
        """
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines and comments.

    >>> swf = SpecialWordFinder("C:\Users\Seventy280 Client Pc\OneDrive\Desktop\python-oo-practice\words.txt")
    4 words read
    
    >>> isinstance(swf.random(), str)
    True
    """

    def read_words(self):
        """Read the words from the file, excluding blank lines and comments.
        
        Returns:
            list: A list of valid words read from the file.
        """
        with open(self.path, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]


