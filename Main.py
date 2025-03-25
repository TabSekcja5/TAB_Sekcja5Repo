from LoginPanel import LoginPanel
from Application import Application

class Main:
    def __init__(self):
        self.logged = False
        self.perm_level = 0
        self.login_panel = LoginPanel(self)
        self.login_panel.mainloop()
    
    def create_main_panel(self):
        self.login_panel.destroy()
        app = Application(self)        
        app.mainloop()              


if __name__ == "__main__":
    main_app = Main()
