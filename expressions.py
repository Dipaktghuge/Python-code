import re
fout1= re.findall('^beast$', 'beast')
print(fout1)
fout1= re.findall('be.st', 'best')
print(fout1)
fout1= re.findall('^be\.st', 'be.st beast')
print(fout1)
fout1= re.findall('^be\?st', 'be?st beast')
print(fout1)
