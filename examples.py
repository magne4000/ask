#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Distributed under terms of the MIT license.
import ask
import os
from question import Choices, YesNo, Text, Path

def handle_choices(answer):
    if answer == '1':
        return False
    return True

def main():
    a = ask.Ask()
    answer = a.ask(Choices('Kittens ?', ['Hell yeah!', 'NO!', 'Why not']))
    print('Without handle function, answer contains the user input value : ' + answer)
    answer = a.ask(Choices('Kittens ?', ['Hell yeah!', 'NO!', 'Why not'], handle_choices))
    print('With handle function, answer contains the computed value (False if 1, else True) : ' + str(answer))
    print('Now a simple YesNo question :')
    print(a.ask(YesNo('Is this real life ?')))
    res = a.ask(Path('What is your current full path ? (can autocomplete path with TAB)'))
    if res == os.getcwd():
        print('Yep you\'re there !')
    else:
        print('Nope you\'re not there !')


if __name__ == '__main__':
    main()
