f = open("cleanupV2.csv", "r")
count = 0
for lll in f:
    # print len(line)
    spl = lll.split(',')
    cnt = len(spl)
    llll = ''
    i = 0
    while i < cnt-1:
        llll = llll + spl[i]+','
        i = i+1
    line = spl[-1]
    if count==0:
        print llll+line[:-1]
        count =1
        continue
    if len(line) == 6:
        print llll+line[:-1]
        continue
    if len(line) == 48:
        print llll+'"'+line[6:16]+'"'
    elif len(line) == 40:
        print llll+'"'+line[1:11]+'"'
    else:
        if line.count('/') == 0:
            print llll+'"'+line[4:14]+'"'
        else:
            splits = line.split('/')
            year = int(splits[2].split('"')[0])
            month = int(splits[1])
            day = int(splits[0].split('"')[-1])
            if month > 12:
                temp = month
                month = day
                day = temp
            days = str(day)
            months = str(month)
            years = str(year)
            if len(days) == 1:
                days = '0'+days
            if len(months)==1:
                months = '0'+months
            print llll+'"'+years+'-'+months+'-'+days+'"'
