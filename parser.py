#!/usr/bin/python
import sys
line = []
indexes = []
list_arg = 0
if len(sys.argv) == 2:        
	index = int(sys.argv[1])
else:        
	list_arg = 1        
	indexes = sys.argv[1:]
for data in sys.stdin:        
	line = data.split(',')        
	if list_arg == 0:                
		print "{0}\t1".format(line[index])        
	else:                
		string = ""                
		for index in indexes:                        	
			string = string+line[int(index)]                        
			if (index == indexes[-1]):                                
				string = string+"\t1"                        
			else:                                
				string = string+","                
		print string
