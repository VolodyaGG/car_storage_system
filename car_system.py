import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from new_car import Add_New_Car
import json
from path_func import resource_path

class CarSystem:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Система хранения автомобилей")
        self.create_window()
        self.create_header()
        self.create_content()
        self.create_lower()
        self.add_car_windows = []
        

    def create_window(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        window_height = int(0.7 * screen_height)
        window_width = int(0.6 * screen_width)

        position_x = int((screen_width - window_width) // 2)
        position_y = int((screen_height - window_height) // 2)

        self.window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    def create_header(self):
        header = tk.Frame(self.window, bg='#2c3e50', height=80)
        header.pack(fill='x', side='top')

        header.pack_propagate(False)
        title_label = tk.Label(
            header,
            text="Система хранения масштабных автомобилей",
            fg="#ecf0f1",
            bg="#2c3e50",
            font=("Montserrat", 20, 'bold')
        )
        title_label.pack(expand=True)

        original_image = Image.open(resource_path("images/button.png"))
        resized_image = original_image.resize((40, 40), Image.LANCZOS)
        self.loadimage = ImageTk.PhotoImage(resized_image)

        # Кнопка справа
        button = tk.Button(header, 
            image=self.loadimage, 
            borderwidth=0, 
            bg='#2c3e50', 
            activebackground='#2c3e50',
            command=self.on_add_auto
        )
        button.place(relx=0.95, rely=0.5, anchor='center')

        tk.Frame(self.window, height=4, bg='#3498db').pack(fill='x')

    def create_content(self):
        
        container = tk.Frame(self.window)
        container.pack(fill='both', expand=True)

        my_canvas = tk.Canvas(container, bg='#bbbbbb')
        my_canvas.pack(side='top', expand=True, fill='both')

        x_scrollbar = ttk.Scrollbar(container,orient='horizontal',command=my_canvas.xview)
        x_scrollbar.pack(side='bottom',fill='x')

        my_canvas.configure(xscrollcommand=x_scrollbar.set)

        self.content = tk.Frame(my_canvas, bg='#bbbbbb')

        content_window = my_canvas.create_window((0,0),window=self.content, anchor="n")
        
        def update_scroll_region(event):
            my_canvas.configure(scrollregion=my_canvas.bbox('all'))

            canvas_height = my_canvas.winfo_height()
            content_height = self.content.winfo_height()
            y_offset = max((canvas_height - content_height) // 2, 0)
            my_canvas.coords(content_window, 0, y_offset)

        self.content.bind("<Configure>", update_scroll_region)
        my_canvas.bind("<Configure>", update_scroll_region)

        self.create_cards()

        self.window.after(100, lambda: my_canvas.xview_moveto(0))

    def create_cards(self):
        
        card_width = int(0.6 * self.window.winfo_screenwidth() / 3)
        card_height = int(0.45 * self.window.winfo_screenheight())

        try:
            with open('cars_data.json', "r", encoding='utf-8') as file:
                cars = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            cars = []

        for i in range(len(cars)):
            card = tk.Frame(
            self.content,
                bg='#3498db',
                bd=0,
                highlightthickness=2,
                highlightbackground="#2980b9",
                padx=15,
                pady=15,
                width=card_width,
                height=card_height
            )
            
            card.pack_propagate(False)
            card.grid(row=0, column=i, padx=40, pady=20)

            img_frame = tk.Frame(card, bg='#3498db')
            img_frame.pack(side='top', fill='both', expand=True)

            text_frame = tk.Frame(card, bg='#3498db')
            text_frame.pack(side='bottom', fill='x')

            if 'photo' in cars[i] and cars[i]['photo'][-4:] in ('.jpg', '.png') or cars[i]['photo'][-5:] == '.jpeg':
                img = Image.open(resource_path(cars[i]['photo']))
                img.thumbnail((card_width - 30, card_height - 100))
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(card, image=photo, bg='#3498db')
                img_label.image = photo
                img_label.pack(expand=True)

            tk.Label(
                card,
                text='Auto №'+str(i+1),
                wraplength=card_width - 20,
                font=("Roboto", 18, 'bold'),
                bg='#3498db',
                fg='white'
            ).pack(pady=5, side='top')
            
            data = (f"Производитель: {cars[i]['manufacturer']}\n"
                f"Модель: {cars[i]['model']}\n"
                f"Год: {cars[i]['year']}\n"
                f"Страна: {cars[i]['country']}\n"
                f"Цена: {cars[i]['price']}"
            )

            desc = tk.Label(
                card,
                text=data,
                bg='#3498db',
                fg='white',
                font=("Roboto", 12),
                justify='left',
                anchor='w'
            )
            desc.pack(pady=5, side='top')

            

        

    def create_lower(self):
        lower = tk.Frame(self.window, height=60, bg='#2c3e50')
        lower.pack(fill='x', side='bottom')
        
        lower.pack_propagate(False)
        tk.Label(
            lower,
            text="© MIEM HSE 2025",
            fg="#ecf0f1",
            bg="#2c3e50",
            font=("Roboto", 10)   
        ).pack(anchor='center', pady=15)

        tk.Frame(self.window, height=4, bg='#3498db').pack(fill='x', side='bottom')

    def on_add_auto(self):
        new_win = Add_New_Car(self)
        self.add_car_windows.append(new_win)

    def update_cards(self):
        for card in self.content.winfo_children():
            card.destroy()

        self.create_cards()