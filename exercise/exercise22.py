#!/use/bin/python
# -*- coding:UTF-8 -*-

for i in xrange(ord('x'),ord('z') + 1):
	for j in xrange(ord('x'),ord('z') + 1):
		if i != j:
			for k in xrange(ord('x'),ord('z') + 1):
				if  i != k and j != k:
					if i != ord('x') and k != ord('x') and k != ord('z'):
						print 'order is a -- %s\t b -- %s\t c-- %s' % (chr(i), chr(j), chr(k))