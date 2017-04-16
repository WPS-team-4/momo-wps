__all__ = (
    'quicksort',
)


def quicksort(list):
    if len(list) <= 1:
        return list

    low = []
    high = []
    same = []
    pivot = list[len(list) // 2]
    for val in list:
        if pivot < val:
            high.append(val)
        elif pivot > val:
            low.append(val)
        elif pivot == val:
            same.append(val)

    return quicksort(low) + same + quicksort(high)
