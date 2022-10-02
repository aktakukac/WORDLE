"""Visual controls and color coding of letters in game."""
from .engine import fiveletterword
from rich.prompt import Prompt
from rich.table import Table


class Visual_console:
    """Class for visuals."""

    def __init__(self, console, style='red'):
        """Start up visual console."""
        self.console = console
        self.style = style

    def setup(self):
        """Set up game header on console."""
        self.console.rule('[bold red] WORDLE', style='red')
        self.console.print('Guess a five letter word!')
        self.console.print(
            '''Your guess will be checked against my random choice'''
            )
        status = True
        return status

    def table(self, maxtries, tries, tries_list):
        """Draw table in game loop with coloring."""
        table = Table()
        table.add_column('Round', justify='center')
        table.add_column('Guesses', justify='center')

        for row_num in range(0, maxtries):
            if row_num <= tries:
                try:
                    guess = tries_list[row_num].coloring()
                except IndexError:
                    guess = '_____'
            else:
                guess = '_____'

            table.add_row(str(row_num + 1), guess)

        self.console.print(table)

    def game(self, maxtries, tries, tries_list, dict, lett):
        """Create table with previous guesses and future placeholders."""
        self.table(maxtries, tries, tries_list)

        abc_colored = ''
        for ltr in lett:
            abc_colored += (ltr.coloring() + ' ')
        self.console.print(abc_colored)

        """Print available tries for user."""
        self.console.print(f'[red]you have {maxtries-tries} guess remaining!',
                           style='red')

        """Ask for next guess."""
        wordchoice = Prompt.ask('[bold red]What is your word guess?')

        """Check and validate guess before returning it for the game."""
        wordchoice = wordchoice.lower()

        if len(wordchoice) != 5:
            self.console.print(
                f'Give a 5 letter word! yours was {len(wordchoice)} long ',
                style='red')
            return None

        wordchoice = fiveletterword(wordchoice.strip().lower(), '00000')

        if wordchoice not in dict:
            self.console.print('this word does not exist!', style='red')
            return None

        if str(wordchoice) in [str() for x in tries_list]:
            self.console.print('you have already tried this word!')
            return None

        return wordchoice

    def checkword(self, wordchoice, word2guess):
        """Check guessed word against hidden word."""
        wordchoice_str = str(wordchoice)
        word2guess_str = str(word2guess)

        wordchoice_set = set(wordchoice_str)
        word2guess_set = set(word2guess_str)

        new_colorcode = ['0', '0', '0', '0', '0']

        for i, lt in enumerate(wordchoice_str):
            if lt == word2guess_str[i]:
                new_colorcode[i] = '2'
                try:
                    word2guess_set.remove(lt)
                except IndexError:
                    continue
                continue
            else:
                for gt in word2guess_str:
                    if (gt in wordchoice_set) and (gt in word2guess_set):
                        if lt == gt:
                            new_colorcode[i] = '1'
                            try:
                                wordchoice_set.remove(gt)
                            except IndexError:
                                continue
                            continue

        new_colorcode_str = ''

        for cc in new_colorcode:
            new_colorcode_str += cc

        wordchoice = fiveletterword(wordchoice, new_colorcode_str)

        return wordchoice

    def exit(self):
        """Ask for continue before leaving the game."""
        ans = Prompt.ask('[bold red]Would you like to play once more?',
                         choices=['Y', 'N'], default='Y')

        if ans == 'Y':
            exitstatus = False
        else:
            exitstatus = True

        return exitstatus
