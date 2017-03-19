import sage.all
import itertools
import datetime

def myFunction():
   f1 = open('./output.debug', 'w+')
   f1.write("Start time of program is : " + str(datetime.datetime.now()) + "\n")
   #nValue = 4
   #Zmod2 = SymmetricGroup(2)
   #Q8 = QuaternionGroup()
   #ZmodGroupN = Zmod2

   #for i in range(nValue - 1):
      #ZmodGroupN = direct_product_permgroups([ZmodGroupN, Zmod2])

   F = FreeGroup(3, [a,b,x])
   G = F/[a**8,b**4,x**2*a**-4,a*b*(b*a)**-1,x*a*((a**-1)*x)**-1,x*b*((b**-1)*x)**-1]
   f1.write(str(G) + "\n")
   #G = direct_product_permgroups([CyclicPermutationGroup(3),CyclicPermutationGroup(3)])
   #G1 = direct_product_permgroups([CyclicPermutationGroup(3),G])
   G1 = G.as_permutation_group()
   groupSize = G1.cardinality()
   f1.write(str(groupSize) + "\n")

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

   counter = 1
   for cs in combinationSize:
      f1.write("Iteration : " + str(counter) + "\n")
      counter += 1
      otherRandomCounter = 1
      for j in itertools.combinations(inverse1,cs):
         f1.write("Counter: " + str(otherRandomCounter) + "\n")
         otherRandomCounter+=1
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

   f1.write("Minimum value of the cardinality of automorphism groups of cayley graphs is : " + str(minGroupSize) + "\n")
   f1.write("r / |G| = " + str(minGroupSize / groupSize) + "\n")
   f1.write("Generating set is : \n")
   f1.write(generatingSet + "\n")
   f1.write("End time of program is " + str(datetime.datetime.now()) + "\n")


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