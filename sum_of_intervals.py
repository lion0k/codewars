def sum_of_intervals(intervals):
    if not intervals:
        return 0

    temp = []
    fin = []
    out = 0
    for new in intervals:
        if temp:
            for exist in temp:
                if (new[0] <= exist[0] <= new[1]) or (new[0] <= exist[1] <= new[1]):
                    if (new[0] < exist[0] and new[1] < exist[1]) or (new[0] <= exist[0] and new[1] < exist[1]):
                        fin.append([new[0], exist[1]])
                    elif (new[0] > exist[0] and new[1] > exist[1]) or (new[0] >= exist[0] and new[1] > exist[1]):
                        fin.append([exist[0], new[1]])
                elif (new[0] < exist[0] and new[1] > exist[1]) or exist[0] < new[0] and exist[1] < new[1]:
                    fin.append([new[0], new[1]])
            temp = fin.copy()
        else:
            temp.append(new)
            fin.append(new)

    print('temp - ', temp)
    print('fin - ', fin)


t0 = [(1, 5), (6, 10)]
t1 = [(1, 5), (2, 5)]
t2 = [(1, 4), (7, 10), (3, 5)]

sum_of_intervals(t2)
