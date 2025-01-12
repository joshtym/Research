
# This file was *autogenerated* from the file /home/dragon/Programming/research/part2.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_96 = Integer(96)
import sys

for i in range(_sage_const_1 ,_sage_const_96 ):
   print("All Groups of order " + str(i))
   print("------------------------------")
   for g in gap.AllSmallGroups(i):
      if gap.IsCommutative(g):
         print(gap.StructureDescription(g))
         print("-------------------------")
         print("FIND ALL INVOLUTIONS")
         print("------------------------")
         immutableList = gap.Enumerator(g)
         for il in immutableList:
            if il*il == immutableList[_sage_const_1 ]:
               print il

