import json


def sort_cmp(a, b):
    return a["rarity"] > b["rarity"]


def sort_key(key):
    return key["adeptal_energy"]


def sort_key_(key):
    return int(key["load"])


if __name__ == "__main__":
    with open("furniture-list.json", mode="r", encoding="utf-8") as f:
        data_str = f.read()
        data_json = json.loads(data_str)
        data_json.sort(key=sort_key, reverse=True)
        max_adeptal_energy = []
        for x in data_json:
            if x["adeptal_energy"] == "90":
                max_adeptal_energy.append(x)

        max_adeptal_energy.sort(key=sort_key_)

        for x in max_adeptal_energy:
            print("{} {} {} {} {}".format(x["name"], x["type"], x["adeptal_energy"], x["load"], x["recipe"]))
