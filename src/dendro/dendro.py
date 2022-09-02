

import plotly.figure_factory as ff
import numpy as np
import json
from os.path import exists
import concurrent.futures

import subprocess as sp


# To get the "tarred and feathered" Android apps, email jedimaestro@asu.edu
# Or see README.md to generate your own
def comparethem(num1, num2):
    print('comparing ' + num1 + ' and ' + num2)
    fn1 = '/home/jedi/tmp/anzhitarredandfeathered/strsonly/' + num1 + '.apk.tgz.txt'
    fn2 = '/home/jedi/tmp/anzhitarredandfeathered/strsonly/' + num2 + '.apk.tgz.txt'
    output = sp.getoutput('./compare ' + fn1 + ' ' + fn2)
    return float(output)


# Again, to get the inputs in terms of apps and app data in JSON format, contact jedimaestro@asu.edu
data = json.load(open('/home/jedi/tmp/anzhitarredandfeathered/json.json'))
Lines = []
APKnums = []


for i in data:
    s = i['download_cnt'].rstrip('+')
    s2 = s.replace('万','0K')
    s2 = s2.replace('亿','00M')
    s = s.replace('万','0000')
    s = s.replace('亿','00000000')
    if len(s) > 1 and i['download'][34:-4] not in APKnums:
        if int(s) > 30000000 or '浏览器' in i['cat']:
            if exists('/home/jedi/tmp/anzhitarredandfeathered/strsonly/' + i['download'][34:-4] + '.apk.tgz.txt'):
                bla = i['name'] + ' (' + s2 + ', ' + i['cat'] + ')'
                print(bla)
                Lines.append(bla)
                APKnums.append(i['download'][34:-4]) 

Lines.append('Oppo Browser (built-in)')
APKnums.append('0000001')
Lines.append('Redmi(Xiaomi) Browser (built-in)')
APKnums.append('0000002')
Lines.append('Vivo Browser (built-in)')
APKnums.append('0000003')
Lines.append('Dungkar (Tibetan lang app)')
APKnums.append('0000004')
Lines.append('Dungkar IME (Tibetan lang app)')
APKnums.append('0000005')
Lines.append('Yongzin (Tibetan lang app)')
APKnums.append('0000006')

X = np.random.rand(len(Lines), len(Lines))

def docomparison(i, j, s, t):
    if i == j:
        return [i, j, 1.0]
    elif i > j:
        answer = comparethem(s, t)
        return [i, j, answer]
    else:
        return [i, j, -1.0]

mythreads = []
with concurrent.futures.ThreadPoolExecutor(max_workers = 8) as executor:
    for i in range(len(Lines)):
        for j in range(len(Lines)):
            mythreads.append(executor.submit(docomparison, i, j, APKnums[i], APKnums[j]))

    for future in concurrent.futures.as_completed(mythreads):
        print('Thread ' + str(future) + ' is done.')
        thelist = future.result()
        if thelist[2] > 0.0:
            X[thelist[0], thelist[1]] = thelist[2] 
            X[thelist[1], thelist[0]] = thelist[2] 
            

print(X)
fig = ff.create_dendrogram(X, orientation='left', labels=Lines)
fig.update_layout(width=1600, height=1200)
fig.show()

