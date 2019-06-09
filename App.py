from TaskManager import TaskList
import re

quit_synonyms = ['quit', 'terminate', 'end', 'close']
help_synonyms = ['help', 'confused', '?']
display_task_synoynms = ['tasks', 'show tasks', 'display tasks']
add_task_synonyms = ['add task', 'create task', 'new task']

def help_dialogue():
    msg = "Help Guide\n"
    msg += "\tclose program - {}\n".format(quit_synonyms)
    msg += "\tadd task - '[new task / create task] [task name]\n"
    msg += "\tmark task as complete -'completed [task_name]' or completed [task_num]\n"
    msg += "\tdelete task - '[delete / clear] [task_name] or [task_num]'\n"
    msg += "\tdisplay tasks - 'display tasks' or 'show tasks' or 'tasks'\n"
    return msg
def is_new_task(command):
    """ Checks if string contains a command to create a new taks.

    Parameters
    ----------
    str : string
        Any string that may contain a command to create a new task.

    Returns
    -------
    Touple (Boolean, String)
        Boolean will be True if 'str' contains a command to create a new task, else will return false. if boolean is False
        then string will be None, else it will be the message following the command used to create a task

    """
    is_new_task = False
    task_name = None

    # check for 'add task [message]' notation
    for synonym in add_task_synonyms:
        if re.search("^{}.".format(synonym), command):
           task_name = re.split(r'{}'.format(synonym),command)[1].strip()
           is_new_task = True

    return(is_new_task, task_name)

def main():
    tasklist = TaskList()
    print(tasklist, end="")

    # input loop
    user_input = input("> ")
    task_name = None
    while user_input not in quit_synonyms:
        # check if user needs help
        if user_input in help_synonyms:
            print(help_dialogue())

        # determine if user is trying to add a new task
        retval = is_new_task(user_input)
        if retval[0]:
            print("taskbot: adding new task")
            tasklist.add_task(retval[1])
        elif user_input in display_task_synoynms:
            print(tasklist)



        user_input = input("> ") # prompt user for new command


main()
