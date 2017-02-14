import sage.all
import itertools
import datetime

def myFunction():
   print("Start time of program is : " + str(datetime.datetime.now()))
   nValue = 1
   Zmod2 = SymmetricGroup(2)
   Q8 = QuaternionGroup()
   ZmodGroupN = Zmod2

   for i in range(nValue - 1):
      ZmodGroupN = direct_product_permgroups([ZmodGroupN, Zmod2])

   G1 = direct_product_permgroups([Q8, ZmodGroupN])
   groupSize = G1.cardinality()

   inverse1 = []
   inverse2 = []
   setsOfInverseClosed = []
   combinationSize = []
   generatingSets = []
   sizeOfAut = []
   minGroupSize = 100000000
   generatingSet = []

   for g in G1:
      for h in G1:
         if str(g*h) == "()":
            if g == h:
               inverse1.append(g)
               inverse2.append(h)
            else:
               if h not in inverse1:
                  inverse1.append(g)
                  inverse2.append(h)

   counter = 1
   for i in inverse1:
      combinationSize.append(counter)
      counter = counter + 1

   for cs in combinationSize:
      for j in itertools.combinations(inverse1,cs):
         testList1 = []
         for k in list(j):
            testList1.append(k)
         testList2 = []
         for k in testList1:
               testList2.append(inverse2[inverse1.index(k)])
         for k in testList2:
            testList1.append(k)
         #setsOfInverseClosed.append(list(set(testList1)))
         setInverseClosed = list(set(testList1))
         perm = PermutationGroup(setInverseClosed)
         if perm.cardinality() == groupSize:
            size = G1.cayley_graph(generators=setInverseClosed).to_undirected().automorphism_group().cardinality()
            if size < minGroupSize:
               minGroupSize = size
               generatingSet = setInverseClosed

   print("Minimum value of the cardinality of automorphism groups of cayley graphs is : " + str(minGroupSize))
   print("r / |G| = " + str(minGroupSize / groupSize))
   print("Generating set is : ")
   print(generatingSet)
   print("End time of program is " + str(datetime.datetime.now()))


   #for s in setsOfInverseClosed:
#      perm = PermutationGroup(s)
#      isActualSet = True
#      if perm.cardinality() == groupSize:
#         generatingSets.append(s)#

#   for gs in generatingSets:
#      sizeOfAut.append(G1.cayley_graph(generators=gs).to_undirected().automorphism_group().cardinality())#

#   print("Minimum value of the cardinality of automorphism groups of cayley graphs is : " + str(min(sizeOfAut)))
#   print("r / |G| = " + str(min(sizeOfAut) / G1.cardinality()))
#   print("End time of program is " + str(datetime.datetime.now()))
   
myFunction()