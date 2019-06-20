import re

class Command(object):
    """Wrapper object for simplifying the process of identifying the key words and parameters within a command.

    Parameters
    ----------
    keywords : A list of strings

    Attributes
    ----------
    keywords
        key words are a list of key words that can be used in commands to determine which action
        the user wants the program to take

    """

    def __init__(self, keywords):
        self.keywords = keywords;

    def __contains__(self, command):
        """Checks if an input contains keywords.

        Parameters
        ----------
        command : string
            Description of parameter `command`.

        Returns
        -------
        type
            Description of returned object.

        """
        pass

    def parseParams(self, command):
        pass
