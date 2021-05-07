

def merge(f, r):
    if not (f and r):
        return f or r
    res = []
    i = j = 0
    while i < len(f) and j < len(r):
        if f[i] > r[j]:
            res.append(r[j])
            j += 1
        else:
            res.append(f[i])
            i += 1
    
    if i<len(f):
        res.extend(f[i:len(f)])
    if j<len(r):
        res.extend(r[j:len(r)])
    return res




def merge_sort(data_list, start, end):
    if start+1 >= end:
        return data_list[start:end]
    
    mid = int((start + end)/2)
    
    f = merge_sort(data_list, start, mid)
    r = merge_sort(data_list, mid, end)

    return merge(f, r)



a = [2, 1]
b = merge_sort(a, 0, len(a))
print(b)
