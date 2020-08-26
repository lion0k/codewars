def move_zeros(array):
    out = [0 for i in range(len(array))]
    cnt = 0
    for i in array:
        if i != 0:
            out[cnt] = bool(i) if isinstance(i, bool) else i
            #
            # else:
            #     out[cnt] = i
            cnt += 1
    return out


print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
