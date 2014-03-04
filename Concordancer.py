# Concordancer.py
print "Start"
import re

FileName = r'spacelessts.txt'

textfile = open(FileName)

data = textfile.read()

textfile.close()

SearchTerm = '/um/'

for matchstr in re.findall(SearchTerm, data):
    print matchstr