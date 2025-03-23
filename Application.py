import customtkinter as ctk
class Application(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('1200x800')
        self.title('Sklep z ubraniami')
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.main_panel = self.create_main_panel()
        self.create_buttons(self.main_panel)

    def create_main_panel(self):
        """Tworzy główny panel na górze aplikacji."""
        main_panel = ctk.CTkFrame(self, width=1200, height=100, corner_radius=10)
        main_panel.pack(side="top", fill="x", padx=10, pady=10)
        return main_panel

    def create_buttons(self, panel):
        """Tworzy przyciski w głównym panelu."""
        button_texts = [
            "Panel główny", 
            "Przeglądaj ubrania", 
            "Dodaj produkt", 
            "Raporty", 
            "Koszyk", 
            "Profil użytkownika"
        ]
        
        for text in button_texts:
            button = ctk.CTkButton(panel, text=text, command=lambda t=text: self.button_action(t))
            button.pack(side="left", padx=10, pady=10, fill="y", expand=True)

    def button_action(self, button_name):
        """Akcja przypisana do przycisków."""
        if button_name == "Panel główny":
            # tutaj dodajemy akcje dla przycisku "Panel główny"
            print("Panel główny")
        elif button_name == "Przeglądaj ubrania":
            # tutaj dodajemy akcje dla przycisku "Przeglądaj ubrania"
            print("Przeglądaj ubrania")
        elif button_name == "Dodaj produkt":
            # tutaj dodajemy akcje dla przycisku "Dodaj produkt"
            print("Dodaj produkt")
        elif button_name == "Raporty":
            # tutaj dodajemy akcje dla przycisku "Raporty"
            print("Raporty")
        elif button_name == "Koszyk":
            # tutaj dodajemy akcje dla przycisku "Koszyk"
            print("Koszyk")
        elif button_name == "Profil użytkownika":
            # tutaj dodajemy akcje dla przycisku "Profil użytkownika"
            print("Profil użytkownika")