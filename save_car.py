import json
import tkinter.messagebox as mb

class SaveCar:
    def __init__(self, parent):
        self.parent = parent
        self.create_json()
    
    def create_json(self):
        uid = self.parent.uid_label.cget("text").upper()
        manufacturer = self.parent.manufacturer_entry.get().upper()
        model =self.parent.model_entry.get().upper()
        year = self.parent.year_entry.get()
        country = self.parent.country_entry.get().upper()
        price = self.parent.price_entry.get()

        car_dict = {'uid': uid, 'manufacturer': manufacturer, 'model': model, 'year': year, 'country': country, 'price': price}

        if car_dict['uid'] == 'UID не получен':
            mb.showerror("Ошибка", "Сначала получите UID")
            return
        
        if not(car_dict["manufacturer"] and car_dict["model"] and car_dict["year"]):
            mb.showerror("Ошибка", "Заполните все обязательные поля!")
            return
        
        try:
            with open('cars_data.json', "r", encoding='utf-8') as file:
                cars = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            cars = []
        
        cars.append(car_dict)

        with open("cars_data.json", "w", encoding="utf-8") as file:
            json.dump(cars, file, ensure_ascii=False, indent=4)  
        
        mb.showinfo("Успех", "Автомобиль успешно сохранен!")
        self.parent.window.destroy()  # Закрываем окно добавления
