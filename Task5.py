#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
from distutils import text_file
import os


dir = 'files'
text_file =[file for file in os.listdir(dir) if file.endswith (".txt")]

result={}
for txt_file in txt_files:
    with open (f'{dir}\\{txt_file}',encoding=='utf-8') as data:
        polynom = filter(lambda x: x not in ('+', '=', '0'), data.read().split())
        for term in polynom:
            if'x^' in term:
                ratio,power= map(lambda x: int(x) if x else 1, term.split('x^'))
                result[power]= result.get(power,0)+ ratio
            elif'x'in term:
                ratio,_=map(lambda x: int(x)if x else 1, term.get(1,0)+ratio)
            else:
              result[0]=result.get(0,0)+int(term)
            result=sorted(result.items(),revers=True)
            terms=[]
            for power,ratio in result:
                ratio=ratio if power ==0 else'' if power==0 else ratio
                power='x'if power==1 else'' if power==0 else f'{ratio}{power}'
                terms.append(term) 

sum_polynom='+'.join(terms) + "=0"
print(sum_polynom)