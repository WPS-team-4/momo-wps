maps = [2, 3, 6, 4, 88, 4, 7, 5, 5, 8, 2, 10, 45, 98, 0, 53, 33, 21, 13]
len = len(maps)
low = []
high = []
same = []
print(maps)
print(len)

copy_maps = maps.copy()


pivot = maps[len // 2]
print(pivot)
maps[len // 2], maps[len - 1] = maps[len - 1], maps[len // 2]
print(maps)
print(pivot)

print('pick pivot:{}'.format(pivot))
for index, map in enumerate(maps):
    # map = copy_maps.pop(index)
    print('maps에서 {}번째 map:{}을 선택'.format(index, map))
    if pivot < map:
        print('map{}을 high에 추가 // 현재 maps: {}'.format(map, maps))
        high.append(map)
        print('현재 high값:{}'.format(high))

    elif pivot > map:
        # print('maps에서 {}번째 map{}을 선택'.format(index, map))
        # map_in = copy_maps.pop(index)
        print('map{}을 low에 추가 // 현재 maps: {}'.format(map, maps))
        low.append(map)
        print('현재 low값:{}'.format(low))
    elif pivot == map:
        print('map{}을 same에 추가 // 현재 maps: {}'.format(map, maps))
        same.append(map)

    print('최종 low:{} // 최종 same:{} // 최종 high:{}'.format(low, same, high))


maps = low.append(same).append(high)
# maps.append(pivot)
# maps.append(high)
print(maps)
print(len(maps))
    # low.append(pivot)
