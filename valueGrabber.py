## -*- coding: utf-8 -*-
import re, sys, libs.test as test
print("The results of entrance exams are presented in the form of a list of N lines, each line of which contains the student's last name and marks for each of the h exams. Determine the number of applicants who have passed the entrance exams to \"5\". \n")

f = open('scheme.txt', 'r', encoding='utf-8')
scheme = str(f.read())
f.close()
f2 = open('dump.txt', 'r', encoding='utf-8')
dump = f2.readlines()
f2.close()


if len(sys.argv) > 1:
    if sys.argv[1] == 'test':
        testresults = []
        if sys.argv[2] == 'main':
            testresults.append(test.maintest(scheme, dump))
        
        partSuccessTesting = 0
        for i in range(len(testresults)):
            if testresults[i][0] == 1: partSuccessTesting += 1
            print(testresults[i][1])
        print("\nPercentage of successful tests:", partSuccessTesting/len(testresults)*100, "%\n")

achieversCount = 0

def detectAchiever(st):
    return re.search('( 5){3}$', st)


for i in range(len(dump)):
    if detectAchiever(dump[i]):
        achieversCount += 1
print ('The number of applicants who passed "5" - ', achieversCount)
