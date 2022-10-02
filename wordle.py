"""Main module of game."""
from rich.console import Console

from Engine import Dict_handler, fiveletterword, Letter_handler, Visual_console


def run_game(maxtries):
    """Game loop."""
    dict_h = Dict_handler('./_data/_words/')
    dict = dict_h.create_dictionary()
    word2guess = fiveletterword(dict_h.choose_word(dict), '00000')

    letter_h = Letter_handler()
    lett = letter_h.get_letters()

    '''
    #hint for testing:
    print(word2guess)
    '''

    game = True
    tries = 0
    tries_list = []

    console.rule(f'[bold red]ROUND {tries + 1}', style='red')

    while game:

        """"Change available alphabet and print for user."""
        lett = letter_h.update_letters(tries_list, lett, word2guess)

        wordchoice = vconsole.game(maxtries, tries, tries_list, dict, lett)

        if wordchoice:
            wordchoice = vconsole.checkword(wordchoice, word2guess)
            tries_list.append(wordchoice)
        else:
            continue

        if wordchoice == word2guess:
            vconsole.table(maxtries, tries, tries_list)
            console.print(f'[red]Congratulations! Took{tries + 1} tries!')
            game = False
        else:
            console.print('false guess!')
            tries += 1
            if tries != maxtries:
                console.rule(f'[bold red]ROUND {tries + 1}', style='red')

        if tries == maxtries:
            vconsole.table(maxtries, tries, tries_list)
            console.rule('You lost!', style='red')
            console.print(f'The solution was {word2guess}', style='red')
            game = False


if __name__ == "__main__":

    console = Console()

    vconsole = Visual_console(console, 'red')

    wannacontinue = vconsole.setup()

    while wannacontinue:

        run_game(8)

        exitstatus = vconsole.exit()

        if exitstatus:
            wannacontinue = False
        else:
            continue
