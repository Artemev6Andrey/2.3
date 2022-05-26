#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Дана последовательность слов. Проверить, правильно ли в ней записаны буквосочетания
жи и ши."""

if __name__ == '__main__':
    s = input()
    s1 = s.replace('жы', 'жи')
    s1 = s1.replace('шы', 'ши')

    if s1 == s:
        print('Ok')
    else:
        print('Есть ошибки')
