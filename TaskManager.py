class TaskList(object):

    # initialize task manager with a list to store tasks
    def __init__(self):
        """Initialize TaskList by creating a list to store the task objects and a dictionary to improve
           runtime for searching."""
        self.task_list = []
        self.task_indicies = {}
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
    def addTask(self, task_name):
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
            self.task_indicies[task_name] = len(self.task_list)
            self.task_list.append(Task(task_name))
            return False

    def __str__(self):
        """Overrides default toString method to print details about all tasks in TaskList.

        Parameters
        ----------


        Returns
        -------
        type
            returns details of all tasks in task list (see __str__ documentation for Task).

        """
        retval = ""
        for task in self.task_list:
            retval += str(task)
        return retval

class Task(object):


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
        self._name = name
        self._completed = False

    def __str__(self):
        """Overrides toString for Task object to print out relavent info about task.

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
        return (lambda: '[ ]  {}'.format(self._name), '[X] - {}'.format(self._name))[self._completed]()

    def markComplete(self):
        """ Marks Task as complete"""
        self._completed = True
