HELP_MESSAGE = """usage: python3 main.py [arguments]
Arguments:
-c, --cli, cli   :   Play the text-based version of the game
-g, --gui, gui   :   Play the graphical version of the game
-h, --help, help :   Show this help message

Welcome to Hangman.
Hangman is a word guessing game. At the beginning of the game you will be asked
to input a word. You will want to get someone else to do this so that you don't
know the word. The you will need to guess the word one letter at a time. For
every incorrectly guessed letter, more parts of the gallows and the man will
appear until the gallows and man are complete and the man dead. Then you lose.
For every correctly guessed letter, it is revealed in its position in the word.
If you guess every letter in the word before the gallows and man are complete,
you win.

Copyright 2022 Benjamin Mickler

Hangman is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

Hangman is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
Hangman. If not, see <https://www.gnu.org/licenses/>."""