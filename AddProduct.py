import customtkinter as ctk 
import re
from Product import Product
import sqlite3
import os

class AddProduct(ctk.CTk):
    def __init__(self, browse_products):
        super().__init__()
        self.browse_products = browse_products
        self.title("Dodaj produkt")
        self.geometry("400x500")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.create_add_product_screen()
        self.mainloop()

    def create_add_product_screen(self):
        # podpięcie funkcji walidujących
        val_int = self.register(self.validate_int)
        val_float = self.register(self.validate_float)

        # Nazwa
        self.name_label = ctk.CTkLabel(self, text="Nazwa:")
        self.name_label.pack(pady=(10, 0))
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.pack()

        # Ilość
        self.quantity_label = ctk.CTkLabel(self, text="Ilość:")
        self.quantity_label.pack(pady=(10, 0))
        self.quantity_entry = ctk.CTkEntry(self, validate="key", validatecommand=(val_int, "%P"))
        self.quantity_entry.pack()

        # Opis
        self.description_label = ctk.CTkLabel(self, text="Opis:")
        self.description_label.pack(pady=(10, 0))
        self.description_entry = ctk.CTkEntry(self)
        self.description_entry.pack()

        # Cena
        self.price_label = ctk.CTkLabel(self, text="Cena:")
        self.price_label.pack(pady=(10, 0))
        self.price_entry = ctk.CTkEntry(self, validate="key", validatecommand=(val_float, "%P"))
        self.price_entry.pack()

        # Kategoria
        self.category_label = ctk.CTkLabel(self, text="Kategoria:")
        self.category_label.pack(pady=(10, 0))
        self.category_entry = ctk.CTkEntry(self)
        self.category_entry.pack()

        # Przycisk Dodaj
        self.add_button = ctk.CTkButton(self, text="Dodaj", command=self.add_product)
        self.add_button.pack(pady=(20, 5))

        # Przycisk Anuluj
        self.cancel_button = ctk.CTkButton(self, text="Anuluj", command=self.destroy)
        self.cancel_button.pack()

    def get_product_data(self):
        return {
            "nazwa": self.name_entry.get(),
            "ilość": self.quantity_entry.get(),
            "opis": self.description_entry.get(),
            "cena": self.price_entry.get(),
            "kategoria": self.category_entry.get()
        }

    def add_product(self):
        data = self.get_product_data()
        print("Dodawanie produktu:", data) 
        name = data["nazwa"]
        quantity = data["ilość"]
        description = data["opis"]
        price = data["cena"]
        category = data["kategoria"]
        product = Product(self, name, quantity, description, price, category)
        self.browse_products.add_product(product)
        #***
        #*  Logika dodawania produktu tutaj

        db_path = "./main/bazadanych/clothing_shop_db.db"

        try:
            # Połączenie z bazą danych
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                print("Połączono!!!")

                # Sprawdzenie tabeli przed wykonaniem zapytania
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()
                print("Dostępne tabele:", tables)

                # Tymczasowo ustawiamy category_id na 1 (musisz mieć kategorię o ID 1 w tabeli categories)
                category_id = 1

                # Zapytanie SQL do wstawienia produktu
                cursor.execute("""
                            INSERT INTO products (category_id, name, description, price, stock_quantity)
                            VALUES (?, ?, ?, ?, ?)
                        """, (category_id, name, description, float(price), int(quantity)))
                print("Zapytanie wywolane")

                # Zatwierdzenie zmian w bazie
                conn.commit()
                print("Produkt zapisany w bazie danych!")

        except sqlite3.Error as e:
            print(f"Błąd podczas zapisu do bazy danych: {e}")
            return

        # Tworzenie obiektu Product i dodanie do BrowseProducts (opcjonalne na tym etapie)
        #product = Product(self, name, quantity, description, price, category)
        #self.browse_products.add_product(product)

        #***

        # zamknięcie okna po dodaniu
        self.destroy()

    # funkcjie walidujące pola liczbowe
    def validate_int(self, new_value):
        return new_value.isdigit() or new_value == ""

    def validate_float(self, new_value):
        if new_value == "":
            return True
        return bool(re.fullmatch(r"\d*(\.\d{0,2})?", new_value))