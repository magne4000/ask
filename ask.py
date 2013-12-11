#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Distributed under terms of the MIT license.
from question import Question
import readline, sys, struct, fcntl, termios

"""
A question/answer based prompt python lib
"""

class Ask:

    asking = False

    def __init__(self, prompt='-> '):
        self.ps = prompt

    @staticmethod
    def _print(s, newline=True):
        """
        Prints something only if a prompt is not displayed
        """
        if not Ask.asking:
            sys.stdout.write('\r'+s)
            if newline:
                sys.stdout.write('\n')
            sys.stdout.flush()

    def ask(self, q):
        """
        Prints the question and input for user answer
        """
        print('\n'+q.question())
        while True:
            Ask.asking = True
            q.before_raw_input()
            answer = raw_input(self.ps)
            q.after_raw_input()
            if q.check(answer):
                a = q.answer(answer)
                if isinstance(a, Question):
                    Ask.asking = False
                    return self.ask(a)
                else:
                    Ask.asking = False
                    return a
