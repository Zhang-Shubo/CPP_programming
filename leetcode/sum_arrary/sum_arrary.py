# 给定一个集合，找出所有和为目标值的序列
dp = {}
def sum_arary(c, target):
    res = []
    if target <= 0:
        return 
    if target in c:
        res.append([target])
    

    for num in c:
        if target-num in dp:
            ararrys = dp[target-num]
        else:
            ararrys = sum_arary(c, target-num)
        if ararrys:
            for ar in ararrys:
                res.append([num] + ar)
    dp[target] = res
    return res


cc = [1, 2, 4, 6]

print(sum_arary(cc, 6))