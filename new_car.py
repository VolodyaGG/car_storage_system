import tkinter as tk
from PIL import Image, ImageTk
from uid_into_py import record_uid
from random import randint
from save_car import SaveCar

class Add_New_Car:
    def __init__(self, parent):
        self.parent = parent
        self.uid_label = None
        self.manufacturer_entry = None
        self.model_entry = None
        self.year_entry = None
        self.country_entry = None
        self.price_entry = None
        self.create_window()
        self.create_header()
        self.create_content()

    def create_window(self):
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()

        window_height = int(0.5 * screen_height)
        window_width = int(0.4 * screen_width)

        position_x = int((screen_width - window_width) // 2)
        position_y = int((screen_height - window_height) // 2)

        self.window = tk.Toplevel(self.parent)
        self.window.title("Добавление автомобиля")

        self.window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    def create_header(self):

        header = tk.Frame(
            self.window, 
            bg='#2c3e50', 
            height=40
        )

        header.pack(fill='x', side='top')
        header.pack_propagate(False)

        tk.Label(
            header, 
            text="Форма добавления автомобиля",
            fg="#ecf0f1",
            bg="#2c3e50",
            font=("Roboto", 15, 'bold')  
        ).pack(pady=7)

        
        refresh = Image.open("images/refresh.png").resize((24, 24), Image.LANCZOS)
        self.refresh_image = ImageTk.PhotoImage(refresh)

        #кнопка обновления
        self.refresh_button = tk.Button(header, 
            image=self.refresh_image, 
            borderwidth=0, 
            bg='#2c3e50', 
            activebackground='#2c3e50',
            command=self.refresh_uid
        )
        self.refresh_button.place(relx=0.95, rely=0.5, anchor='center')

        #кнопки добавления
        add = Image.open("images/add.png").resize((24, 24), Image.LANCZOS)
        self.add_image = ImageTk.PhotoImage(add)
       
        self.add_button = tk.Button(header, 
            image=self.add_image, 
            borderwidth=0, 
            bg='#2c3e50', 
            activebackground='#2c3e50',
            command=self.save_car
        )
        self.add_button.place(relx=0.9, rely=0.5, anchor='center')

        tk.Frame(self.window, height=4, bg='#3498db').pack(fill='x', side='top')

    def save_car(self):
        SaveCar(self)

    def refresh_uid(self):
        new_uid = self.get_uid()
        self.uid_label.config(text=new_uid if new_uid else "UID не получен")
        state = 'normal' if new_uid else 'disabled'

        for entry in [
            self.manufacturer_entry,
            self.model_entry,
            self.year_entry,
            self.country_entry,
            self.price_entry
        ]:
            entry.delete(0, 'end')
            entry.config(state=state)
            


    def create_content(self):
        content = tk.Frame(self.window, bg='#bbbbbb')
        content.pack(fill='both', expand=True)

        #uid
        tk.Label(
            content,
            text='UID:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=0, column=0, padx=10, pady=15)
        
        self.uid_label = tk.Label(
            content,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        )

        
        recieved_uid = self.get_uid() 
        self.uid_label.config(text=recieved_uid if recieved_uid else "UID не получен")
        self.uid_label.grid(row=0, column=1, padx=10, pady=15)

        #manufacturer
        tk.Label(
            content,
            text='Производитель:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=1, column=0, padx=10, pady=15)

        self.manufacturer_entry = tk.Entry(
            content,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        )
        self.manufacturer_entry.grid(row=1, column=1, padx=10, pady=15)

        #model
        tk.Label(
            content,
            text='Модель:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=2, column=0, padx=10, pady=15)

        self.model_entry = tk.Entry(
            content,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        )
        self.model_entry.grid(row=2, column=1, padx=10, pady=15)

        #year
        tk.Label(
            content,
            text='Год:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=3, column=0, padx=10, pady=15)

        self.year_entry = tk.Entry(
            content,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        )
        self.year_entry.grid(row=3, column=1, padx=10, pady=15)

        #country
        tk.Label(
            content,
            text='Страна:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=4, column=0, padx=10, pady=15)

        self.country_entry = tk.Entry(
            content,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        )
        self.country_entry.grid(row=4, column=1, padx=10, pady=15)

        #price
        tk.Label(
            content,
            text='Цена:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=5, column=0, padx=10, pady=15)

        self.price_entry = tk.Entry(
            content,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        )
        self.price_entry.grid(row=5, column=1, padx=10, pady=15)
            
        state = 'normal' if recieved_uid else 'disabled'
        for entry in [
            self.manufacturer_entry,
            self.model_entry,
            self.year_entry,
            self.country_entry,
            self.price_entry    
        ]:
            entry.config(state=state)


    def get_uid(self):
        #return record_uid()
        if randint(1,2) == 1:
            return 'AA-BB-CC-DD'
        else:
            return None
    
