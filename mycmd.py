import os
from colorama import Fore, Style, init
import humanize

init(autoreset=True)

prev_dirs = []

def list_files_recursive(path, indent=""):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            print(f"{Fore.GREEN}{indent}[{item}]{Style.RESET_ALL}")
            list_files_recursive(item_path, indent + "  ")
        else:
            size = os.path.getsize(item_path)
            formatted_size = humanize.naturalsize(size)
            print(f"{Fore.RED}{indent}{item} ({Fore.YELLOW}{formatted_size}{Fore.RED}){Style.RESET_ALL}")

def change_directory(directory):
    try:
        prev_dirs.append(os.getcwd())
        os.chdir(directory)
        print(f"{Fore.MAGENTA}Current directory: {os.getcwd()}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.MAGENTA}Directory not found: {directory}{Style.RESET_ALL}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def make_directory(directory_name):
    try:
        os.makedirs(directory_name)
        print(f"{Fore.GREEN}Directory '{directory_name}' created.{Style.RESET_ALL}")
    except FileExistsError:
        print(f"{Fore.MAGENTA}Directory '{directory_name}' already exists.{Style.RESET_ALL}")

def make_file(file_name):
    with open(file_name, 'w') as file:
        print(f"{Fore.RED}File '{file_name}' created.{Style.RESET_ALL}")

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"{Fore.CYAN}Content of '{file_name}':\n{content}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.MAGENTA}File '{file_name}' not found.{Style.RESET_ALL}")

def print_working_directory():
    print(f"{Fore.MAGENTA}Current directory: {os.getcwd()}{Style.RESET_ALL}")

def back():
    if prev_dirs:
        os.chdir(prev_dirs.pop())
        print(f"{Fore.MAGENTA}Returned to previous directory: {os.getcwd()}{Style.RESET_ALL}")
    else:
        print(f"{Fore.MAGENTA}No previous directory available.{Style.RESET_ALL}")

def main():
    current_directory = os.getcwd()
    print(f"{Fore.MAGENTA}Welcome! Current directory: {current_directory}{Style.RESET_ALL}")

    while True:
        user_input = input(f"{Fore.MAGENTA}>> {Style.RESET_ALL}")

        if user_input.lower() == 'exit':
            print("Exiting. Goodbye!")
            break
        elif user_input.lower() == 'list':
            list_command(user_input)
        elif user_input.lower().startswith('cd '):
            _, directory = user_input.split(' ', 1)
            change_directory(directory)
        elif user_input.lower() == 'clear':
            clear_screen()
        elif user_input.lower().startswith('make dir '):
            _, directory_name = user_input.split(' ', 1)
            make_directory(directory_name)
        elif user_input.lower().startswith('make file '):
            _, file_name = user_input.split(' ', 1)
            make_file(file_name)
        elif user_input.lower().startswith('path'):
            print_working_directory()
        elif user_input.lower().startswith('list '):
            list_command(user_input)
        elif user_input.lower() == '..':
            back()
        else:
            print(f"{Fore.MAGENTA}Unknown command. Type 'list' to list files, 'cd <directory>' to change directory, 'clear' to clear the screen, 'mkdir <directory>' to create a directory, 'mkfile <file>' to create a file, 'pwd' to display the current directory, 'back' to go back to the previous directory, or 'exit' to exit.{Style.RESET_ALL}")

def list_command(user_input):
    _, *args = user_input.split()

    if "-r" in args:
        args.remove("-r")  # Remove -r from the arguments
        if len(args) == 1:
            read_file(args[0])
        else:
            print(f"{Fore.MAGENTA}Invalid usage of '-r' option. Specify a single file to read its content.{Style.RESET_ALL}")
    else:
        if len(args) == 0:
            path = os.getcwd()
        elif len(args) == 1:
            path = args[0]
        else:
            print(f"{Fore.MAGENTA}Invalid usage of 'list' command. Use 'list' or 'list <path>'{Style.RESET_ALL}")
            return

        list_files_recursive(path)


if __name__ == "__main__":
    main()
