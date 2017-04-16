def quicksort(list):
    if len(list) <= 1:
        return list

    low = []
    high = []
    same = []
    pivot = list[len(list) // 2]

    print('pick pivot:{}'.format(pivot))
    for val in list:
        print('list에서 {}을 선택'.format(val))
        if pivot < val:
            print('val{}을 high에 추가 // 현재 list: {}'.format(val, list))
            high.append(val)
            print('현재 high값:{}'.format(high))
        elif pivot > val:
            print('val{}을 low에 추가 // 현재 list: {}'.format(val, list))
            low.append(val)
            print('현재 low값:{}'.format(low))
        elif pivot == val:
            print('val{}을 same에 추가 // 현재 list: {}'.format(val, list))
            same.append(val)

        print('최종 low:{} // 최종 same:{} // 최종 high:{}'.format(low, same, high))
    return quicksort(low) + same + quicksort(high)
