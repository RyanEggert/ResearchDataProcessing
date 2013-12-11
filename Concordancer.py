# Concordancer.py
print "Start"
import re

FileName = r'C:\Users\reggert\Documents\My Box Files\Olin\Research\Groupwork Project\Transcription\Plaintext Transcripts\Team I.txt'

textfile = open(FileName)

data = textfile.read()

textfile.close()

SearchTerm = 'yeah'

for matchstr in re.findall(SearchTerm, data):
    print matchstr