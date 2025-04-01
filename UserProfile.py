import customtkinter as ctk

class UserProfile(ctk.CTkFrame):
    def __init__(self, parent, user_id, username, email):
        super().__init__(parent)
        self.configure(fg_color="#242424")
        self.perm_level = parent.root.get_perm_level()
        self.parent = parent

        self.id = user_id
        self.username = username
        self.email = email
        
        # TODO - wy�wietlanie profilu u�ytkownika z mo�liwo�ci� zmiany danych
        # do zrobienia jak baza wstanie