import customtkinter as ctk 
from IDGenerator import IDGenerator
from Perms import Perms
from EditProduct import EditProduct
import sqlite3


class Product(ctk.CTkFrame):
    def __init__(self, parent, product_id, name, quantity, description, price, category):
        super().__init__(parent)
        self.parent = parent
        self.name = name
        self.quantity = quantity
        self.description = description
        self.price = price
        self.category = category
        self.perm_level = parent.get_perm_level()
        self.product_id = product_id
        
        self.configure(fg_color="#2b2b2a")
        
        self.name_label = ctk.CTkLabel(self, text=self.name)
        self.name_label.pack(pady=(10, 0))
        self.quantity_label = ctk.CTkLabel(self, text=self.quantity)
        self.quantity_label.pack(pady=(10, 0))
        self.description_label = ctk.CTkLabel(self, text=self.description)
        self.description_label.pack(pady=(10, 0))
        self.price_label = ctk.CTkLabel(self, text=self.price)
        self.price_label.pack(pady=(10, 0))
        self.category_label = ctk.CTkLabel(self, text=self.category)
        self.category_label.pack(pady=(10, 0))
        
        if self.perm_level == Perms.MANAGER.value or self.perm_level == Perms.ADMIN.value:
            self.edit_button = ctk.CTkButton(self, text="Edytuj", command=self.edit)
            self.edit_button.pack(pady=10)
            
            self.delete_button = ctk.CTkButton(self, text="Usun", command=self.delete)
            self.delete_button.pack(pady=10)
        
    def edit(self):
        EditProduct(self)
        pass
    
    def delete(self):
        db_path = "./main/bazadanych/clothing_shop_db.db"
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM products WHERE product_id = ?", (self.product_id,))
                conn.commit()
                print(f"Produkt o ID {self.product_id} został usunięty z bazy danych.")
        except sqlite3.Error as e:
            print(f"Błąd podczas usuwania produktu z bazy danych: {e}")

        self.parent.unpack_product_by_id(self.product_id)

