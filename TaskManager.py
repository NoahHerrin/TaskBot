# Project: Taskbot
# Author: Noah Herrin
# Purpose: Data structure responsible for storing tasks


class TaskList(object):

    def __init__(self):
        """Initialize TaskList by creating a list to store the task objects and a dictionary to improve
           runtime for searching."""
        self.__task_list = []
        self.__task_indicies = {}

    def __contains__(self,key):
        return key in self.__task_indicies

    def add_task(self, task_name):
        if task_name in self:
            return True
        else:
            self.__task_indicies[task_name] = len(self.__task_list)
            self.__task_list.append(Task(task_name))
            return False
    def get_tasklist(self):
        return self.__task_list
    def get_task(self, task_name):
        """Short summary.

        Parameters
        ----------
        task_name : str
            The name of the desired Task object.

        Returns
        -------
        Task
            The Task object with whose name attribute is the same as 'task_name'

        Exceptions
        ----------
        'task [task_name] does not exist'
            attempted to get a task not contained in tasklist

        """
        if task_name not in self:
            return False
        else:
            return self.__task_list[self.__task_indicies[task_name]]

    def __str__(self):
        """Overrides default toString method to print details about all tasks in TaskList.

        Parameters
        ----------


        Returns
        -------
        type
            returns details of all tasks in task list (see __str__ documentation for Task).

        """

        retval = "You have {} tasks\n".format(len(self.__task_list))

        for task in self.__task_list:
            retval += str(task)
        return retval.rstrip()


class Task(object):
    # TO DO LIST
    #
    # [ ] save list to a given destination, mongodb or local file
    # [ ] make functions editiable, change task name
    # [ ] add notes to tasks
    # [ ] add the option to open up links in notes for task

    def __init__(self, name):
        """Initialize new Task object.

        Parameters
        ----------
        name : str
            The message that will be displayed whenever task is referenced.

        Returns
        -------
        None
            Does not return a value

        """
        self.__name = name
        self.__completed = False

    def get_name(self):
        return self.__name
        
    def __str__(self):
        """returns a formatted value of Task object.

        Parameters
        ----------


        Returns
        -------
        str
            Returns a string containing the status of the task, completed, incomplete along with the name of the task.
            Example 1: Completed Task
            "[X] Walk the dog"
            Example 2: Incomplete Task
            "[ ] Visit all 6 continents"

        """
        if self.__completed:
            return "[X] - {} \n".format(self.__name)
        else:
            return "[ ] - {}\n".format(self.__name)

    def mark_complete(self):
        """ Marks Task as complete"""
        self.__completed = True
