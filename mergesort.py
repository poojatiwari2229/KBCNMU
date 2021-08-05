# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:18:56 2021

@author: divya
"""

def partition(list1,lb,ub):
    pivot=list1[lb]
    start=lb
    end=ub
    temp=0
    while(start<end):
        while (start <= end and list1[start]<= pivot):
            start += 1
        while (start <= end and list1[end]>pivot):
            end -= 1
        if (start < end):
            temp = list1[start]
            list1[start] = list1[end]
            list1[end] = temp

    temp=list1[lb]
    list1[lb]=list1[end]
    list1[end]=temp
    return lb


def quick_sort(list1,lb,ub):
    loc=0
    if(lb<ub):
        loc=partition(list1,lb,ub)
        quick_sort(list1,lb,loc-1)
        quick_sort(list1,loc+1,ub)
    #print(list1)
    return list1

list1=list()
no=int(input('enter how many no wish to store in the list: '))
for i in range(no):
    list1.append(int(input('enter the no: ')))
print('items in list are befor sort :',list1)
print("after sorting list element are: ",quick_sort(list1,0,no-1))