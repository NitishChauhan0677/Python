a = [12,23,4,3443,3,2332,2323,2343,23, "Python Is Fun"]
print(a[6])
a.append(9)
print(a)
for i in a:
    print(i, end=" ")

a.remove(3443)
print(a)