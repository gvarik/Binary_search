''''В первой строке даны целое число 1≤n≤105 и массив A[1…n] из n различных натуральных чисел, не превышающих 109, в порядке возрастания, во второй — целое число 1≤k≤105 и k натуральных чисел b1,…,bk, не превышающих 109.
Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=bi, или −1, если такого j нет.'''

import sys


def find_pos(xs,query):
    lo,hi=0,len(xs)
    while lo<hi:
        mid=(lo+hi)//2
        if query<xs[mid]:
            hi=mid
        elif query>xs[mid]:
            lo=mid+1
        else:
            return mid+1
    return -1


def main():
    reader=(map(int,line.split()) for line in sys.stdin)
    n,*xs=next(reader)
    k,*queries=next(reader)
    for query in queries:
        print(find_pos(xs,query),end=' ')



main()
