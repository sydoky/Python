def function(laptop):
    maximum = laptop[0]
    minimum = laptop[0]
    for tree in laptop:
        if tree > maximum:
            maximum = tree
        if tree < minimum:
            minimum = tree
    return maximum + minimum

print(function([1, 2, 3, 4, 5 ,6 ,7 ,8]))
