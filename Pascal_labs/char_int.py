s = 'у п у п у у п у п п у п п п у п'
a = s.split(' ')
b = []
for i in range(len(a)):
    if a[i] == 'у':
        b.append(2019)
    elif a[i] == 'п':
        b.append(2018)
    else:
        raise Exception('String has wrong format')
print(b)
