"""
Python Homework Assignment #8: Input and Output (I/O)
Details:
Create a note-taking program. When a user starts it up, it should prompt them for a filename.
If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. After they enter the text, it should save the file and exit.
If they enter a file name that already exists, it should ask the user if they want:
A) Read the file
B) Delete the file and start over
C) Append the file
If the user wants to read the file it should simply show the contents of the file on the screen.
If the user wants to start over then the file should be deleted and another empty one made in its place.
If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file.
Extra Credit:
Allow the user to select a 4th option:
D) Replace a single line
If the user wants to replace a single line in the file, they will then need to be prompted for 2 bits of information:
1) The line number they want to update.
2) The text that should replace that line.
"""
import os

filename = input("Please enter the filename: ")
# Here we check if the file exists
if os.path.isfile("./" + filename):
    print("Looking for file {}...".format(filename))
    print("Found it!")
    action = input(
        "What would you like to do with the file?\nPossible actions are: read, delete, append, replace\n")
    if action == "read":
        print("The content of the file:")
        with open(filename, "r") as read_file:
            print(read_file.read())
    elif action == "append":
        text = input("Please enter your note: ")
        with open(filename, "a") as append_file:
            append_file.write(text + "\n")
    elif action == "delete":
        os.remove("./" + filename)
        print("{} have been deleted.".format(filename))
        # I don't think it makes sense to create a new empty file right after deletion...
        # Anyway, this is the requested task so here it is
        with open(filename, "w") as write_file:
            write_file.write("")
    elif action == "replace":
        line_num = int(
            input("Please enter the line number for the replacement: "))
        text = input("Please enter your note: ")
        with open(filename, "r") as read_file:
            lines = read_file.readlines()
        with open(filename, "w") as write_file:
            for idx, line in enumerate(lines):
                # print(idx, line)
                if idx == line_num - 1:
                    print("Line num {} needs to be replaced!".format(line_num))
                    write_file.write(text + "\n")
                else:
                    print("Writing \"{}\"".format(line))
                    write_file.write(line)

    else:
        print("Sorry, unrecognized action 😢")
else:
    print("Nope, this file does not exist, I'm going to create it for you! 😄")
    text = input("Please enter your note: ")
    with open(filename, "w") as write_file:
        write_file.write(text + "\n")





"""
EZEBUIRO
UCHECHUKWU
VINCENT
"""