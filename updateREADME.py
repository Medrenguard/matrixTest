## -*- coding: utf-8 -*-
f = open('dump.txt')
f2 = open('README.md', 'w')
f2.write(f.read())
f.close()
f2.close()