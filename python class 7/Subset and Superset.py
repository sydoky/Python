#Two ways to remove items from sets
#SUPER SET & SUBSET

##SUBSET:
even_set={2,4,6,8,10}
a={4,6,10}
b={5,7,9,10}

if a.issubset(even_set):
    print("True")

else:
    print("False")
print("--------")

if b.issubset(even_set):
    print("True")

else:
    print("False")
print("--------------------------")
print("--------------------------")

#SUPERSET
if even_set.issuperset(a):
    print("True SUPER")

else:
    print("False SUPER")
print("-----")
if even_set.issuperset(b):
    print("True SUPER")

else:
    print("False SUPER")
