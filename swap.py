def chars_min_up(a,b):
    new_a=b[:1]+a[1:]
    new_b=a[:1]+b[1:]
    return new_a+ new_b
print(chars_min_up('hello\t','world'))
