"""Module handle dictionary, word and letter objects."""
import os
from random import choice


class fiveletterword:
    """Class object to handle words."""

    def __init__(self, word, colorcoding):
        """Initiate of fiveletterword object with colorcoding."""
        self.word = word
        self.colorcoding = colorcoding

    def coloring(self):
        """Colorize word for rich print."""
        colorized_word = ''
        for i, lt in enumerate(str(self.word)):
            if int(self.colorcoding[i]) == 0:
                color = 'grey3'
            elif int(self.colorcoding[i]) == 1:
                color = 'black on bright_yellow'
            elif int(self.colorcoding[i]) == 2:
                color = 'black on green'
            else:
                raise ValueError()

            colorized_word += f'[{color}]{lt}[/{color}]'

        return colorized_word

    def __str__(self):
        """Represent string for printing."""
        return f'{self.word}'

    def __repr__(self):
        """Represent string for other use."""
        return f'{self.word}'

    def __eq__(self, other):
        """Equal sign."""
        return self.word == other.word


class letter:
    """Class to handle letters along the game."""

    def __init__(self, letter, availability, orderkey):
        """Initiate letter object."""
        self.letter = letter
        self.availablity = availability
        self.orderkey = orderkey

    def coloring(self):
        """Return letter with coloring for printing on console."""
        if self.availablity == 0:
            color = 'black'
        elif self.availablity == 1:
            color = 'grey93'
        elif self.availablity == 2:
            color = 'black on green'
        else:
            raise ValueError()

        return f'[{color}]{self.letter}[/{color}]'

    def __str__(self):
        """Represent letter for printing."""
        return f'{self.letter}'

    def __eq__(self, other):
        """Equal for comparison."""
        return self.orderkey == other.orderkey

    def __ne__(self, other):
        """Not equal for comparison."""
        return self.orderkey != other.orderkey

    def __lt__(self, other):
        """Larger than for comparison."""
        return self.orderkey < other.orderkey

    def __le__(self, other):
        """Larger or equal for comparison."""
        return self.orderkey <= other.orderkey

    def __gt__(self, other):
        """Greater than for comparison."""
        return self.orderkey > other.orderkey

    def __ge__(self, other):
        """Greater than or equal for comparison."""
        return self.orderkey >= other.orderkey

    def __cmp__(self, other):
        """Comparison magic method."""
        return self.orderkey == other.orderkey

    def __repr__(self):
        """Representaton of letter."""
        return f'{self.letter}, {self.availablity}, {self.orderkey}'


class Letter_handler:
    """Class for handling letters."""

    def __init__(self):
        """Initiate letter object with alphabet."""
        abc = [
            'a', 'á', 'b', 'c', 'cs', 'd', 'dz', 'dzs', 'e', 'é', 'f',
            'g', 'gy', 'h', 'i', 'í', 'j', 'k', 'l', 'ly', 'm', 'n', 'ny',
            'o', 'ó', 'ö', 'ő', 'p', 'r', 's', 'sz', 't', 'ty', 'u', 'ú', 'ü',
            'ű', 'v', 'x', 'y', 'z', 'zs'
            ]

        abc_n = []

        for ltr in abc:
            # csak egyszavas betűk játszanak most
            if len(ltr) == 1:
                abc_n.append(ltr)

        abc = abc_n

        abc_dict = dict()

        for i, ltr in enumerate(abc):
            abc_dict[ltr] = i
        self.abc_dict = abc_dict

        alphabet = []

        for ltr in abc:
            alphabet.append(letter(ltr, 0, abc_dict[ltr]))
        self.alphabet = alphabet

    def get_letters(self):
        """Return all letters in the object."""
        return self.alphabet

    def update_letters(self, tries_list, lett, word2guess):
        """Update letters during checking."""
        tried_letters = set()
        for tries in tries_list:
            for lt in str(tries):
                tried_letters.add(lt)

        solution_letters = set()
        for lt in str(word2guess):
            solution_letters.add(lt)

        all_letters = set()
        for lt in lett:
            all_letters.add(str(lt))

        new_lett = []

        untried_letters = all_letters.difference(tried_letters)

        for lt in list(untried_letters):
            new_lett.append(letter(lt, 0, self.abc_dict[lt]))

        tried_correct = tried_letters.intersection(solution_letters)

        for lt in list(tried_correct):
            new_lett.append(letter(lt, 2, self.abc_dict[lt]))

        tried_incorrect = tried_letters.difference(tried_correct)

        for lt in list(tried_incorrect):
            new_lett.append(letter(lt, 1, self.abc_dict[lt]))

        new_lett = sorted(new_lett, key=lambda x: x.orderkey)
        return new_lett


class Dict_handler:
    """Class to handle dictionary files."""

    def __init__(self, path: str):
        """Initiate dict handler object."""
        self.path = path

    def create_dictionary(self):
        """Open dictionary files and return a word list."""
        word_files = [
                'freedict.txt'
                ]

        words = []

        for word_file in word_files:
            path = os.path.join(self.path, word_file)
            with open(path) as f:
                f.seek(0, 0)
                for line in f.readlines():
                    if len(line.strip()) == 5:
                        word = fiveletterword(line.strip().lower(), '00000')
                        words.append(word)

        return words

    def choose_word(self, words) -> str:
        """Chose a random word."""
        return choice(words)
