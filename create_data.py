from linear import *
import sys
fw=open(sys.argv[1],'w')
offset=0
while offset<100000:
  print_result(offset,fw)
  offset+=1000
