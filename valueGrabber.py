## -*- coding: utf-8 -*-
import re
print("Результаты вступительных экзаменов представлены в виде списка из N строк, в каждой строке которого записаны фамилия студента и отметки по каждому из h экзаменов. Определить количество абитуриентов, сдавших вступительные экзамены на \"отлично\". \n")

defFile = 'dump.txt'

achieversCount = 0

def detectAchiever(st):
    return re.search('( 5){3}$', st)

with open(defFile) as f:
    arr = f.readlines()
    for i in range(len(arr)):
        if detectAchiever(arr[i]):
            achieversCount += 1
    print('Количество абитуриентов, сдавших на "отлично" -', achieversCount)
