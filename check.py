f = open("red.csv", "r")
count = 0
for x in f:
    # print len(line)
    spl = x.split(',')
    cnt = len(spl)
    y = ''
    i = 0
    while i < cnt-1:
        y = y + spl[i]+','
        i = i+1
    line = spl[-1]
    if count==0:
        print line[:-1]