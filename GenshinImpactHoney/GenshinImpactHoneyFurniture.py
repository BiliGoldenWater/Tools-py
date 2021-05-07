import backoff as backoff
import requests
import aiohttp
import asyncio
import json

from bs4 import BeautifulSoup


@backoff.on_exception(backoff.expo, exception=aiohttp.client_exceptions.ClientOSError, max_tries=10)
@backoff.on_exception(backoff.expo, exception=aiohttp.client_exceptions.ServerDisconnectedError, max_tries=10)
async def get_data(id, root_url_p, url_p):
    async with aiohttp.ClientSession() as session:
        async with session.get(root_url_p + url_p) as response:
            result_ = await response.read()

    print(url_p)

    soup_ = BeautifulSoup(result_.decode("utf-8"), "lxml")
    name = soup_.select("#content-main > div:nth-child(3) > div > div > div > div.custom_title")
    type_ = soup_.select("#content-main > div:nth-child(3) > div > div > div > table.item_main_table > "
                         "tr:nth-child(1) > td:nth-child(3) > a")
    rarity = len(soup_.select("#content-main > div:nth-child(3) > div > div > div > table.item_main_table > "
                              "tr:nth-child(2) > td:nth-child(2) > div"))
    adeptal_energy = soup_.select("#content-main > div:nth-child(3) > div > div > div > table.item_main_table > "
                                  "tr:nth-child(3) > td:nth-child(2)")
    load = soup_.select("#content-main > div:nth-child(3) > div > div > div > table.item_main_table > "
                        "tr:nth-child(4) > td:nth-child(2)")
    trust = soup_.select("#content-main > div:nth-child(3) > div > div > div > table.item_main_table > "
                         "tr:nth-child(5) > td:nth-child(2)")
    description = soup_.select("#content-main > div:nth-child(3) > div > div > div > table.item_main_table > "
                               "tr:nth-child(6) > td:nth-child(2) > div")
    recipe_title = soup_.select("#content-main > div:nth-child(3) > div > div > div > span")
    recipe = soup_.select("#content-main > div:nth-child(3) > div > div > div > table:nth-child(5) > tr > td")
    if len(recipe_title) == 0:
        recipe = []
    else:
        if recipe_title[0].get_text() != " Obtained from recipe ":
            recipe = []

    type_ = type_[0].get_text() if len(type_) > 0 else ""
    type_ = type_.split(" ")
    type_ = type_[len(type_) - 1] if len(type_) > 0 else ""

    recipe_processed = recipe[0].get_text() if len(recipe) > 0 else ""
    recipe_processed = recipe_processed.replace(" ", "")
    recipe_item_list = recipe_processed.split("+")
    recipe_final = {}
    for item in recipe_item_list:
        item_info = item.split("x")
        item_time = item.split(":")

        if len(item_info) > 1:
            if not isinstance(recipe_final.get("items"), list):
                recipe_final["items"] = []
            recipe_final["items"].append({
                "name": item_info[0],
                "count": int(item_info[1])
            })
        elif len(item_time) > 1:
            hours = int(item_time[0])
            minutes = int(item_time[1])
            seconds = int(item_time[2])

            recipe_final["time"] = (hours * 60 * 60) + (minutes * 60) + seconds
        else:
            recipe_final["other"] = item

    data_final = {"id": id,
                  "url": url_p,
                  "name": name[0].get_text(),
                  "type": type_,
                  "rarity": rarity,
                  "adeptal_energy": adeptal_energy[0].get_text(),
                  "load": load[0].get_text(),
                  "trust": trust[0].get_text(),
                  "description": description[0].get_text("\\n"),
                  "recipe": recipe_final}
    print(data_final)

    return data_final


loop = asyncio.get_event_loop()
if __name__ == "__main__":
    root_url = "https://genshin.honeyhunterworld.com"
    target_url = root_url + "/db/item/furniture-list/?lang=CHS"

    result = requests.get(url=target_url)
    soup = BeautifulSoup(result.text, "lxml")

    data_list = soup.select("#content-main > div:nth-child(3) > div > div > div > div.items_wrap > a")
    data_len = len(data_list)

    furniture_list = []
    tasks = []

    print("Count:", data_len)

    for i in range(data_len):
        data = data_list[i]
        url = data.get("href")

        if url.startswith("/db/item/hs"):
            continue

        task = asyncio.ensure_future(get_data(i + 1, root_url, url))
        tasks.append(task)

    furniture_list = loop.run_until_complete(asyncio.gather(*tasks))

    with open("furniture-list.json", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(furniture_list, indent=2).encode("utf-8").decode("unicode-escape"))
