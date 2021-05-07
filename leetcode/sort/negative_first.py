# 给定一个序列，要求所有复数排在正数前面，而且按照原来顺序，要求时间复杂度为O(n), 空间复杂度为O(1)

def negative_first(array):
    i = j = 0
    while j < len(array):
        if array[j] < 0:
            tj = j
            for x in range(j-1, i-1, -1):
                array[x], array[tj] = array[tj], array[x]
                tj -= 1
            i += 1
        j += 1
    return array


a = [0,0,0,0,0,0,0,-1, -2, 3, 4, -5, 6, 10, -11, -5]

print(negative_first(a))