#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 magne <joel.charles@getonmyhor.se>
#
# Distributed under terms of the MIT license.
import re, readline, glob

"""
Here are all classes used to handle different types of questions
"""

class Question:
    """
    Abstract class
    """

    def before_raw_input(self):
        pass

    def after_raw_input(self):
        pass

    def question(self):
        raise('This method must be overhidden')

    def answer(self, answer):
        if hasattr(self, 'callback') and self.callback is not None:
            return self.callback(answer)
        return answer

    def check(self, userinput):
        raise('This method must be overhidden')

class Text(Question):

    def __init__(self, text, callback=None):
        self.text = text
        self.callback = callback
        self.newline = True

    def question(self):
        return self.text

    def check(self, userinput):
        return True

class Float(Text):

    def __init__(self, text, callback=None):
        self.text = text
        self.callback = callback
        self.newline = True

    def check(self, userinput):
        try:
            float(userinput)
        except ValueError:
            return False
        return True

class Regex(Text):

    def __init__(self, text, regex, callback=None):
        self.text = text
        self.regex = re.compile(regex)
        self.callback = callback
        self.newline = True
    
    def check(self, userinput):
        return self.regex.match(userinput) is not None

class Choices(Question):
    """
    Multiple choices oriented questions class
    """

    def __init__(self, text, choices, callback=None):
        self.text = text
        self.choices = choices
        self.callback = callback
        self.whitelist = [str(ind) for ind in range(1, len(choices) + 1)]

    def question(self):
        return self.text + "\n" + "\n".join(["%d. %s" % (i+1, s) for i, s in enumerate(self.choices)])

    def check(self, userinput):
        if userinput in self.whitelist:
            return True
        return False

class YesNo(Choices):

    def __init__(self, text, callback=lambda a: a.lower() == 'y'):
        self.text = text
        self.callback = callback
        self.whitelist = ['y', 'n']

    def question(self):
        return (self.text + ' [y/n] ')

class Path(Text):

    def _complete(self, text, state):
        return (glob.glob(text+'*')+[None])[state]

    def before_raw_input(self):
        readline.set_completer_delims(' \t\n;')
        readline.parse_and_bind('tab: complete')
        readline.set_completer(self._complete)

    def after_raw_input(self):
        readline.set_completer()
