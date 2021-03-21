import operator
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

str = input("Please enter a string: ")
most_frequent(str)
sorted_d =sorted(most_frequent(str).items(), key=operator.itemgetter(1), reverse=True)
print(sorted_d)