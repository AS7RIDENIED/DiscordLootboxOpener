import httpx, time

url = "https://discord.com/api/v9/users/@me/lootboxes/open"
authorization = input("Введи authorization из хидеров запроса:\n> ")
super_properities = input("Введи x-super-properities из хидеров запроса:\n> ")
headers = {
    "authorization": authorization,
    "x-super-properties": super_properities,
}
cd = 4.45
while True:
    response = httpx.post(
        url=url,
        headers=headers,
    )
    if response.status_code != 200:
        print("Случилась какая-то ебанина, запрос не прошел")
        time.sleep(cd)
    elif response.status_code == 200:
        try:
            opened = "xxx"
            lootbox_data = response.json().get("user_lootbox_data")
            if lootbox_data:
                opened_items = lootbox_data.get("opened_items")
                if opened_items:
                    opened = sum(opened_items.values())
            print(f"{response} | Opened -> {opened}")
        except Exception as e:
            print(
                f"{response} | {e} | В запросе вернуло какую-то ебанину, но лутбокс открылся\n{response.text}"
            )
    time.sleep(cd)
