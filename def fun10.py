li = [12, 35, 9, 56, 24]

def swapList(li):
    size = len(li)

    temp = li[0]
    li[0] = li[size-1]
    li[size-1] = temp

    return li

print(swapList(li))