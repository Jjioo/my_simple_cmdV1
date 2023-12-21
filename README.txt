MySimpleCMD - Command Line Interpreter

Welcome to MySimpleCMD, a basic command-line interpreter implemented in Python.

Commands:
1. `list [-r] [path]`: List files and directories. Use the `-r` option to read the content of a file.
   Examples:
   - `list`: List files and directories in the current directory.
   - `list -r file.txt`: Display the content of the file.txt.

2. `cd <directory>`: Change the current directory.
   Example: `cd my_directory`

3. `clear`: Clear the console screen.

4. `mkdir <directory>`: Create a new directory.
   Example: `mkdir my_directory`

5. `mkfile <file>`: Create a new file.
   Example: `mkfile my_file.txt`

6. `pwd`: Display the current working directory.

7. `back`: Return to the previous directory.

8. `exit`: Exit SimpleCMD.

Usage:
- Enter a command and press Enter to execute.
- Use `list`, `cd`, `clear`, `mkdir`, `mkfile`, `pwd`, `back`, or `exit` followed by appropriate parameters.
- For the `list` command, use `-r` to read the content of a file.

Note:
- When creating directories or files, the script operates in the current working directory.
- Use the `cd` command to navigate between directories.

Enjoy using MySimpleCMD!---Sahraoui Tarek Ziad
