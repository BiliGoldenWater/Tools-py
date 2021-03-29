keys_calc = {"-1": 'z',
             "-2": 'x',
             "-3": 'c',
             "-4": 'v',
             "-5": 'b',
             "-6": 'n',
             "-7": 'm',
             "1": 'a',
             "2": 's',
             "3": 'd',
             "4": 'f',
             "5": 'g',
             "6": 'h',
             "7": 'j',
             "8": 'q',
             "9": 'w',
             "+": 'e',
             '-': 'r',
             '*': 't',
             '/': 'y',
             '=': 'u'}

with open("temp", mode="r", encoding="utf-8") as f:
    data = f.read()
    for key in keys_calc:
        data = data.replace(key, keys_calc[key])
    with open("temp2", mode="w", encoding="utf-8") as fw:
        fw.write(data)
