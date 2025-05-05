import json


names = ["uid","manufacturer", "model", "year", "country", "price"]

uid = input("Input UID (draft): ") #later connect with uid_into_py 
manufacturer = input("Input car brand: ")
model = input("Input car model: ")
year = input("Input year of production: ")
country = input("Input producing country: ")
price = input("Input starting price: ")

car_dict = {'uid': uid, 'manufacturer': manufacturer, 'model': model, 'year': year, 'country': country, 'price': price}

with open("cars_data.json", "w", encoding="utf-8") as file:
    json.dump(car_dict, file, ensure_ascii=False, indent=4)    

