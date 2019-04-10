Project: Log Analysis 

Overview of the project:

My task is to create a reporting tool that prints out reports (in plain text) based on the data in the database.
This reporting tool is a Python program using the psycopg2 module to connect to the database.

Design of Code:

My code structure for this project is I have created a function called "print_answers()". Inside this function follows the method of excpetion using the try,catch and except functions.
The "try:" function is where all the code is processed and called and run by the main(): function. If the program is run and there are issues while running the program the "except:" function will 
will throw an exception error followed by an print statement of the error. Otherwise if the program runs successfully the following output will be produce in the git bash terminal.

Expected Output:

The most popular 3 articles of all time:
Candidate is jerk, alleges rival -- 338647 Views
Bears love berries, alleges bear -- 253801 Views
Bad things gone, say good people -- 170098 Views

The most popular authors of all time:
Ursula La Multa -- 507594 Views
Rudolf von Treppenwitz -- 423457 Views
Anonymous Contributor -- 170098 Views
Markoff Chaney -- 84557 Views

Days had more than 1% of requests lead to errors:
2016-07-17 -- 2.26% errors

How to run the python file:

Requirements:
- MUST have "FSND-VIRTUAL-MACHINE" File

Instructions:
1: Place the python file called "project1.py" inside the fsnd-virtual-machine => vagrant folder.
2: Open up Git Bash.
3: In the Git Bash terminal do a command directory to desktop "cd desktop" (For example the directory of where your folder is located maybe different but I have place the folder in my desktop).
4: In the Git Bash terminal do a command directory to the folder "fsnd-virtual-machine", cd fsnd-virtual-machine.
5: After doing a command directory to the "fsnd-virtual-machine" folder, do a command directory to the vagrant folder where your python file "project.py" is located. cd vagrant
6: Then once you have enter the vagrant folder, type 'ls' and press enter, you would want to do this step to make sure the directory you are in is where the python file is.
7: Once you have check that the python file is inside the vagrant folder, do a "vagrant up" to setup the local virtual machine.
8: Once that have been run, do a "vagrant ssh".
9: After you have enter into vargrant mode, do a "cd /vagrant".
10: Followed by that input the command 'ls'.
11: Once that has been done, do enter the following command "psql -d news -f newsdata.sql".
12: After this has been loaded you are all set to go.
13: Before we actually run the python file, you must intall the following package: "pip install psycopg2".
14: Once this has been installed, you are ready to run the python file.
15: Finally to run the file you enter the following command "python project1.py".
