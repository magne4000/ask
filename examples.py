#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Distributed under terms of the MIT license.
import ask
from question import Choices, YesNo, Text, Path

def handle_choices(answer):
    if answer == '1':
        return False
    return True

def handle1(answer):
    if answer.lower() == 'y':
        return True
    return False

def handle2(answer):
    print('The chosen path : ' + answer)
    return True

def main():
    a = ask.Ask()
    answer = a.ask(Choices('Kittens ?', ['Hell yeah!', 'NO!', 'Why not'], handle_choices))
    if answer:
        a.ask(YesNo('Is this real life ?', handle1))
    else:
        a.ask(Path('Where are you ?', handle2))

if __name__ == '__main__':
    main()
