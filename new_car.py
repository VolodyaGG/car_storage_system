import tkinter as tk
from PIL import Image, ImageTk
from uid_into_py import record_uid


class Add_New_Car:
    def __init__(self, parent):
        self.parent = parent
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

        
        refresh = Image.open("refresh.png").resize((24, 24), Image.LANCZOS)
        self.refresh_image = ImageTk.PhotoImage(refresh)

        #кнопка обновления
        self.refresh_button = tk.Button(header, 
            image=self.refresh_image, 
            borderwidth=0, 
            bg='#2c3e50', 
            activebackground='#2c3e50'
        )
        self.refresh_button.place(relx=0.95, rely=0.5, anchor='center')

        #кнопки добавления
        add = Image.open("add.png").resize((24, 24), Image.LANCZOS)
        self.add_image = ImageTk.PhotoImage(add)
       
        self.add_button = tk.Button(header, 
            image=self.add_image, 
            borderwidth=0, 
            bg='#2c3e50', 
            activebackground='#2c3e50'
        )
        self.add_button.place(relx=0.9, rely=0.5, anchor='center')

        tk.Frame(self.window, height=4, bg='#3498db').pack(fill='x', side='top')



    

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
        
        uid = tk.Label(
            content,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        )

        
        recieved_uid = self.get_uid()
        uid.config(text=recieved_uid)

        uid.grid(row=0, column=1, padx=10, pady=15)

        #manufacturer
        tk.Label(
            content,
            text='Производитель:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=1, column=0, padx=10, pady=15)

        manufacturer_entry = tk.Entry(
            content,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        )
        manufacturer_entry.grid(row=1, column=1, padx=10, pady=15)

        #model
        tk.Label(
            content,
            text='Модель:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=2, column=0, padx=10, pady=15)

        model_entry = tk.Entry(
            content,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        )
        model_entry.grid(row=2, column=1, padx=10, pady=15)

        #year
        tk.Label(
            content,
            text='Год:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=3, column=0, padx=10, pady=15)

        year_entry = tk.Entry(
            content,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        )
        year_entry.grid(row=3, column=1, padx=10, pady=15)

        #country
        tk.Label(
            content,
            text='Страна:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=4, column=0, padx=10, pady=15)

        country_entry = tk.Entry(
            content,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        )
        country_entry.grid(row=4, column=1, padx=10, pady=15)

        #price
        tk.Label(
            content,
            text='Цена:',
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        ).grid(row=5, column=0, padx=10, pady=15)

        price_entry = tk.Entry(
            content,
            fg="#2c3e50",
            bg="#bbbbbb",
            font=("Roboto", 15, 'bold')    
        )
        price_entry.grid(row=5, column=1, padx=10, pady=15)

        if not recieved_uid:
            uid.config(text="UID не получен")
            manufacturer_entry.config(state='disabled')
            model_entry.config(state='disabled')
            year_entry.config(state='disabled')
            country_entry.config(state='disabled')
            price_entry.config(state='disabled')
        else:
            manufacturer_entry.config(state='normal')
            model_entry.config(state='normal')
            year_entry.config(state='normal')
            country_entry.config(state='normal')
            price_entry.config(state='normal')



    def get_uid(self):
        #return record_uid
        #return 'AA-BB-CC-DD'
        return None