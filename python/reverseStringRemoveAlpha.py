#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/15 7:57 PM
# @Author: wisdom
# @File:reverseStringRemoveAlpha.py


from typing import List
import re


def isCharacter(x: List[str]) -> List:
    listResult = []
    for elements in x:
        result = ''
        for index in range(len(elements)):
            if re.match(r'[A-Z|a-z]', elements[index]):
                result += elements[index]
                continue
            else:
                result += ' '
        listResult.append(result)
    listResult.reverse()
    return listResult


if __name__ == '__main__':
    strings = input()
    lists = strings.split(' ')
    resultList = isCharacter(lists)
    result = ''
    for ele in resultList:
        if ele:
            lt = ele.split()
        result += ' '.join(reversed(lt)) + ' '
    print(result.strip())
