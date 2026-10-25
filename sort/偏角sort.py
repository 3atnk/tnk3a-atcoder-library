def angle_sort(A):
    n = len(A)
    if n <= 1:
        return A

    def upper(x, y):
        # +x軸から反時計回りで前半180度
        return y > 0 or (y == 0 and x >= 0)

    buf = [None] * n
    width = 1

    while width < n:
        for l in range(0, n, width * 2):
            m = min(l + width, n)
            r = min(l + width * 2, n)

            i = l
            j = m
            k = l

            while i < m and j < r:
                ax, ay = A[i]
                bx, by = A[j]

                ha = upper(ax, ay)
                hb = upper(bx, by)

                if ha != hb:
                    take_left = ha
                else:
                    take_left = ax * by - ay * bx >= 0

                if take_left:
                    buf[k] = A[i]
                    i += 1
                else:
                    buf[k] = A[j]
                    j += 1
                k += 1

            while i < m:
                buf[k] = A[i]
                i += 1
                k += 1

            while j < r:
                buf[k] = A[j]
                j += 1
                k += 1

        A, buf = buf, A
        width *= 2

    return A
