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
           Example Usage
                help_command = Command(['help', 'usage', 'confused'])
                add_task_command = Command('add task', 'new task', 'create task')

                cmd = "help"
                cmd in help_command -> True
                cmd in add_task_command -> False

                cmd2 = "add task review notes"
                cmd2 in help_command -> False
                cmd2 in add_task_command -> True

        Parameters
        ----------
        command : string
            A string input containing key words and or parameters.

        Returns
        -------
        Boolean
            Indicates whether the command contains the command specific keywords.

        """

        # iterate through command sepecific key words
        # Best case O(1) worst case O(n)
        for keyword in self.keywords:

            # use regular expressions to search for key word in the given command
            if re.search("^{}.".format(keyword), command):
                return True
        return False

    def validateCommand(self, command):
        """ Takes a command and removes the key words leaving only the parameters.

        Parameters
        ----------
        command : string
            string input of the form 'key words' 'parameters'.

        Returns
        -------
        String
            a string representing the parameters of the command.

        """

        for keyword in self.keywords:

            # use regular expressions to search for key word in the given command
            if re.search("^{}.".format(keyword), command):
                params = re.split(r'{}'.format(synonym),command)[1].strip()
                return params
        return None








class CommandHandler(object):
    """Short summary.

    Parameters
    ----------
        None

    Attributes
    ----------
    __commands : dictionary
        __commands is a private dictionary meant to keep track of the command handlers for different commands
        data will be stored in the following format.
        'command name' : command object containing keywords corrisponding to command

    """

    def __init__(self):
        self.__commands = {}

    def executeCommand(self, commandString):
        # purpose TBD
        cmd = findCommand(commandString)
        params = cmd.validateCommand()
        print(params)

    def findCommand(self, commandString):
        """finds the correct command to parse commandString.

        Parameters
        ----------
        commandString : String
            The string command to be parsed and executed.

        Returns
        -------
        Command
            If the command is valid findCommand will return a command object that is able to correctly parse the input.
        Boolean
            return False if commandString is invalid

        """
        # iterate through commands
        for command in self.__commands:

            if commandString in self.__commands[command]:
                return self.__commands[command]

        return False


    def addCommand(self, commandName, keywords):
        """adds a new commmand to the command handler's master list

        Parameters
        ----------
        commandName : String
            a string identifier used for the master list.
        keywords : Array of String
            a list of string key words that will indicate the intentions of a command.

        Returns
        -------
        Boolean
            returns True if commandName does not exists and False if it does.


        """

        if commandName in self._commands:
            return False
        else:
            self.__commands[commandName] = keywords
            return True
