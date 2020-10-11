import hashlib

ipt = "aa"

mid = hashlib.sha256(ipt.encode()).hexdigest()

i = 0

while True:
    if bytes.fromhex(mid) <= bytes.fromhex("000000e1143d100d05e787053bfde5dc148e494d94b79e5b0d1d7d3e91ca9121"):
        print(mid)
        print(i+1)
        break
    mid = hashlib.sha256(mid.encode()).hexdigest()
    i += 1
