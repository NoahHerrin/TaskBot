from TaskManager import TaskList
import re
import sys

Commands = {}
taskList = None
isRunning = True
OUTPUTFNAME = 'taskdata.txt'

# an action function for the 'add task' command
def add_task(command, synonym):
        global taskList
        # split keywords from command params
        taskname = re.split(r'{}'.format(synonym),command)[1].strip()
        if taskname is not "":
                taskList.add_task(taskname)
                return True
        else:
                return False

# an action function for the 'display task' command
def display_task(command,synonym):
        print(taskList)
        return True

# an action function for the 'quit' command
def quit(command, synonym):
        global isRunning
        isRunning = False
        save_to_file()
        return True

def mark_complete(command, synonym):
        taskname = re.split(r'{}'.format(synonym),command)[1].strip()
        tl=  taskList.get_tasklist()
        # search for taskname
        for t in tl:
                if t.get_name().lower() == taskname.lower().strip():
                        # task was found, mark as complete
                        t.mark_complete()
                        return True
        # task specified does not exist
        return False

def save_to_file():
        file = open(OUTPUTFNAME, "w")
        tasklist = taskList.get_tasklist()
        for task in tasklist:
                file.write("{},{}\n".format(task.get_name(), task.is_complete()))
        file.close()
def read_from_file():
        file = open(OUTPUTFNAME, "r")
        for line in file:
                line = line.rstrip().split(",")
                taskList.add_task(line[0])

                if line[1].lower() == "true":
                        mark_complete("mark complete {}".format(line[0]), 'mark complete')
                
                

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
        read_from_file()
        inputLoop()