def sort_cmp(a, cmp):
    n = len(a)
    if n <= 1:
        return a

    mid = n // 2
    left = sort_cmp(a[:mid], cmp)
    right = sort_cmp(a[mid:], cmp)

    ret = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if cmp(left[i], right[j]) <= 0:
            ret.append(left[i])
            i += 1
        else:
            ret.append(right[j])
            j += 1

    while i < len(left):
        ret.append(left[i])
        i += 1

    while j < len(right):
        ret.append(right[j])
        j += 1

    return ret
