
def partition(data_list, start, end):
    i = j = 0
    q = data_list[end-1]
    while j < end-1:
        if data_list[j] < q:
            data_list[i], data_list[j] = data_list[j], data_list[i]
            i += 1
        j += 1
    data_list[i], data_list[end-1] = data_list[end-1], data_list[i]
    return i
    

def quick_sort(data_list, start, end):
    if start + 1 >= end:
        return 
    q = partition(data_list, start, end)

    quick_sort(data_list, start, q)
    quick_sort(data_list, q+1, end)


a = [1,4,2,8,11,23,12,4,6,3]

quick_sort(a, 0, len(a))

print(a)