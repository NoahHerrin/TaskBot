from TaskManager import TaskList
import re
import sys

Commands = {}
taskList = None
isRunning = True

def add_task(command, synonym):
        global taskList
        taskname = re.split(r'{}'.format(synonym),command)[1].strip()
        if taskname is not "":
                taskList.add_task(taskname)
                return True
        else:
                return False
def display_task(command,synonym):
        print(taskList)
        return True
def quit(command, synonym):
        global isRunning
        isRunning = False
        return True
def mark_complete(command, synonym):
        taskname = re.split(r'{}'.format(synonym),command)[1].strip()
        tl=  taskList.get_tasklist()
        # loop through tasks until correct one is found
        for t in tl:
                if t.get_name().lower() == taskname.lower().strip():
                        t.mark_complete()
                        return True
        return False


# initialize each command with it's own synoynms, and callback function
def initializeCommands():
        global Commands
        Commands['add task'] = {}
        Commands['add task']['synonyms'] = ['add task', 'new task', 'create task']
        Commands['add task']['action'] = add_task

        Commands['display tasks'] = {}
        Commands['display tasks']['synonyms'] = ['display', 'show tasklist', 'tasklist', 'show list']
        Commands['display tasks']['action'] = display_task

        Commands['quit'] = {}
        Commands['quit']['synonyms'] = ['quit', 'close', 'done']
        Commands['quit']['action'] = quit

        Commands['mark complete'] = {}
        Commands['mark complete']['synonyms'] = ['mark complete', 'check off', 'completed']
        Commands['mark complete']['action'] = mark_complete

# processes and executes commands
def processInput(command):
        global Commands
        for key in Commands:
                for synonym in Commands[key]['synonyms']:
                    if re.match("^{}".format(synonym),command):
                            # pass the command to the appropriate action function
                            return Commands[key]['action'](command,synonym)
        return False

        

def inputLoop():
        print("welcome to taskbot.")
        cmd = ""

        while isRunning:
                cmd = input("\t> ")
                if not processInput(cmd):
                        print('\t invalid command')

        


if __name__ == "__main__":
        initializeCommands()
        taskList = TaskList()
        inputLoop()