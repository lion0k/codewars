def revrot(s, n):
    if not s or n == 0 or n > len(s):
        return ''

    output = ''
    for i in range(len(s) // n):
        x = s[i * n:n * i + n]
        div_2 = sum([int(i) ** 3 for i in x]) % 2 == 0
        output += x[::-1] if div_2 else x[1:] + x[:1]

    return output


print(revrot("8278828727", 4))