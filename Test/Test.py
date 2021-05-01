import time

ipt = 99999999

result = 0

time_start = time.time_ns()

for x in range(1, ipt + 1):
    t = 1
    if ipt % x == 0:
        if x % 2 == 1:
            result += 1
            # print(x)
            t += 1

time_end = time.time_ns()

time_cost = time_end - time_start
time_cost_ms = time_cost / 1000 / 1000

print("result: {}, time cost(ms):{:.0f}".format(result, time_cost_ms))
