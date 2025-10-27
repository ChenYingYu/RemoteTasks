import urllib.request as request
import json
import csv

# parse data from URLs
ch_url = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
en_url = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"

with request.urlopen(ch_url) as response:
    ch_data = json.load(response)

with request.urlopen(en_url) as response:
    en_data = json.load(response)

ch_hotel_list = ch_data["list"]
en_hotel_list = en_data["list"]

# Merge English names and addresses into Chinese data
merged_hotel_list = []
id_look_up = {hotel["_id"]: hotel for hotel in ch_hotel_list}
for hotel in en_hotel_list:
    id = hotel["_id"]
    if id in id_look_up:
        merged_hotel = {**id_look_up[id], **hotel}
        merged_hotel_list.append(merged_hotel)

# Output one hotel information per line into hotels.csv
with open("hotels.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for hotel in merged_hotel_list:
        # ChineseName,EnglishName,ChineseAddress,EnglishAddress,Phone,RoomCount
        ch_name = hotel.get("旅宿名稱", "N/A")
        en_name = hotel.get("hotel name", "N/A")
        ch_address = hotel.get("地址", "N/A")
        en_address = hotel.get("address", "N/A")
        phone = hotel.get("電話或手機號碼", "N/A")
        room_count = hotel.get("房間數", "N/A")

        writer.writerow([ch_name, en_name, ch_address, en_address, phone, room_count])


# Group hotels by district.
districts = {
    "中正區": {"hotel_count": 0, "room_count": 0},
    "萬華區": {"hotel_count": 0, "room_count": 0},
    "中山區": {"hotel_count": 0, "room_count": 0},
    "大同區": {"hotel_count": 0, "room_count": 0},
    "文山區": {"hotel_count": 0, "room_count": 0},
    "大安區": {"hotel_count": 0, "room_count": 0},
    "松山區": {"hotel_count": 0, "room_count": 0},
    "信義區": {"hotel_count": 0, "room_count": 0},
    "士林區": {"hotel_count": 0, "room_count": 0},
    "北投區": {"hotel_count": 0, "room_count": 0},
    "南港區": {"hotel_count": 0, "room_count": 0},
    "內湖區": {"hotel_count": 0, "room_count": 0},
}


for hotel in merged_hotel_list:
    for district, value in districts.items():
        if district in hotel["地址"]:
            hotel_count = int(districts[district].get("hotel_count", 0)) + 1
            room_count = int(districts[district].get("room_count", 0)) + int(
                hotel.get("房間數", 0)
            )

            districts[district] = {"hotel_count": hotel_count, "room_count": room_count}

# Output how many hotels and rooms are there for each district into districts.csv .
with open("districts.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for district, value in districts.items():
        writer.writerow([district, value["hotel_count"], value["room_count"]])
