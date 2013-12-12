# Concordancer.py
print "Start"
import re

FileName = r'Insert filepath'

textfile = open(FileName)

data = textfile.read()

textfile.close()

SearchTerm = 'yeah'

for matchstr in re.findall(SearchTerm, data):
    print matchstr