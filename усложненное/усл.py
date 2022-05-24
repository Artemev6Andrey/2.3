#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Дано предложение. Определить количество слов:
начинающихся с буквы н;
оканчивающихся буквой р."""

if __name__ == '__main__':
    t = input()
    r = sum(1 for x in t.split() if x[0] == "н")
    q = sum(1 for x in t.split() if x[-1] == "р")
    print(r, q)
