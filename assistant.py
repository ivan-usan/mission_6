filename = None

def file_cmd(command_str):
    """
    pre: `command_str`: str of format `file <file>`
    post: returns :str
          - Either the message that informs that file was found
          - Or the message with exception, if there exists some troubles with file or format
    """
    global filename

    args = command_str.split(' ')[1:]

    if len(args) == 0:
        return 'You haven\'t entered the file name'

    filename = args[0]

    try:
        with open(filename, 'r') as f: # checks the possibility to load the file
            pass

        return f'Loaded {filename}'
    except FileNotFoundError:
        return 'Error because file not found' 
    except:
        return 'Uknown exception'


def info_cmd(command_str):
    pass

def words_cmd(command_str):
    pass

def search_cmd(command_str):
    pass

def sum_cmd(command_str):
    """
    pre: `command_str`: str of format `sum <number1> ... <numbern>`
    post: returns :str
          - Either the message with sum value
          - Or the message with exception, if the format was ignored
    """
    args = command_str.split(' ')[1:]

    if len(args) == 0:
        return 'You haven\'t entered the numbers'

    try:
        sum_ = sum(float(number) for number in args)
        return f'Summary equals to {sum_}'
    except ValueError:
        return ('Error in provided numbers\n' 
                'Remember the number needs to have the digits from 0 to 9 and for real numbers use `.` instead of `,`')
    except:
        return 'Uknown exception'

def avg_cmd(command_str):
    """
    pre: `command_str`: str of format `avg <number1> ... <numbern>`
    post: returns :str
          - Either the message with average value
          - Or the message with exception, if the format was ignored
    """

    args = command_str.split(' ')[1:]

    if len(args) == 0:
        return 'You haven\'t entered the numbers'

    try:
        avg = sum(float(number) for number in args) / len(args)
        return f'Average equals to {avg}'
    except ValueError:
        return ('Error in provided numbers\n' 
                'Remember the number needs to have the digits from 0 to 9 and for real numbers use `.` instead of `,`')
    except:
        return 'Uknown exception'

def help_cmd(command_str):
    return '\n'.join(["file <name>: specify the name of the file on which program will work from this moment",
                      "info: show the number of the lines and characters in the specified file",
                      "words: specify the current file as the words list from this moment",
                      "search <word>: determines whether word is inside current words list",
                      "sum <number1> ... <numbern>: calculates the sum of specified numbers (real, not only integer)", 
                      "avg <number1> ... <numbern>: calculates the average of specified numbers (real, not only integer)",
                      "help: shows all available commands",
                      "exit: stops the program"])

commands = {
    "sum": sum_cmd,
    "avg": avg_cmd,
    "help": help_cmd,
    "file": file_cmd,
    "info": info_cmd,
    "words": words_cmd,
    "search_cmd": search_cmd
}

if __name__ == '__main__':
    print('Welcome to your personalized tool!')
    while True:
        command_str = input('> ').strip()
        command = command_str.split(' ')[0]
    
        if command_str == 'exit':
            break
        elif command in commands:
            msg = commands[command](command_str)
            print(msg)
        else:
            print('You have entered the incorrect command, use help if you don\'t remember some command.')
