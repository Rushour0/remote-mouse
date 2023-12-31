
# Function definition - colorstr
def colorstr(*input):
    # Colors a string https://en.wikipedia.org/wiki/ANSI_escape_code
    *args, string = input if len(input) > 1 else ('blue', 'bold', input[0])
    colors = {'black': '\033[30m',
              'red': '\033[31m',
              'green': '\033[32m',
              'yellow': '\033[33m',
              'blue': '\033[34m',
              'magenta': '\033[35m',
              'cyan': '\033[36m',
              'white': '\033[37m',
              'bright_black': '\033[90m',
              'bright_red': '\033[91m',
              'bright_green': '\033[92m',
              'bright_yellow': '\033[93m',
              'bright_blue': '\033[94m',
              'bright_magenta': '\033[95m',
              'bright_cyan': '\033[96m',
              'bright_white': '\033[97m',
              'end': '\033[0m',
              'bold': '\033[1m',
              'italic': '\033[3m',
              'underline': '\033[4m',
              'strikethrough': '\033[9m'
              }

    return ''.join(colors[x] for x in args) + f'{string}' + colors['end']