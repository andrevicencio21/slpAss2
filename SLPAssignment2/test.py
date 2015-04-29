import enrol
import os

e = enrol.Enrol(r'C:\Users\andre1\git\slpAss2\SLPAssignment2')
print os.listdir(e.path)
enrol.read_lines('SUBJECTS')