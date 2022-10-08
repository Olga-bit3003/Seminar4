
from random import randint
max_val=100
k = int(input('Введите натуральную степень k:'))
coeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(coeff) if j][::-1])
poly=poly.replace('x^1+', 'x+')
poly=poly.replace('x^0', '')
poly+=('','1')[poly[-1]=='+']
poly=(poly, poly[:-2])[poly[-2:]=='^1']
print(poly)

with open ('file1.txt', 'w') as data:
    data.write(str(poly).replace('**','^')+"=0")