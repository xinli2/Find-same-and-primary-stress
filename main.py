"""
    File: main.py
    Author: Xin Li
    Purpose: This program willl contain the functions
    compare_front(),compare_back(), and primary_stress().
    It will compare form front and back to find how many
    element same. It will find the location of the primary
    stress too.
"""

def compare_front(a,b):
    length = 0
    inner_length = 0
    count = 0
    element_a = ''
    element_b =''
    assert type(a) == type(b)
    if len(a) == len(b)==0:
        return 0
    if len(a) < len(b):
        length = len(a)
    else:
        length = len(b)
    for e in range(length):
        element_a = str(a[e])
        element_b= str(b[e])
        if element_a == element_b:
                count += 1
        else:
            return count
    return count

def compare_back(a,b):
    length = 0
    inner_length = 0
    count = 0
    element_a = ''
    element_b =''
    assert type(a) == type(b)
    if len(a) == len(b)==0:
        return 0
    if len(a) < len(b):
        length = len(a)
    else:
        length = len(b)
    for e in range(length):
        element_a = str(a[len(a)-e-1])
        element_b= str(b[len(b)-e-1])
        if element_a == element_b:
                count += 1
        else:
            return count
    return count

def primary_stress(c):
    assert isinstance(c, list)==True
    assert len(c) != 0
    for i in c:
        assert len(i) != 0
    for k in range(len(c)):
        if len(c[k]) == 3:
            if c[k][2].isdigit()==True:
                if int(c[k][2]) == 1:
                    return k
    return None
