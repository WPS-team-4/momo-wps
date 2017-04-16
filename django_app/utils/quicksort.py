maps = [2, 3, 6, 4, 88, 4, 7, 5, 5, 8, 2, 10, 45, 98, 0, 53, 33, 21, 13]
len = len(maps)
low = []
high = []
print(maps)
print(len)
for index, map in enumerate(maps):
    pivot = maps.pop(len // 2)
    print('pick pivot:{}'.format(pivot))
    copy_maps = maps.copy()
    map = copy_maps.pop(index)
    print('maps에서 {}번째 map:{}을 선택'.format(index, map))
    if pivot < map:
        print('map{}을 high에 추가 // 현재 copy_maps: {}'.format(map, copy_maps))
        high.append(map)
        print('현재 high값:{}'.format(high))

    elif pivot >= map:
        # print('maps에서 {}번째 map{}을 선택'.format(index, map))
        # map_in = copy_maps.pop(index)
        print('map{}을 low에 추가 // 현재 copy_maps: {}'.format(map, copy_maps))
        low.append(map)
        print('현재 low값:{}'.format(low))

    print('최종 low:{} // 최종 high:{}'.format(low,high))
    low.append(high)
# low.append(pivot)
