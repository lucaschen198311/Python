def minCoinChange(num):
    change = {}
    if num//25>0:
        change["quater"] = num//25
        num = num%25
    else:
        change["quater"] = 0
    if num//10>0:
        change["dime"] = num//10
        num = num%10
    else:
        change["dime"] = 0
    if num//5>0:
        change["nickle"] = num//5
        num = num%5
    else:
        change["nickle"] = 0
    change["penny"] = num
    return change

print(minCoinChange(321))