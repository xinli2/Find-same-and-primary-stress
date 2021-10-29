"""
    File: cover_list_code.py
    Author: Xin Li
    Purpose: This program will import a file teacher provided.
    It will test and cover all the line that the teacher's
    program.
"""
from list_insert import *


def main():
    obja = ListNode( ('02','03') )
    objb = ListNode( ('12','02') )
    objc = ListNode( ('02','02') )
    objd = ListNode( ('02','03') )
    obje = ListNode( ('02','04') )
    obje.next = ListNode( ('02','04') )

    data = sorted_list_insert(None, obja)
    data = sorted_list_insert(data, objb)
    data = sorted_list_insert(data, objc)
    data = sorted_list_insert(data, objd)
    data = sorted_list_insert(data, obje)
    data = sorted_list_insert(obje, objc)
    data = sorted_list_insert(None, None)
    head = None
    print_list(head)
    data = sorted_list_insert(None, ListNode( ('01','01') ))
    data = sorted_list_insert(data, ListNode( ('03','03') ))
    data = sorted_list_insert(data, ListNode( ('02','02') ))
    print_list(data)

if __name__ =="__main__":
    main()
