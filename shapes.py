"""
    File: shapes.py
    Author: Xin Li
    Purpose: This program willl declare five function: shape_alpha()
    shape_bravo(), shape_charlie(), shape_delta(), shape_echo().
    These functions must create a series of object (all Pytjon
    list objects, arranged in various fashions).
"""

def shape_alpha():
    lst_1=['','']
    lst_2 = [10,'','',40]
    lst_3 = ['','']
    lst_4 = [1.1,-17]
    lst_5 = [123,456]
    var_abc = "abc"
    var_jkl = "jkl"
    lst_1[0] = lst_2
    lst_2[1] = var_abc
    lst_2[2] = var_jkl
    lst_1[1] = lst_3
    lst_3[0] = lst_4
    lst_3[1] = lst_5
    return lst_1



def shape_bravo():
    var_whoa = "whoa"
    var_excellent="excellent"
    var_bogus ="bogus"
    var_righteous ="righteous"
    var_rufus = "rufus"
    lst = ['','']
    lst_1 = ['','']
    lst_2 = ['','']
    lst_3 = ['','']
    lst_4 = ['','']
    lst[0] = lst_1
    lst[1] = lst_4
    lst_1[0] = lst_2
    lst_2[0] = var_whoa
    lst_2[1] = var_excellent
    lst_3[0] = var_bogus
    lst_3[1] = var_righteous
    lst_1[1] = lst_3
    lst_4[1] = var_rufus
    lst_4[0] = lst_3
    return lst


def shape_charlie(arg1):
    lst = ['','']
    lst_1 = ['','']
    lst_2 = ['','']
    lst_3 = ['','']
    var_arg1 = arg1
    var_none = None
    lst[1] = var_arg1
    lst[0] = lst_1
    lst_1[0] = lst_2
    lst_1[1] = var_arg1

    lst_2[0] = lst_3
    lst_2[1] = var_arg1

    lst_3[0] = var_none
    lst_3[1] = var_arg1
    return lst

def shape_delta(arg1,arg2):
    lst = [arg1,arg2,'','']
    lst_1 = [arg1,'','',arg2]
    lst_2 = [arg1,arg2,'','']
    lst_3 = [arg1,arg2]
    lst_10 = [10]
    lst_20 = [20]
    lst_30 = [30]
    lst[2] = lst_1
    lst[3] = lst_10
    lst_1[1] = lst_2
    lst_1[2] = lst_20
    lst_2[2] = lst_3
    lst_2[3]= lst_30
    return lst

def shape_echo(arg1, arg2, arg3):
    lst = ['','']
    lst_1 = ['','']
    lst_2 = ['','']
    var_arg1 = arg1
    var_arg2 = arg2
    var_arg3 = arg3
    lst[1] = var_arg1
    lst[0] = lst_1
    lst_1[0] = lst_2
    lst_1[1] = arg2
    lst_2[0] = lst
    lst_2[1] = arg3
    return lst
