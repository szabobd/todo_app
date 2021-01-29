TODO app documentation


Background: 
Given that the user has Python 3 installed on his computer with Windows operating system
Given the user pulled the directory of TODO app from GitHub (https://github.com/green-fox-academy/szabobd_github_handle-todo-app)

Feature: Listing arguments and counting done and undone tasks
Background:
	Given the user is using command line to open the directory
Scenario:	
	When the user inputs todo.py 
	Then the program should list the valid arguments the program accepts
	Then the program should also print the number of done and undone tasks

Feature: Listing all todos
Background: 
	Given the user is opened the directory in command line 
Scenario:
	Given the user already typed todo.py
	When the user types -l separated with a space from todo.py
	Then the program should print the list of all tasks, according to the order they were added
	Given that the list is empty, the program should print “No todos for today 😊”

Feature: Listing undone tasks
Background: 
Given the user is opened the directory in command line and the user already typed todo.py
Scenario:
	When the user types in -u, the program should list the tasks not marked as done according to 
	the order the tasks were added

Feature: Add new tasks
Background: 
Given the user is opened the directory in command line and the user already typed todo.py
Scenario:
When the user types in -a separated with a space, and then the task itself, separated with a space 
Then the program should add the new element to the end of the all tasks and to the end of undone tasks list, with the name given 

Feature: Add new task error handling
Background: 
Given the user is opened the directory in command line and the user already typed todo.py
Scenario:
Given the user types in the -a argument without a task written behind the argument separated with space, the program should print “Unable to add: no task provided”


Feature: Remove task
Background: 
Given the user is opened the directory in command line and the user already typed todo.py
Given that there are tasks on the all tasks list
Scenario:
Given the user types -r separated with a space after todo.py, and after -r a number, again, separated with a space
Then the program should remove the task associated with the number given from the task list

Feature: Remove task error handling
Background: 
Given the user is opened the directory in command line and the user already typed todo.py
Scenario:
Given the user types in the -r argument without a number written behind the argument separated with space, the program should print “Unable to remove: no index provided”
Scenario:
Given the user types in anything else then a number after the -r argument, the program should print “Unable to remove: index is not a number”

Feature: Check task
Background: 
Given the user is opened the directory in command line and the user already typed todo.py
Scenario:
Given the user types in the -c argument and a number after that, separated with a space, the program should mark the task associated with the number as done, and print an x in the square bracket between the number and the name of the task

Feature: Check task error handling
Background: 
Given the user is opened the directory in command line and the user already typed todo.py
Scenario:
Given the user types in the -c argument without a number written behind the argument separated with space, the program should print “Unable to check: no index provided”

