def sum_of_intervals(intervals):
    def find_and_change(source, before, after):
        for i in range(len(source)):
            if source[i] == before:
                source[i] = after
                break

    if not intervals:
        return 0

    fin = []
    intervals.sort()
    for new in intervals:
        if fin:
            exist = fin[-1]

            if (new[0] <= exist[0] <= new[1]) or (new[0] <= exist[1] <= new[1]):
                if (new[0] < exist[0] and new[1] < exist[1]) or (new[0] <= exist[0] and new[1] < exist[1]):
                    find_and_change(fin, exist, [new[0], exist[1]])
                elif (new[0] > exist[0] and new[1] > exist[1]) or (new[0] >= exist[0] and new[1] > exist[1]):
                    find_and_change(fin, exist, [exist[0], new[1]])
            elif new[0] >= exist[0] and new[1] <= exist[1]:
                continue
            elif new[0] < exist[0] and new[1] > exist[1]:
                find_and_change(fin, exist, [new[0], new[1]])
            elif new[0] > exist[0] and new[1] > exist[1]:
                fin.append([new[0], new[1]])
        else:
            fin.append(new)

    return sum([i[1] - i[0] for i in fin])
