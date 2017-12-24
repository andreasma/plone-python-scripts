#!/usr/bin/env python


file1 = raw_input('Please type in the name of the first file you want to compare \n'
                  'of identical users, that has not been active on the platform yet: ')

file2 = raw_input('Please type in the name of the second file with not active users that\n'
                  'you want to compare with the content of the file you typed in before: ')


# Create two sets from the listed items of the two text files and intersect them.
# Make a list of the matching items and write the items of this list to a text file.
# The list contains the active users of the site.

print (file1)
print (file2)

data = [line.strip() for line in open(file1, 'r')]

data2 = [line.strip() for line in open(file2, 'r')]


set1 = set(data)
set2 = set(data2)
set3 = set1.intersection(set2)

found = []
for match in set3:
    found.append(match)
    
with open('longnotactiveusers.txt', 'ab') as notactive:
    for item in found:
        notactive.write("%s\n" % item)
