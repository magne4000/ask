#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Distributed under terms of the MIT license.
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass
from question import Question
import readline
import sys
import threading
try:
    import queue
except ImportError:
    import Queue as queue


class Ask:
    """
    A question/answer based prompt python lib which support multithreading
    """
    q = queue.Queue()

    @staticmethod
    def print_worker(q, ps):
        while True:
            item = q.get()
            if item is None:
                break
            ws = ' ' * (len(readline.get_line_buffer()) + 2)
            sys.stdout.write('\r{}\r{}'.format(ws, item))
            sys.stdout.write('{}{}'.format(ps, readline.get_line_buffer()))
            sys.stdout.flush()
            q.task_done()

    def __init__(self, prompt='-> '):
        self.ps = prompt
        self.print_t = threading.Thread(target=Ask.print_worker, args=(Ask.q, self.ps))
        self.print_t.daemon = True
        self.print_t.start()

    @staticmethod
    def _print(s, newline=True):
        Ask.q.put("{}{}".format(s, '\n' if newline else ''))

    def ask(self, q):
        """
        Prints the question and input for user answer
        """
        Ask._print(q.question())
        while True:
            q.before_raw_input()
            answer = input(self.ps)
            q.after_raw_input()
            if q.check(answer):
                a = q.answer(answer)
                if isinstance(a, Question):
                    return self.ask(a)
                else:
                    return a
