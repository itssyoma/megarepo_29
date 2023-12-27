#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def is_valid_sk(s):
    def is_valid(s, balance):
        if not s:
            return balance == 0
        elif balance < 0:
            return False
        else:
            if s[0] == '(':
                return is_valid(s[1:], balance + 1)
            elif s[0] == ')':
                return is_valid(s[1:], balance - 1)
            else:
                return is_valid(s[1:], balance)

    return is_valid(s, 0)


if __name__ == "__main__":
    s = input("Введите выражение со скобками: ")

    if '(' not in s or ')' not in s:
        print("Выражение не содержит скобок", file=sys.stderr)
        exit(1)

    if is_valid_sk(s):
        print("Скобки расставлены верно")
    else:
        print("Скобки расставлены неверно")
