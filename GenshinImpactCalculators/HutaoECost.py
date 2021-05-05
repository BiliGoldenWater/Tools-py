ipt = 100
percentPerTime = 0.3
times = 0

while True:
    print("{} {}".format(str(times).zfill(2), ipt))

    if ipt + 0.1 < 1:
        break

    ipt -= ipt * percentPerTime
    times += 1
