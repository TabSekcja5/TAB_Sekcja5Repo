import customtkinter as ctk

class LoginPanel(ctk.CTk):
    def __init__(self, root):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.root = root
        self.title("Sklep z ubraniami")
        self.geometry("600x600")
        self.create_login_screen()


    def create_registration_screen(self):
        # Usunięcie poprzednich widgetów
        for widget in self.winfo_children():
            widget.destroy()

        # Etykieta tytułowa
        title = ctk.CTkLabel(self, text="Rejestracja", font=("Arial", 18))
        title.pack(pady=20)

        # Pole na nazwę użytkownika
        username_label = ctk.CTkLabel(self, text="Nazwa użytkownika:")
        username_label.pack(pady=5)
        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.pack(pady=5)

        # Pole na e-mail
        email_label = ctk.CTkLabel(self, text="E-mail:")
        email_label.pack(pady=5)
        self.email_entry = ctk.CTkEntry(self)
        self.email_entry.pack(pady=5)

        # Pole na hasło
        password_label = ctk.CTkLabel(self, text="Hasło:")
        password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack(pady=5)

        # Przycisk rejestracji
        register_button = ctk.CTkButton(self, text="Rejestruj", command=self.register)
        register_button.pack(pady=20)

        # Przycisk przejścia do logowania
        switch_to_login_button = ctk.CTkButton(self, text="Masz już konto? Zaloguj się", command=self.create_login_screen)
        switch_to_login_button.pack(pady=10)

    def create_login_screen(self):
        # Usunięcie poprzednich widgetów
        for widget in self.winfo_children():
            widget.destroy()

        # Etykieta tytułowa
        title = ctk.CTkLabel(self, text="Logowanie", font=("Arial", 18))
        title.pack(pady=20)

        # Pole na nazwę użytkownika / e-mail
        user_email_label = ctk.CTkLabel(self, text="Nazwa użytkownika / E-mail:")
        user_email_label.pack(pady=5)
        self.user_email_entry = ctk.CTkEntry(self)
        self.user_email_entry.pack(pady=5)

        # Pole na hasło
        password_label = ctk.CTkLabel(self, text="Hasło:")
        password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack(pady=5)

        # Przycisk logowania
        login_button = ctk.CTkButton(self, text="Zaloguj", command=self.login)
        login_button.pack(pady=20)

        # Przycisk przejścia do rejestracji
        switch_to_register_button = ctk.CTkButton(self, text="Nie masz konta? Zarejestruj się", command=self.create_registration_screen)
        switch_to_register_button.pack(pady=10)

    def register(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        print(f"Rejestracja użytkownika: {username}, {email}, {password}")
        # Tu możesz dodać logikę rejestracji użytkownika

    def login(self):
        user_email = self.user_email_entry.get()
        password = self.password_entry.get()
        print(f"Logowanie użytkownika: {user_email}, {password}")
        
        # TODO logika logowania
        self.root.create_main_panel()

if __name__ == "__main__":
    root = ctk.CTk()
    app = LoginPanel(root)
    app.mainloop()
