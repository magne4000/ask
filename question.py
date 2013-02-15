#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 magne <magne@blondi>
#
# Distributed under terms of the MIT license.
import re

"""
Here are all classes used to handle different types of questions
"""

class Question:
    """
    Abstract class
    """

    def tostr(self):
        raise('This method must be overhidden')

    def call(self):
        if hasattr(self, 'callback'):
            self.callback()

class Answer:
    """
    Abstract class
    """

    def check(self, userinput):
        raise('This method must be overhidden')

class Text(Question, Answer):

    def __init__(self, text, callback):
        self.text = text
        self.callback = callback
        self.newline = True

    def tostr(self):
        return self.text

    def check(self, userinput):
        return True

    
class Choices(Question, Answer):
    """
    Multiple choices oriented questions class
    """

    def __init__(self, choices, callback):
        self.choices = choices
        self.callback = callback
        self.whitelist = [str(ind) for ind in range(1, len(choices))]

    def tostr(self):
        for i, s in enumerate(self.choices):
            yield "%d. %s" % (i, s)
        yield "\n"

    def check(self, userinput):
        if userinput in self.whitelist:
            return True
        return False

class YesNo(Choices):

    def __init__(self, text, callback):
        self.text = text
        self.callback = callback
        self.whitelist = ['y', 'n']

    def tostr(self):
        return (text + ' [y/n] ')

class Path(Text):
    pass
