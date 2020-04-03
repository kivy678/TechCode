# -*- coding:utf-8 -*-

import csv

with open(r'set\test.csv', 'w') as fw:
    cw = csv.writer(fw, delimiter=',', lineterminator='\n')
    cw.writerow([1, 2, 3])
    cw.writerow(['a', 'b', 'c'])


with open(r'set\test.csv', 'r') as fr:
    cr = csv.reader(fr, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)

    for row in cr:
        print(row)


print('done...')
