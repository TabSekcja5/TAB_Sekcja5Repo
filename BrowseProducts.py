import customtkinter as ctk
from Perms import Perms
from Product import Product
import sqlite3

class BrowseProducts(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#242424")
        self.perm_level = parent.root.get_perm_level()

        # Tworzenie przewijalnego kontenera
        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.configure(fg_color="#242424")
        self.scroll_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.product_list = self.generate_products_list()
        self.create_products_list()

    def get_perm_level(self):
        return self.perm_level

    def generate_products_list(self):
        products = []
        db_path = "./main/bazadanych/clothing_shop_db.db"

        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                print("Połączono z bazą danych")

                cursor.execute("""
                    SELECT p.name, p.description, p.price, p.stock_quantity, c.name
                    FROM products p
                    JOIN categories c ON p.category_id = c.category_id
                """)
                rows = cursor.fetchall()
                print("Wyniki zapytania:", rows)

                for row in rows:
                    name = row[0]
                    description = row[1]
                    price = row[2]
                    stock_quantity = row[3]
                    category_name = row[4]
                    print(f"Ładowanie produktu: {name}, {description}, {price}, {stock_quantity}, {category_name}")

                    product = Product(self, name, stock_quantity, description, price, category_name)
                    products.append(product)

                print("Produkty załadowane z bazy danych!")
        except sqlite3.Error as e:
            print(f"Błąd podczas odczytu z bazy danych: {e}")

        return products


    def create_products_list(self):
        for product in self.product_list:
            product.pack(in_=self.scroll_frame, padx=2, pady=2, side='top', fill='x')

    def refresh(self):
        #odswiez liste produktow
        for widget in self.winfo_children():
            widget.destroy()
        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.product_list = self.generate_products_list()
        self.create_products_list()

    def unpack_product_by_id(self, product_id):
        for product in self.product_list:
            if product.id == product_id:
                product.pack_forget()
