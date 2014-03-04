# Concordancer.py
print "Start"
import re

FileName = r'spacelessts.txt'

textfile = open(FileName)

data = textfile.read()

textfile.close()

SearchTerm = '.(30)a*(30)'

for matchstr in re.findall(SearchTerm, data):
    print matchstr