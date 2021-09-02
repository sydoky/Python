weight = set({50, 70, 80, 75, 35, 79})
print(weight)

year = {1987, 1997, 2003, 1984, 1995, 1993}
print(year)

year.add('eat')
print(year)


animals = ('bear', 'tiger', 'whale', 'cat', 'iguana')
animals2 = set(animals)
print(animals2)

#create a set of ood numbers from 1 to 70
odd_numbers = set(range(1, 71, 2))
print(odd_numbers)

normal_set = set(range(1, 41))
print(normal_set)

checking_union = (odd_numbers.union(normal_set))
print(checking_union)

checking_intersection = (odd_numbers.intersection(normal_set))
print(checking_intersection)

find_difference = (odd_numbers.difference(normal_set))
print(find_difference)

find_difference2 = (odd_numbers.difference_update(normal_set))
print(find_difference)

symmetric = (odd_numbers.symmetric_difference(normal_set))
print(symmetric)

symmetric = (normal_set.symmetric_difference(odd_numbers))
print(symmetric)