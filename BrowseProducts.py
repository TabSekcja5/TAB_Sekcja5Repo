import customtkinter as ctk
from Perms import Perms

class BrowseProducts(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#242424")
        self.perm_level = parent.root.get_perm_level()
        self.product_list = self.generate_products_list()
        self.parent = parent
        self.create_products_list()
    
    def generate_products_list(self):
        products = []
        # TODO odczyt danych z bazy
        return products

    def create_products_list(self):
        for product in self.product_list:
            product.pack(padx = 2, pady = 2, side = 'left')

    def unpack_product_by_id(self, product_id):
        for product in self.product_list:
            if product.id == product_id:
                product.pack_forget()
    
    def add_product(self, product):
        product.pack(pady = 2, expand = True, fill = 'x')
        self.product_list.append(product)
