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
        """Overrides contains method for TaskList, checks if task already exists.

        Parameters
        ----------
        key : str
            The name of a Task that may or may not exist.

        Returns
        -------
        Boolean
            Returns True if TaskList contains task if not it will return False.

        """
        return key in self.task_indicies

    def add_task(self, task_name):
        """ Adds new task to the list

        Parameters
        ----------
        task_name : str
            The name that will be displayed whenever program references this task.

        Returns
        -------
        Boolean
            will return True if task list already contains task and False if it does not.

        """
        if task_name in self:
            return True
        else:
            self.__task_indicies[task_name] = len(self.__task_list)
            self.__task_list.append(Task(task_name))
            return False

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
            raise Exception("Task '{}' does not exist.")
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
        return retval


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
