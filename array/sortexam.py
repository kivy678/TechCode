# -*- coding:utf-8 -*-

#################################################################
import bisect

####################### 배열 이진 분할 알고리즘 #####################
# 정렬된 리스트를 삽입 후에 다시 정렬할 필요 없도록 관리할 수 있도록 지원

sample_list = [1, 2, 3, 5]
print(bisect.bisect(sample_list, 2))
# >>> 2

print(bisect.bisect_left(sample_list, 2))
# >>> 1

bisect.insort(sample_list, 4)
print(sample_list)
# >>> [1, 2, 3, 4, 5]


#################################################################

print('Done...')
