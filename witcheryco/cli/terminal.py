import re

from terminal_palette import Palette

pal = Palette()

def log(*texts, text_list=None):
    if text_list is not None:
        _texts = text_list
    else:
        _texts = texts

    for t in _texts:
        print(t)
    print() # empty line

def log_error(text):
    print(pal.red.bold.bg_default('[X] ' + text))

def format_error(text):
    return pal.red.bold.bg_default('[X] ' + text)

def format_warning(text):
    return pal.black.bg_yellow.bold('[!] ' + text)

def log_warning(text):
    print(format_warning(text))

def format_action(text):
    return pal.bright_blue.bg_default.bold('* ' + text)

def log_action(text):
    print(format_action(text))

def format_notice(text):
    return pal.bright_red.bg_default.bold('* ' + text)
    
def log_notice(text):
    print(format_notice(text))

def keystroke(text):
    return pal.black.bg_white.bold(' ' + text + ' ')

def title(text):
    return pal.yellow.bg_default.bold(text)


def prompt_int(prompt, coerse=False, min=None, max=None):
    """
    Prompts the user for an integer input with the given prompt.
    If `coerse = True`, forces the user to enter a input without an exit option
    """
    if type(min) is int:
        if type(max) is int:
            prompt += ' ' + pal.black.bg_white('[' + str(min) + ' - ' + str(max) + ']')
        else:
            prompt += ' ' + pal.black.bg_white('[' + str(min) + ' - ...]')
    else:
        if type(max) is int:
            prompt += ' ' + pal.black.bg_white('[... - ' + str(max) + ']')

    if not coerse:
        prompt += ' or enter ' + keystroke('..') + ' to cancel'

    prompt += ': '

    # Coerce loop
    while True:
        answer = input(prompt)

        if answer == '..' and not coerse:
            print()
            return None

        try:
            answer = int(answer)
            if type(min) is int and int(answer) < min:
                log_error('Your value must be higher than ' + str(min))
            elif type(max) is int and int(answer) > max:
                log_error('Your value must be less than ' + str(max))
            else:
                print()
                return answer
        except ValueError:
            log_error('You must enter a valid integer')


def prompt_float(prompt, coerse=False, min=None, max=None):
    """
    Prompts the user for a float input with the given prompt.
    If `coerse = True`, forces the user to enter a input without an exit option
    """
    if type(min) is float:
        if type(max) is float:
            prompt += ' ' + pal.black.bg_white([' + str(min) + ' - ' + str(max) + '])
        else:
            prompt += ' ' + pal.black.bg_white('[' + str(min) + ' - ...]')
    else:
        if type(max) is int:
            prompt += ' ' + pal.black.bg_white('[... - ' + str(max) + ']')

    if not coerse:
        prompt += ' or enter ' + keystroke('..') + ' to cancel'

    prompt += ': '

    # Coerce loop
    while True:
        answer = input(prompt)

        if answer == '..' and not coerse:
            print()
            return None

        try:
            answer = int(answer)
            if type(min) is int and int(answer) < min:
                log_error('Your value must be higher than ' + str(min))
            elif type(max) is int and int(answer) > max:
                log_error('Your value must be less than ' + str(max))
            else:
                return answer
        except ValueError:
            log_error('You must enter a valid integer')


def prompt_string(prompt: str, coerse=False, blacklist_word=None, black_patt=None, white_patt=None):
    """
    Prompts the user for a string input with the given prompt.
    If `coerse = True`, forces the user to enter a input without an exit option.
    `blacklist_word` is not case-sensitive.
    """
    if not coerse:
        prompt += ' or enter ' + keystroke('..') + ' to cancel'

    while True:
        forbids = False
        answer = input(prompt)

        if answer == '..' and not coerse:
            print()
            return None

        # check user input for blacklist pattern
        if black_patt is not None:
            # if the blacklist pattern is found
            if re.match(black_patt, answer) is not None:
                log_error(answer + ' may not be used as a response.')
                continue

        # check user input for blacklist pattern
        if white_patt is not None:
            # if the whitelist pattern is not found
            if re.match(white_patt, answer) is None:
                log_error(answer + ' may not be used as a response.')
                continue

        # check for forbidden words
        if blacklist_word is not None:
            # make answer case-insensitive
            lower_ans = answer.lower()
            for w in blacklist_word:
                # make forbidden word case-insensitive
                w = w.lower()

                if w in lower_ans:
                    log_error('You may not use the word \'' + w + '\'!')
                    forbids = True
                    break

            # if a improper answer is found
            if forbids is True:
                continue

        print()
        return answer


def prompt_choice(prompt: str, *menu_items: str, coerse=False):
    """
    Prompts the user for an int input with the given prompt and item list.
    If `coerse = True`, forces the user to enter a input without an exit option
    """
    # Construct the message
    if not coerse:
        prompt += '\nEnter ' + keystroke('..') + ' to cancel'

    for i in range(len(menu_items)):
        prompt += '\n' + keystroke(str(i + 1)) + ' ' + menu_items[i]

    prompt += '\nSelect via number: '

    # Coerce loop  
    while True:
        answer = input(prompt)

        if answer == '..' and not coerse:
            return None

        try:
            answer = int(answer)
            if answer <= 0 or answer > len(menu_items):
                log_error('This is not a valid number for a menu item')
                continue

            return menu_items[answer - 1]
        except ValueError:
            log_error('Please type in the number of the item you wish to select')

def prompt_choice_tree(prompt: str, *menu_items: tuple, coerce=False, menu_list=None):
    """
    Prompts the user for an int input with the given prompt and item list.
    If `coerse = True`, forces the user to enter a input without an exit option.
    The menu_items are tuples in the format of (str, function)
    """
    # Construct the message
    if not coerce:
        prompt += '\nEnter ' + keystroke('..') + ' to cancel'

    if menu_list is not None:
        items = menu_list
    else:
        items = menu_items

    for i in range(len(items)):
        prompt += '\n' + keystroke(str(i + 1)) + ' ' + items[i][0] # 0 is the str

    prompt += '\nSelect via number: '

    # Coerce loop  
    while True:
        answer = input(prompt)

        if answer == '..' and not coerce:
            return None

        try:
            answer = int(answer)
            if answer <= 0 or answer > len(items):
                log_error('This is not a valid number for a menu item')
                continue

            items[answer - 1][1]() # run the lambda
            return items[answer - 1]
        except ValueError:
            log_error('Please type in the number of the item you wish to select')