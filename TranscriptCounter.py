import xlrd

PythonRows = []
PythonCopy = []
# Transcript Location
transcriptfilepath = r'C:\Users\reggert\Dropbox\Discourse Files 2013-2014\Analysis\Team III.xls'

fullbook = xlrd.open_workbook(filename=transcriptfilepath)

Trans = fullbook.sheet_by_index(0)  # This will take the 1st (for n=0) sheet

for column_index in range(2):
    for row_index in range(Trans.nrows):
        cell = Trans.cell(row_index, column_index)
        PythonRows.append(cell)
    print PythonRows
    PythonCopy.append(PythonRows)

print len(PythonCopy)