from scrape import scrape
import csv
import time
from datetime import datetime

class skins:
    def __init__(self, type_accessory, name, id, last_sold, price_min, price_max, sale_order):
        self.type_accessory = type_accessory
        self.name = name
        self.id = id
        self.last_sold = last_sold
        self.price_min = price_min
        self.price_max = price_max
        self.sale_order = sale_order
        
    def __str__(self):
        return f"{self.type_accessory} - {self.name} | Last Sold: {self.last_sold} | Price Range: {self.price_min} - {self.price_max} | Sale Order: {self.sale_order}"
        
class type_category:
    def __init__(self, name):
        self.name = name
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        print(f"\nItems in Category '{self.name}':")
        for item in self.items:
            print(item)
            
class managerClass:
    def __init__(self, name):
        self.name = name
        self.id = id
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        print(f"\nItems in Category '{self.name}':")
        for item in self.items:
            item_details = scrape(item.id)
            item.last_sold = item_details[0]
            item.price_min = item_details[1]
            item.price_max = item_details[2]
            item.sale_order = item_details[3]
            write_to_csv(item.type_accessory ,item.name, item.last_sold, 'data.csv')
            print(item)


class ItemManager:
    def __init__(self):
        self.categories = {}

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories[category_name] = managerClass(category_name)

    def add_item_to_category(self, category_name, item):
        if category_name in self.categories:
            self.categories[category_name].add_item(item)
        else:
            print(f"Category '{category_name}' does not exist.")

    def display_items_by_category(self, category_name):
        if category_name in self.categories:
            self.categories[category_name].display_items()
        else:
            print(f"Category '{category_name}' does not exist.")

# Function to write data to CSV file
def write_to_csv(acessory, name, last_sold, csv_filename):
    pretty_name = acessory + ' - ' + name
    with open(csv_filename, 'a', newline='') as csvfile:
        fieldnames = ["Timestamp", "Gun", "Last Sold"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header only if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write data to CSV with timestamp
        writer.writerow({"Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Gun": pretty_name[5:], "Last Sold":last_sold})

# Example usage:

# Creating an ItemManager instance
item_manager = ItemManager()

# Adding categories to the ItemManager
item_manager.add_category("2018")
item_manager.add_category("2019")
item_manager.add_category("PL")
item_manager.add_category("Glacier")

#2019 GUN
# w1 = [
#     skins("GUN: R4C", "FaZeClan2019", '27e67988-af83-4d24-8467-afa2521e11cd', 0, 0, 0, 0),
#     skins("GUN: SMG-11", "G2 Esports 2019", '0a8b0eaa-c4a3-444a-b40c-c4a3f3315024', 0, 0, 0, 0),
#     skins("GUN: 416-C CARBINE", "Rogue 2019", 'fb00cd0c-0983-4683-b93d-4f5d6e5ab295', 0, 0, 0, 0),
#     skins("GUN: K1A", "TeamLiquid2019", '0c67ed36-1980-480b-9594-5b08096cde71', 0, 0, 0, 0),
#     skins("GUN: R4-C", "Evil Geniuses 2019", '9b699a3b-af83-4f88-a137-a0d3984eab17', 0, 0, 0, 0)
# ]
    
w2 = [
    skins("GUN: C8-SFW", "GLACIER", '52456808-84f5-4ac7-80c8-0b07f4200b7d', 0, 0, 0, 0),
    skins("GUN: 416-C", "GLACIER", '550af976-1315-434a-b2fa-5137a4dde7bd', 0, 0, 0, 0),
    skins("GUN: G36C", "GLACIER", 'c780a450-8ac5-473b-8d2f-b7aac243e9f2', 0, 0, 0, 0),
    skins("GUN: 556XI", "GLACIER", 'da8bad72-043a-4014-97d6-d8b99628a43e', 0, 0, 0, 0),
    skins("GUN: R4-C", "GLACIER", 'f619eb19-de6e-4dcd-96eb-08b45f80fe64', 0, 0, 0, 0),
    skins("GUN: 6P41", "GLACIER", '6bb292f8-66c2-4f17-825d-d0c8d740ce84', 0, 0, 0, 0),
    skins("GUN: M590A1", "GLACIER", '2f4918b3-cd1e-4a3c-b08e-27b300b0e3c1', 0, 0, 0, 0),
    skins("GUN: 5.7 USG", "GLACIER", '3b259c5a-8f1f-4cc8-9c51-befc5693bb25', 0, 0, 0, 0),
    skins("GUN: GSH-18", "GLACIER", '7537e8ba-987b-45b1-80ce-890d1d2c0f56', 0, 0, 0, 0),
    skins("GUN: MP5", "GLACIER", 'bfc657e7-5168-4da5-bebb-b0c8c1e2f889', 0, 0, 0, 0),
    skins("GUN: M870", "GLACIER", '26b6de59-e112-4198-a681-92a55962e653', 0, 0, 0, 0),
    skins("GUN: L85A2", "GLACIER", 'c7dc7bfd-4e61-440d-9232-ca087580024e', 0, 0, 0, 0),
    skins("GUN: P9", "GLACIER", '06797959-3dd8-4c3a-95af-f6193318edf3', 0, 0, 0, 0),
    skins("GUN: F2", "GLACIER", '47eb21ff-8ef6-489a-879e-c21bce34baa4', 0, 0, 0, 0),
    skins("GUN: SUPER 90", "GLACIER", '1929af4a-ca8f-40ba-ba8f-455c0c3ba7a0', 0, 0, 0, 0),
    skins("GUN: LFP586", "GLACIER", 'f44fda95-3f5c-4c6b-bf06-2cd3bc3e93af', 0, 0, 0, 0),
    skins("GUN: MP7", "GLACIER", '9c99e160-4396-4b3d-954d-12bd11e992dc', 0, 0, 0, 0),
    skins("GUN: P90", "GLACIER", 'd3b6fb36-a61f-44a0-b508-d54e08a91a2d', 0, 0, 0, 0),
    skins("GUN: 9x19VSN", "GLACIER", '19d12c03-fe32-4167-a4cf-5e034cdf0258', 0, 0, 0, 0),
    skins("GUN: 9mm C1", "GLACIER", '2a812cf0-93fa-4c84-9e87-673d164b6fdf', 0, 0, 0, 0),
    skins("GUN: P12", "GLACIER", '3fc7f216-bcef-4a6a-b5c1-e6deac714b17', 0, 0, 0, 0),
    skins("GUN: CAMRS", "GLACIER", '4bfb905e-b3f1-47fe-b7d1-0909bf94c5cb', 0, 0, 0, 0),
    skins("GUN: MP5K", "GLACIER", '7520880d-88bd-4ffd-8d96-4d9b8471f925', 0, 0, 0, 0),
    skins("GUN: 552 COMMANDO", "GLACIER", 'adb8a620-3321-44ff-9f60-d63d6bff2d9f', 0, 0, 0, 0),
    skins("GUN: AR33", "GLACIER", '4fc78237-6a9d-4c11-aaf3-170bf787d824', 0, 0, 0, 0),
    skins("GUN: OTs-03", "GLACIER", '7101568d-051b-4c82-a955-a4c0c72a39f1', 0, 0, 0, 0),
    skins("GUN: FMG-9", "GLACIER", '820cda34-3e45-4983-b7c7-e0d4cf7a3f2f', 0, 0, 0, 0),
    skins("GUN: AK-12", "GLACIER", '84925275-b76f-4da9-a361-b551d414fc27', 0, 0, 0, 0),
    skins("GUN: M45 MEUSOC", "GLACIER", '4e0bbd3f-b483-4941-be12-812af0e00715', 0, 0, 0, 0),
    skins("GUN: SMG-11", "GLACIER", '73512c14-2110-44be-9f56-eb7c48281dff', 0, 0, 0, 0),
    skins("GUN: MK1 9mm", "GLACIER", '2789482f-1345-48f2-8e2a-0b7ffba57c37', 0, 0, 0, 0),
    skins("GUN: M1014", "GLACIER", '74ea0bde-c802-4684-a5fd-b619ede00cd7', 0, 0, 0, 0),
    skins("GUN: AUG A2", "GLACIER", '9703e629-4907-481d-9a02-72088b1b3413', 0, 0, 0, 0),
    skins("GUN: SG-CQB", "GLACIER", '4940d7c6-8244-4020-b418-ea29070b0a23', 0, 0, 0, 0),
    skins("GUN: PMM", "GLACIER", '920e1e06-6094-4681-9323-e5b95875a966', 0, 0, 0, 0),
    skins("GUN: UMP45", "GLACIER", 'aa3781de-2bc5-45b7-8a59-1bebe4ef6d4b', 0, 0, 0, 0),
    skins("GUN: G8A1", "GLACIER", 'c580471d-2d0e-4857-a0dd-35886ef21cb9', 0, 0, 0, 0),
    skins("GUN: 417", "GLACIER", 'd68e56ad-668c-4c79-8643-1d6d8ba52fdf', 0, 0, 0, 0),
    skins("GUN: P226 MK 25", "GLACIER", '1146bd66-822e-498f-aa22-d7796ddf3e48', 0, 0, 0, 0),
    skins("GUN: SASG-12", "GLACIER", '3adf36cb-742b-4e84-9d2f-9bde911abfb6', 0, 0, 0, 0),
]


# for w_item in w1:
#     item_manager.add_item_to_category("2019", w_item)

for w_item in w2:
    item_manager.add_item_to_category("Glacier", w_item)
#y = input ("Y/N")
#if (y = 'y'):
#item_manager.display_items_by_category("2019")
while True:
    item_manager.display_items_by_category("Glacier")
    time.sleep(3600)