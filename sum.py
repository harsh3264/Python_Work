a = []
b = []
count = 0
x = int(raw_input("Enter the length of lists :"))
for i in range(x):
    k = int(raw_input("Enter the list 1 digit {}:".format(i+1)))
    a.append(k)
for j in range(x):
    m = int(raw_input("Enter the list 2 digit {}:".format(j+1)))
    b.append(m)
c = a + b
c.sort()
for i in range(len(c)/2):
       count += c[i]
print count