import sys

for i in range(1,96):
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
            if il*il == immutableList[1]:
               print il