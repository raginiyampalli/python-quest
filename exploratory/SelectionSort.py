def selection_sort(values):
    i = 0
    while i < len(values):
        min_value = values[i]
        min_position = i
        j = i + 1
        while j < len(values):
            if min_value > values[j]:
                min_value = values[j]
                min_position = j
            j += 1
        temp = values[i]
        values[i] = values[min_position]
        values[min_position] = temp
        i += 1

    for v in values:
        print(v)


selection_sort([3, 7, 100, 4, 6, 11])
