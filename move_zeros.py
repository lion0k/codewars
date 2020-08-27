def move_zeros(array):
    out = [0 for i in range(len(array))]
    cnt = 0
    for i in array:
        if isinstance(i, bool):
            out[cnt] = bool(i)
            cnt += 1
        else:
            if i != 0:
                out[cnt] = i
                cnt += 1
    return out
