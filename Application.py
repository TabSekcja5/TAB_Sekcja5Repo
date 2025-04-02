import customtkinter as ctk
from Perms import Perms
from AddProduct import AddProduct
from BrowseProducts import BrowseProducts
from UserProfile import UserProfile

class Application(ctk.CTk):
    def __init__(self, root):
        super().__init__()

        self.root = root
        self.geometry('1200x800')
        self.title('Sklep z ubraniami')
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.main_panel = self.create_main_panel()
        self.create_buttons(self.main_panel)
        self.browse_products = BrowseProducts(self)

        # do zmiany jak baza wstanie
        self.user_profile = UserProfile(self,root.user_id,"temp Username","temp Email")

    def create_main_panel(self):
        """Tworzy główny panel na górze aplikacji."""
        main_panel = ctk.CTkFrame(self, width=1200, height=100, corner_radius=10)
        main_panel.pack(side="top", fill="x", padx=10, pady=10)
        return main_panel

    def create_buttons(self, panel):
        """Tworzy przyciski w głównym panelu."""

        # do edycji w przypadku dodania nowego panelu / modyfikacji permisji
        button_options = {
            Perms.GUEST.value: [
                "Panel główny", 
                "Przeglądaj ubrania"
                ],
            Perms.USER.value: [  
                "Panel główny", 
                "Przeglądaj ubrania", 
                "Koszyk", 
                "Profil użytkownika"
                ],
            Perms.MANAGER.value: [
                "Panel główny", 
                "Przeglądaj ubrania", 
                "Dodaj produkt", 
                "Panel Managera"
                ],
            Perms.ADMIN.value: [
                "Panel główny", 
                "Przeglądaj ubrania", 
                "Dodaj produkt", 
                "Raporty", 
                "Panel Admina"
                ],
        }
        
        button_texts = button_options.get(self.root.perm_level, [])

        for text in button_texts:
            button = ctk.CTkButton(panel, text=text, command=lambda t=text: self.button_action(t))
            button.pack(side="left", padx=10, pady=10, fill="x", expand=True)

    def button_action(self, button_name):
        """Akcja przypisana do przycisków."""
        self.hide_all()

        if button_name == "Panel główny":
            # tutaj dodajemy akcje dla przycisku "Panel główny"
            print("Panel główny")

        elif button_name == "Przeglądaj ubrania":
            # tutaj dodajemy akcje dla przycisku "Przeglądaj ubrania"
            print("Przeglądaj ubrania")
            self.browse_products.pack(fill="both", expand=True)

        elif button_name == "Dodaj produkt":
            # tutaj dodajemy akcje dla przycisku "Dodaj produkt"
            print("Dodaj produkt")
            AddProduct(self.browse_products)

        elif button_name == "Raporty":
            # tutaj dodajemy akcje dla przycisku "Raporty"
            print("Raporty")

        elif button_name == "Koszyk":
            # tutaj dodajemy akcje dla przycisku "Koszyk"
            print("Koszyk")

        elif button_name == "Profil użytkownika":
            # tutaj dodajemy akcje dla przycisku "Profil użytkownika"
            print("Profil użytkownika")
            self.user_profile.pack(fill="both", expand=True)

        elif button_name == "Panel Managera":
            # tutaj dodajemy akcje dla przycisku "Profil użytkownika"
            print("Panel Managera")

        elif button_name == "Panel Admina":
            # tutaj dodajemy akcje dla przycisku "Profil użytkownika"
            print("Panel Admina")


    def hide_all(self):
        self.browse_products.pack_forget()
        self.user_profile.pack_forget()