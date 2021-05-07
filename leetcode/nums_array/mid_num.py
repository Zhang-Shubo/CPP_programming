
def findMedianSortedArrays(nums1, nums2) -> float:
    len1 = len(nums1)
    len2 = len(nums2)
    mid = (len1 + len2)//2
    mod = (len1 + len2) % 2
    if len1+len2 <=2:
        nums1.extend(nums2)
        return sum(nums1)/(len1+len2)*1.0
    i = 0
    j = k = 0
    current_num = 0
    mid_num = 0
    mid_num2 = 0
    while j < len1 or k < len2:
        if i == mid+1 and mod == 1:
            mid_num2 = mid_num = current_num
            break
        elif i == mid and mod == 0:
            mid_num = current_num
        elif i == mid+1 and mod == 0:
            mid_num2 = current_num
            break
            
        if j < len1 and k < len2:
            if nums1[j] < nums2[k]:
                current_num = nums1[j]
                j += 1
            else:
                current_num = nums2[k]
                k += 1
        elif j < len1:
            current_num = nums1[j]
            j += 1
        elif k < len2:
            current_num = nums2[k]
            k += 1
        i +=1

    return (mid_num+mid_num2)/2.0


def findMedianSortedArrays2(nums1, nums2) -> float:
    len1 = len(nums1)
    len2 = len(nums2)
    mid1 = (len1 + len2 + 1)//2
    mid2 = (len1 + len2 + 2)//2

    return (find_kth(nums1, 0, len1, nums2, 0, len2, mid1) + find_kth(nums1, 0, len1, nums2, 0, len2, mid2))/2.0
def find_kth(nums1, begin1, end1, nums2, begin2, end2, k):

    if k == 1:
        if nums1[begin1:end1] and nums2[begin2:end2]:
            if nums1[begin1] < nums2[begin2]:
                return nums1[begin1]
            else:
                return nums2[begin2]
        elif nums1[begin1:end1]:
            return nums1[begin1]
        elif nums2[begin2:end2]:
            return nums2[begin2]
    else:
        if not nums1[begin1:end1]:
            return nums2[begin2+k-1]
        elif not nums2[begin2:end2]:
            return nums1[begin1+k-1]
    new_b1 = begin1 + k//2 -1 if begin1 + k//2 -1 < end1 else end1 - 1
    new_b2 = begin2 + k//2 -1 if begin2 + k//2 -1 < end2 else end2 - 1
    
    if nums1[new_b1] < nums2[new_b2]:
        return find_kth(nums1, new_b1+1, end1, nums2, begin2, end2, k - new_b1 + begin1-1)
    else:
        return find_kth(nums1, begin1, end1, nums2, new_b2+1, end2, k - new_b2 + begin2-1)

l1 = [1,3]
l2 = [2,7]
# a = find_kth(l1, 0, len(l1), l2, 0, len(l2), 2)


a = findMedianSortedArrays2(l1, l2)
print(a)