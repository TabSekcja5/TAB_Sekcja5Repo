import customtkinter as ctk
from Perms import Perms

class UserProfile(ctk.CTkFrame):
    def __init__(self, parent, user_id, username, email):
        super().__init__(parent)
        self.configure(fg_color="#242424")
        self.perm_level = parent.root.get_perm_level()
        self.parent = parent

        #TODO pobranie danych z bazy

        self.id = user_id
        self.username = username
        self.email = email
        self.balance = 100.10

        profile_frame = ctk.CTkFrame(self, corner_radius=10)  # Prostokątna ramka
        profile_frame.pack(pady=20, padx=10, fill="x")

        welcome_label = ctk.CTkLabel(
            profile_frame, 
            text=f"Profil użytkownika {self.username}",
            font=("Arial", 20, "bold"),  
            fg_color="transparent"
        )
        welcome_label.pack(pady=10)

        your_userdata = ctk.CTkLabel(
            profile_frame, 
            text=f"Twoje dane:",
            font=("Arial", 14, "bold"),
        )
        your_userdata.pack(pady=2, padx=40, anchor="w")

        self.add_paragraph(profile_frame,f"Nazwa użytkownika: {self.username}")
        self.add_paragraph(profile_frame,f"Email: {self.email}")
        self.add_paragraph(profile_frame,f"Bilans konta: {self.balance} zł")

        line = ctk.CTkFrame(profile_frame, height=2, fg_color="white")
        line.pack(fill="x", pady=20, padx = 20)

        self.create_buttons(profile_frame)
        
    def add_paragraph(self, frame, text_str):
        text_label = ctk.CTkLabel(
            frame, 
            text=text_str,
            font=("Arial", 14),
        )
        text_label.pack(pady=2, padx=40, anchor="w")

    # tworzy buttony w ramce profilu
    def create_buttons(self, frame):

        button_frame = ctk.CTkFrame(frame, corner_radius=5, fg_color="#333333")
        button_frame.pack(pady=10, padx=10, fill="x", expand=True)

        button_texts = [
            "Modyfikuj dane", 
            "Historia zamówień",
            "Portfel"
        ]

        for text in button_texts:
            button = ctk.CTkButton(button_frame, text=text, command=lambda t=text: self.button_action(t))
            button.pack(side="left", padx=10, pady=10, fill="x", expand=True)

    # prypisanie akcji do przycisków
    def button_action(self, button_name):
        if button_name == "Modyfikuj dane":
            print("Modyfikuj dane")

        if button_name == "Historia zamówień":
            print("Historia zamówień")

        if button_name == "Portfel":
            print("Portfel")


