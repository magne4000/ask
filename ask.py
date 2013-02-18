#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Distributed under terms of the MIT license.

"""
A question/answer based prompt python lib
"""

class Ask:

    def __init__(self, prompt='-> '):
        self.ps = prompt

    def ask(self, q):
        print(q.question())
        while True:
            q.before_raw_input()
            answer = raw_input(self.ps)
            q.after_raw_input()
            if q.check(answer):
                return q.answer(answer)

