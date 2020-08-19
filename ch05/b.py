def merge_sort(aList):
    if len(aList) <= 1:
        print('aaaa')
        return aList
    
    print('aList: ',end = "")
    print(*aList)

    mid = len(aList) // 2
    left = aList[:mid]
    right = aList[mid:]

    print('mid: ',end = "")
    print(mid)

    left = merge_sort(left)
    print('left: ',end = "")
    print(*left)

    right = merge_sort(right)
    print('right: ',end = "")
    print(*right)

    return list(merge(left, right))


def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    if left:
        sorted_list.extend(left[left_index:])
    if right:
        sorted_list.extend(right[right_index:])
    print('sorted: ',end = "")
    print(*sorted_list)
    return sorted_list


n = int(input())
a = list(map(int,input().split()))

print(merge_sort(a))
