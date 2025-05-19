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
        photo_path = getattr(self.parent, 'photo_path', '')

        car_dict = {'uid': uid, 
                    'manufacturer': manufacturer, 
                    'model': model, 
                    'year': year, 
                    'country': country, 
                    'price': price, 
                    'photo': photo_path
                    }

        try:
            with open('cars_data.json', "r", encoding='utf-8') as file:
                cars = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            cars = []

        uid_list = []
        for car in cars:
            uid_list.append(car['uid'])
            

        if car_dict['uid'] == 'UID не получен':
            mb.showerror("Ошибка", "Сначала получите UID")
            return
        
        if car_dict['uid'] in uid_list:
            mb.showerror('Ошибка', 'UID уже зарегистрирован')
            return
        
        if not(car_dict["manufacturer"] and car_dict["model"] and car_dict["year"]):
            mb.showerror("Ошибка", "Заполните все обязательные поля!")
            return
        
        
        cars.append(car_dict)

        with open("cars_data.json", "w", encoding="utf-8") as file:
            json.dump(cars, file, ensure_ascii=False, indent=4)  
        
        mb.showinfo("Успех", "Автомобиль успешно сохранен!")
        self.parent.window.destroy()  # Закрываем окно добавления
        self.parent.car_system.update_cards()

