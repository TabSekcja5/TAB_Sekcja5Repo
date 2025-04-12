import customtkinter as ctk 
from IDGenerator import IDGenerator
from Perms import Perms


class Product(ctk.CTkFrame):
    def __init__(self, parent, name, quantity, description, price, category):
        super().__init__(parent)
        self.parent = parent
        self.id = IDGenerator().generate_id()
        self.name = name
        self.quantity = quantity
        self.description = description
        self.price = price
        self.category = category
        self.perm_level = parent.get_perm_level()
        
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
        #* Implementacja edycji produktu
        pass
    
    def delete(self):
        self.parent.unpack_product_by_id(self.id)
        #* Implementacja usuwania produktu

