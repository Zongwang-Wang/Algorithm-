def inversion(num_list):
    if len(num_list) == 1:
        return num_list, 0
    else:
        n = len(num_list) // 2
        left, left_count = inversion(num_list[:n])
        right, right_count = inversion(num_list[n:])
        merged, merged_count = merge_count(left, right)
        return merged, left_count + right_count + merged_count


def merge_count(left, right):
    merged = []
    i = j = 0
    count = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left[i:])
            j += 1

    merged += left[i:]
    merged += right[j:]

    return merged, count

with open('data.txt', 'r') as f:
    data_array = [int(line.strip()) for line in f]
print(inversion(data_array))
