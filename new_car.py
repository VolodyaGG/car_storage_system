import tkinter as tk
from PIL import Image, ImageTk
from uid_into_py import record_uid
from random import randint
from save_car import SaveCar
from tkinter import filedialog

class Add_New_Car:
    def __init__(self, car_system):
        self.car_system = car_system
        self.parent = car_system.window
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

        window_height = int(0.6 * screen_height)
        window_width = int(0.4 * screen_width)

        position_x = int((screen_width - window_width) // 2)
        position_y = int((screen_height - window_height) // 2)

        self.window = tk.Toplevel(self.parent)
        self.window.title("Добавление автомобиля")
        self.window.transient(self.parent)
        self.window.grab_set()

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

    def create_content(self):

        content = tk.Frame(self.window, bg='#bbbbbb')
        content.pack(fill='both', expand=True)
        
        form_frame = tk.Frame(content, bg='#bbbbbb')
        form_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        pady = 0.018 * self.parent.winfo_screenheight()

        # UID
        tk.Label(
            form_frame,
            text='UID:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=0, column=0, padx=10, pady=pady, sticky='e')
        
        self.uid_label = tk.Label(
            form_frame,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        )
        
        recieved_uid = self.get_uid() 
        self.uid_label.config(text=recieved_uid if recieved_uid else "UID не получен")
        self.uid_label.grid(row=0, column=1, padx=10, pady=pady)

        # Производитель
        tk.Label(
            form_frame,
            text='Производитель:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=1, column=0, padx=10, pady=pady, sticky='e')

        self.manufacturer_entry = tk.Entry(
            form_frame,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold'),
            width=25  
        )
        self.manufacturer_entry.grid(row=1, column=1, padx=10, pady=pady)

        # Модель
        tk.Label(
            form_frame,
            text='Модель:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=2, column=0, padx=10, pady=pady, sticky='e')

        self.model_entry = tk.Entry(
            form_frame,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold'),
            width=25
        )
        self.model_entry.grid(row=2, column=1, padx=10, pady=pady)

        # Год
        tk.Label(
            form_frame,
            text='Год:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=3, column=0, padx=10, pady=pady, sticky='e')

        self.year_entry = tk.Entry(
            form_frame,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold'),
            width=25
        )
        self.year_entry.grid(row=3, column=1, padx=10, pady=pady)

        # Страна
        tk.Label(
            form_frame,
            text='Страна:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=4, column=0, padx=10, pady=pady, sticky='e')

        self.country_entry = tk.Entry(
            form_frame,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold'),
            width=25
        )
        self.country_entry.grid(row=4, column=1, padx=10, pady=pady)

        # Цена
        tk.Label(
            form_frame,
            text='Цена:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=5, column=0, padx=10, pady=pady, sticky='e')

        self.price_entry = tk.Entry(
            form_frame,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold'),
            width=25
        )
        self.price_entry.grid(row=5, column=1, padx=10, pady=pady)

        # Картинка
        tk.Label(
            form_frame,
            text='Изображение:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=6, column=0, padx=10, pady=pady, sticky='e')

        choose_photo = Image.open("images/choose.png").resize((220, 50), Image.LANCZOS)
        self.choose_image = ImageTk.PhotoImage(choose_photo)

        self.choose_button = tk.Button(form_frame, 
            image=self.choose_image, 
            borderwidth=0, 
            bg='#bbbbbb', 
            activebackground='#bbbbbb',
            command=self.choose_photo
        )
        self.choose_button.grid(row=6, column=1, padx=10, pady=pady)
            

        state = 'normal' if recieved_uid else 'disabled'
        for entry in [
            self.manufacturer_entry,
            self.model_entry,
            self.year_entry,
            self.country_entry,
            self.price_entry,
            self.choose_button    
        ]:
            entry.config(state=state)

    def refresh_uid(self):
        new_uid = self.get_uid()
        self.uid_label.config(text=new_uid if new_uid else "UID не получен")
        state = 'normal' if new_uid else 'disabled'

        for entry in [
            self.manufacturer_entry,
            self.model_entry,
            self.year_entry,
            self.country_entry,
            self.price_entry,
        ]:
            entry.delete(0, 'end')
            entry.config(state=state)

        self.choose_button.config(state=state)

    def get_uid(self):
        UID = record_uid()
        if UID != None:
            return UID
        else:
            return None
        '''
        if randint(1,2) == 1:
            string = ""
            hex_numbers = '0123456789ABCDEF'
            for index in range (8):
                string += hex_numbers[randint(0,15)]
                if index % 2 == 1 and index !=7:
                    string += "-"
            return string
        else:
            return None'''
        
    def choose_photo(self):
        filetypes = (
            ('Image files', '*.jpg *.jpeg *.png'),
            ('All files', '*.*')
        )

        filename = filedialog.askopenfilename(
            title = 'Выберите изображение автомобиля',
            initialdir='/',
            filetypes=filetypes    
        )

        if filename:
            self.photo_path = filename

    
