#!/usr/bin/python
# -*- coding:UTF-8 -*-

Tn = 0
Sn = []
n = int(raw_input('n = :\n'))
a = int(raw_input('a = :\n'))

for count in xrange(n):
	Tn += a
	a *= 10
	Sn.append(Tn)
	print Tn
Sn = reduce(lambda x, y : x + y, Sn)
print Sn