x, y = [int(i) for i in '4 4'.split()]
res = [[0] * x] * y
m = [['.'] * x]
for i in range(y):
    m.append(['.'] + [i for i in input()] + ['.'])
m.append(['.'] * x)
print(m)



# ..*.
# **..
# ..*.
# ....







